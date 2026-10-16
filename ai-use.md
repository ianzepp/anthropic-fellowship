# How AI was used

This is a plain statement of who did what, across all the work linked
from this repository.

## The operator's role

Ian Zepp directs the work. That means choosing the questions, designing
the process and the test frameworks, defining scenarios and their
variants, writing predictions, raising edge cases, ruling on disputed
decisions, and labeling gold data by hand. In the Faber process this is
about one message in twenty (see [`agent-process.md`](agent-process.md)).

## The agents' role

None of the implementation code in the linked repositories was written
by hand. AI agents produced and managed it under that direction:
Claude Code, Codex, OpenCode, and other models coordinated through Vivi
and Tugboat. Independent AI auditors review the implementers' output, and
regularly send it back.

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
