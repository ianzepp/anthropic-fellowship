# How AI was used

This is a plain statement of who did what, across all the work linked
from this repository.

## The operator's role

Ian Zepp directs the work. That means choosing the questions, designing
the process and the test frameworks, defining scenarios and their
variants, writing predictions, raising edge cases, ruling on disputed
decisions, and labeling gold data by hand. The operator directs through chat sessions
with the agent assigned the Mind role, which coordinates the other
agents (see [`agent-process.md`](agent-process.md)).

## The agents' role

None of the implementation code in the linked repositories was written
by hand. AI agents produced and managed it under that direction:
Claude Code, Codex, OpenCode, and other models coordinated through Vivi
and Tugboat. Independent AI auditors review the implementers' output, and
regularly send it back.

Radix, the Faber compiler monorepo, was built the way an architect
builds a skyscraper. The operator held the vision, iterated the plans,
and supervised the agents doing the implementation, using different
agents for different parts of the build. The operator did not write a
single line of it. A count on 2026-10-17 found about 1.37 million lines
of code, of which about 1.28 million are Rust. "Built Radix" on the
resume means this.

The commit history runs from the initial commit on 2025-12-20 through
2026-10-16. HEAD has 24,328 commits. The git author on 24,107 of them
is Ian Zepp, because the agents commit under his identity. The other
221 are committed under model or hand names. The pace is back-loaded.
There were no commits in March 2026. October is through the 16th, so
that month is not finished.

| Month | Commits |
| --- | ---: |
| 2025-12 | 608 |
| 2026-01 | 902 |
| 2026-02 | 89 |
| 2026-03 | 0 |
| 2026-04 | 37 |
| 2026-05 | 417 |
| 2026-06 | 1,493 |
| 2026-07 | 3,983 |
| 2026-08 | 7,055 |
| 2026-09 | 2,360 |
| 2026-10 | 7,384 |

## Gradus and Triga

Two public libraries written in Faber sit beside the compiler.
[Gradus](https://github.com/faberlang/gradus) is the ML and inference
library. Its Faber source covers tensors, gradients, training, and
generation, and `src/kernel.fab` holds the device entries: `@ kernel`
functions for RMSNorm, GEMM, RoPE, softmax, and SwiGLU. Those entries
are Faber. The compiler lowers them. The host-side modules are ordinary
Faber in the same library, so the language is doing both the CPU-side
program and the GPU-side kernel. Gradus has 1,252 commits, from
2026-08-03 through 2026-10-16, 1,109 of them in August.
[Triga](https://github.com/faberlang/triga) is the graphics and geometry
library, also Faber: meshes, scene graphs, and shader contracts that
emit WGSL. It has 622 commits, from 2026-07-09 through 2026-10-16.
Same authorship as Radix: the operator directed the build and did not
hand-write the implementation.

## The trials project specifically

The authorship of `llm-pressure-trials` is recorded period by period in
its README. Two points are worth repeating here:

- In October 2026, Claude declined to write the adversarial prompt
  variants for the re-run studies. GLM 5.3 wrote them, and carried out
  the rest of the October work.
- GLM 5.3 was also one of the October judges and a subject in the
  October cohort. That overlap is disclosed in the repository's
  limitations.

## This repository

The documents here were drafted by Claude (Opus 5.5) from the operator's
direction and from measured data, and reviewed by the operator.
