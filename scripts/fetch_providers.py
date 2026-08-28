#!/usr/bin/env python3
"""Pull public provider catalogs and refresh README + JSON snapshots."""
from __future__ import annotations

import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
HISTORY = DATA / "history"
README = ROOT / "README.md"
OPENROUTER = "https://openrouter.ai/api/v1/models"


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def fetch_openrouter() -> list[dict]:
    req = urllib.request.Request(
        OPENROUTER,
        headers={"User-Agent": "free-coding-agent-models/1.0 (student tracker)"},
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        payload = json.load(resp)
    models = payload.get("data") or []
    free = []
    for model in models:
        pricing = model.get("pricing") or {}
        try:
            prompt = float(pricing.get("prompt") or 1)
            completion = float(pricing.get("completion") or 1)
        except (TypeError, ValueError):
            continue
        if prompt != 0 or completion != 0:
            continue
        free.append(
            {
                "id": model.get("id"),
                "name": model.get("name"),
                "context_length": model.get("context_length"),
                "pricing": pricing,
            }
        )
    free.sort(key=lambda row: (row.get("name") or row.get("id") or "").lower())
    return free, len(models)


def fmt_ctx(value) -> str:
    try:
        n = int(value)
    except (TypeError, ValueError):
        return "—"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.0f}M" if n % 1_000_000 == 0 else f"{n / 1_000_000:.1f}M"
    if n >= 1000:
        return f"{n // 1000}K"
    return str(n)


def table_md(rows: list[dict]) -> str:
    lines = [
        "| Model ID | Name | Context |",
        "| --- | --- | --- |",
    ]
    for row in rows:
        mid = row.get("id") or ""
        name = row.get("name") or mid
        lines.append(f"| `{mid}` | {name} | {fmt_ctx(row.get('context_length'))} |")
    return "\n".join(lines)


def replace_section(text: str, start: str, end: str, body: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    replacement = start + "\n\n" + body.strip() + "\n\n" + end
    if not pattern.search(text):
        raise SystemExit(f"README markers missing: {start} / {end}")
    return pattern.sub(replacement, text, count=1)


def main() -> None:
    DATA.mkdir(exist_ok=True)
    HISTORY.mkdir(parents=True, exist_ok=True)
    now = utc_now()
    free, total = fetch_openrouter()
    snapshot = {
        "fetched_at": now.isoformat(),
        "source": OPENROUTER,
        "total_models": total,
        "free_models": len(free),
        "models": free,
    }
    (DATA / "openrouter-free.json").write_text(json.dumps(snapshot, indent=2) + "\n")
    (HISTORY / f"{now.date().isoformat()}.json").write_text(json.dumps(snapshot, indent=2) + "\n")

    readme = README.read_text()
    readme = re.sub(
        r"- Live OpenRouter catalog pulled: \*\*\d+\*\* models",
        f"- Live OpenRouter catalog pulled: **{total}** models",
        readme,
        count=1,
    )
    readme = re.sub(
        r"- Priced at \$0 input \+ \$0 output today: \*\*\d+\*\* models",
        f"- Priced at $0 input + $0 output today: **{len(free)}** models",
        readme,
        count=1,
    )
    readme = re.sub(
        r"\*\*Honest headline \(\d{{4}}-\d{{2}}-\d{{2}}\):",
        f"**Honest headline ({now.date().isoformat()}):",
        readme,
        count=1,
    )
    start = "<!-- OPENROUTER_FREE_START -->"
    end = "<!-- OPENROUTER_FREE_END -->"
    if start not in readme:
        # First-run compatibility: inject markers around the generated table if absent.
        readme = readme.replace(
            "## OpenRouter $0 models today (live pull)",
            "## OpenRouter $0 models today (live pull)\n\n" + start + "\n" + end,
            1,
        )
    generated = (
        f"Pulled from `GET {OPENROUTER}` with `pricing.prompt == 0` and "
        f"`pricing.completion == 0` on {now.strftime('%Y-%m-%d %H:%M UTC')}.\n\n"
        + table_md(free)
    )
    readme = replace_section(readme, start, end, generated)
    README.write_text(readme)
    print(f"Wrote {len(free)} free models / {total} total")


if __name__ == "__main__":
    main()
