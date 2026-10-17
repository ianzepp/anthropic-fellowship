# Evidence

Public repositories behind this application, grouped by what they show.
Repositories marked *private* are named for completeness; the statistics
drawn from them are published here as aggregates only.

## How the October work was produced

Verbatim sessions are in [`transcripts/`](transcripts/). The Claude
session is where a safety classifier stopped drafting for this
application. The GLM 5.3 session is where the October grid was run.

## AI safety research

- **llm-pressure-trials** (*private until submission*;
  `github.com/ianzepp/llm-pressure-trials`). Behavioral pressure trials
  run January–March 2026 and re-run against current models in October
  2026, with pre-registered predictions and a grader audit. Summary in
  [`research-summary.md`](research-summary.md).

## Directing AI agents

- [ianzepp/vivi](https://github.com/ianzepp/vivi). Local-first project
  mailspace for LLM agents: tasks, mail, roles, and work graphs, plus the
  Tugboat, Speedboat, and Pump coordination tools.
- [ianzepp/tugboat](https://github.com/ianzepp/tugboat). The
  Mind/Hand/Cadence multi-agent protocol on Vivi.
- [ianzepp/fleet](https://github.com/ianzepp/fleet). Mind/Head/Hand
  multi-agent project loops.
- [ianzepp/cassio](https://github.com/ianzepp/cassio). Converts session
  logs into readable transcripts. It produced the files in
  [`transcripts/`](transcripts/), and it is the provenance source for the
  trials work. The public repo description names Claude Code, Codex, and
  OpenCode. The exports here also include Grok sessions.
- Process measurements: [`agent-process.md`](agent-process.md).

## Security-adjacent engineering

- [ianzepp/interface-ai-th1](https://github.com/ianzepp/interface-ai-th1).
  LLM-authored browser capabilities and their deterministic replay, with
  reviewed evidence and a credential-scanning commit gate.

## Minted Geek Swarm

Minted Geek's agent platform, built through the same process. The
source repositories are private; the measured statistics are in
[`agent-process.md`](agent-process.md).

- [mintedgeek/releases](https://github.com/mintedgeek/releases): public
  binary releases of the Minted Geek tools.

## The Faber language

Faber is a programming language and compiler built through the process
in [`agent-process.md`](agent-process.md).

- [faberlang/faber](https://github.com/faberlang/faber)
- [faberlang/norma](https://github.com/faberlang/norma)
- [faberlang/gradus](https://github.com/faberlang/gradus). The ML and
  inference library, written in Faber. The source covers tensors,
  gradients, loss, optimizers, neural-net primitives, training,
  tokenization, and generation, including admission of GGUF and
  Safetensors models. `src/kernel.fab` is the device side: `@ kernel`
  entries for RMSNorm, GEMM, RoPE, softmax, and SwiGLU, written in Faber
  and lowered by the compiler. The host-side modules are ordinary Faber.
  1,252 commits, 2026-08-03 through 2026-10-16.
- [faberlang/triga](https://github.com/faberlang/triga). The graphics and
  geometry library, also written in Faber. It is the data contract
  between compiled Faber and a GPU host: meshes, scene graphs, and
  shader contracts that emit WGSL. 622 commits, 2026-07-09 through
  2026-10-16.
- [faberlang/tela](https://github.com/faberlang/tela)
- [faberlang/tree-sitter-faber](https://github.com/faberlang/tree-sitter-faber)
- [faberlang/faberlang.dev](https://github.com/faberlang/faberlang.dev)
- `faberlang/radix`, the compiler monorepo (*private*; 19,115 commits
  between 2026-07-09 and 2026-10-16).
