# Free coding & agent models (daily tracker)

Student-focused snapshot of providers that advertise **free** models for coding and agentic frameworks.

**Honest headline (2026-09-01):** almost no hosted API is truly unlimited. Most “free unlimited” claims hide RPM/RPD caps, weekly quotas, or rotating model IDs. The only reliably unlimited path is **local inference** (Ollama, LM Studio, llama.cpp).

This repo is updated daily by GitHub Actions from public provider catalogs (starting with OpenRouter’s unauthenticated `/api/v1/models`).

- Live OpenRouter catalog pulled: **418** models
- Priced at $0 input + $0 output today: **21** models

## Verdict for students

| Claim | Reality |
| --- | --- |
| “Free unlimited API” | Rare. Hosted free tiers almost always cap requests/day or tokens/day. |
| Best $0 coding APIs | Google AI Studio (Gemini Flash family), Groq, OpenRouter `:free`, NVIDIA NIM (~40 RPM), Z.ai Flash |
| Best $0 coding *agents* | OpenCode Zen, Kilo Code, Google Antigravity (weekly quota), Codex CLI on free ChatGPT |
| Truly unlimited | Local models on your machine |

## What providers say vs what you get

### Hosted APIs (free, usually not unlimited)

| Provider | What they say | Practical limit (as of 2026-09-01) | Card? | Coding / agents |
| --- | --- | --- | --- | --- |
| [OpenRouter `:free`](https://openrouter.ai/collections/free-models) | Models with $0 pricing | **20 RPM / 50 RPD** account-wide; **1000 RPD** after a one-time $10 credit purchase | No | Yes — Nemotron 3 Ultra, Laguna S 2.1, North Mini Code, Gemma 4, GLM 5.2 |
| [Google AI Studio / Gemini API](https://aistudio.google.com) | Free of charge on listed Flash models | Per-model RPM/RPD (Flash often ~10–15 RPM, hundreds–1000 RPD). Free-tier prompts may be used to improve products. Pro often paid-only | No | Strong for agents (1M context, tool use) |
| [Groq](https://console.groq.com) | Free plan with published rate table | ~30 RPM; RPD often ~1,000 on chat models (higher on small). Catalog churns | No | Fast; gpt-oss, qwen3.x |
| [GitHub Models](https://github.com/marketplace/models) | Free inference with a GitHub account | Rate-limited by plan (~10–15 RPM, 50–150 RPD). **New customers blocked since Jun 2026** | No | Existing accounts only |
| [NVIDIA NIM](https://build.nvidia.com) | Free developer endpoints | ~40 RPM trial (no credits system); not for production | No (dev signup) | Nemotron family is agent-oriented |
| [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) | Free daily neuron allotment | **10,000 Neurons/day** (shared, resets 00:00 UTC) | No | Light coding only |
| [Z.ai / GLM](https://z.ai) | Some Flash models free on API | GLM-4.7-Flash / 4.5-Flash free; flagship paid or Coding Plan quotas | No for Flash | GLM Flash usable for code |
| [Pollinations](https://pollinations.ai) | Often listed as unlimited / no-auth | Legacy anonymous throttled (~1 req/3–5s); newer endpoints need key / pollen | No | Weak for multi-step agents |
| [Mistral La Plateforme](https://console.mistral.ai) | Free mode / monthly allowance | Allowance, not unlimited | No | Codestral when included |

### Coding agents that include $0 models

| Agent | $0 models named in recent probes | Limit |
| --- | --- | --- |
| [OpenCode](https://opencode.ai) | big-pickle, mimo-v2.5, ling-3.0-flash-fin, nemotron-3-ultra, nemotron-3.5-lightning, muse-spark-1.2 | Zen free IDs rotate; BYOK also works |
| [Kilo Code](https://kilo.ai) | nemotron-3-ultra/super, north-mini-code, laguna-s/xs-2.1 (~200 req/hr) | $0 hosted pool, rotating IDs |
| [Google Antigravity](https://antigravity.google) | gemini + Claude + gpt-oss on free plan | Weekly quota under “unlimited” language |
| [OpenAI Codex CLI](https://learn.chatgpt.com/docs/codex/cli) | gpt on free ChatGPT | Shared 5-hour + weekly rate limits |

### Actually unlimited (local)

| Tool | Note |
| --- | --- |
| [Ollama](https://ollama.com) | OpenAI-compatible local server. Unlimited on your hardware. |
| [LM Studio](https://lmstudio.ai) | GUI + local server. |
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | Lowest-level local runtime. |

## OpenRouter $0 models today (live pull)

<!-- OPENROUTER_FREE_START -->

Pulled from `GET https://openrouter.ai/api/v1/models` with `pricing.prompt == 0` and `pricing.completion == 0` on 2026-09-01 14:28 UTC.

| Model ID | Name | Context |
| --- | --- | --- |
| `cohere/north-mini-code:free` | Cohere: North Mini Code (free) | 256K |
| `dots-studio/dots-3-note-preview:free` | Dots Studio: Dots3-Note Preview (free) | 512K |
| `google/gemma-4-26b-a4b-it:free` | Google: Gemma 4 26B A4B  (free) | 262K |
| `google/gemma-4-31b-it:free` | Google: Gemma 4 31B (free) | 262K |
| `google/lyria-3-clip-preview` | Google: Lyria 3 Clip Preview | 1M |
| `google/lyria-3-pro-preview` | Google: Lyria 3 Pro Preview | 1M |
| `inclusionai/ling-3.0-flash-fin:free` | Ling 3.0 Flash Fin (free) | 262K |
| `liquid/lfm-2.5-2.6b:free` | LiquidAI: LFM2.5-2.6B (free) | 65K |
| `minimax/minimax-m2.7:free` | MiniMax: MiniMax M2.7 (free) | 196K |
| `minimax/minimax-m3:free` | MiniMax: MiniMax M3 (free) | 1M |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | NVIDIA: Nemotron 3 Nano Omni (free) | 256K |
| `nvidia/nemotron-3-super-120b-a12b:free` | NVIDIA: Nemotron 3 Super (free) | 262K |
| `nvidia/nemotron-3-ultra-550b-a55b:free` | NVIDIA: Nemotron 3 Ultra (free) | 1M |
| `nvidia/nemotron-3.5-content-safety:free` | NVIDIA: Nemotron 3.5 Content Safety (free) | 128K |
| `nvidia/nemotron-3.5-lightning:free` | NVIDIA: Nemotron 3.5 Lightning (free) | 1M |
| `openrouter/free` | Free Models Router | 200K |
| `poolside/laguna-s-2.1:free` | Poolside: Laguna S 2.1 (free) | 262K |
| `poolside/laguna-xs-2.1:free` | Poolside: Laguna XS 2.1 (free) | 262K |
| `thinkingmachines/inkling-small:free` | Thinking Machines: Inkling Small (free) | 1M |
| `thinkingmachines/inkling:free` | Thinking Machines: Inkling (free) | 1M |
| `z-ai/glm-5.2:free` | Z.ai: GLM 5.2 (free) | 256K |

<!-- OPENROUTER_FREE_END -->

Best coding-oriented IDs in that list today: `poolside/laguna-s-2.1:free`, `cohere/north-mini-code:free`, `nvidia/nemotron-3-ultra-550b-a55b:free`, `nvidia/nemotron-3.5-lightning:free`, `z-ai/glm-5.2:free`.

## How the daily Action works

```
.github/workflows/daily.yml
        |
        v
scripts/fetch_providers.py
        |
        +-- GET openrouter.ai/api/v1/models  (no key)
        |     filter prompt+completion price == 0
        |
        +-- writes data/openrouter-free.json
        +-- writes data/history/YYYY-MM-DD.json
        +-- refreshes the OpenRouter table in README.md
```

Schedule: every day at 04:00 UTC (also runnable from the Actions tab).

## Student notes

1. Prefer **official free tiers** (Gemini, Groq, OpenRouter, NVIDIA NIM) over unofficial “unlimited Claude/GPT” proxies. Those break, get keys revoked, and often violate provider ToS.
2. Free model IDs **rotate**. Hard-coding one ID will fail within weeks. Keep a fallback list.
3. OpenRouter `:free` is one key for many models but is **request-capped**, not token-unlimited.
4. For class projects that must not die mid-demo: run a local model, and use a hosted free tier as backup.
5. Community trackers used as secondary sources: [awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding), [ClawLabsAI/free-ai-models](https://github.com/ClawLabsAI/free-ai-models).

## License

CC0-1.0 for the compiled tables. Provider names and model IDs belong to their owners.
