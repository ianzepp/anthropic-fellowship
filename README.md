# Anthropic Fellowship application: Ian Zepp

Supporting material for an application to the Anthropic Fellows Program
(security focus), January 2027 cohort.

## Contents

| Document | What it covers |
| --- | --- |
| [`research-summary.md`](research-summary.md) | The LLM pressure trials: pre-registered predictions, a grader audit, and October 2026 re-runs on 43 models |
| [`agent-process.md`](agent-process.md) | Measured statistics on how one operator directs AI agents to build the Faber language |
| [`ai-use.md`](ai-use.md) | Who did what: the operator's role and the agents' role, stated plainly |
| [`evidence.md`](evidence.md) | Links to the public repositories behind each claim |
| [`transcripts/`](transcripts/) | The Claude drafting session, the GLM session that directed the October grid, and the five hands that wrote it |
| [`responses/`](responses/) | The answers submitted on the application form |

## Reproducing the numbers

[`scripts/vivi_stats.py`](scripts/vivi_stats.py) produces every figure in
`agent-process.md` from the project's Vivi database, read-only. Its
output is committed in [`data/`](data/) and contains counts only.

## Status

Submitted on 2026-10-17 through the Constellation application form.
The form answers are in [`responses/`](responses/). This repository and
`llm-pressure-trials` were made public for the submission. Local notes that name other people are not in the
repository.
