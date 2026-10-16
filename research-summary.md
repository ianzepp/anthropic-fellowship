# Research summary: LLM pressure trials

Repository: `github.com/ianzepp/llm-pressure-trials` (private until
submission). Start with `docs/findings/overview.md` there.

## What it is

Behavioral red-team trials on how language models respond to pressure:
format and framing shifts, invented authority, coercion after a refusal,
and lethal-decision thresholds. The trials were run against the models
available in January and March 2026. In October 2026 they were audited
and re-run against 43 current models, about 3,680 new trials across
eight studies.

## How it was done

- **Provenance.** Dates are backed by git history, checksummed data
  files, and session transcripts captured at the time.
- **Pre-registration.** The operator's predictions were written and
  committed before any October run, and were never edited afterwards.
- **A 2×2 grid.** Old grader against new grader, March runs against
  October runs. This separates grader error from changes in model
  behavior.
- **Grader validation.** The corrected grading stack scored 96% against
  hand-labeled gold data, and the labels were checked by blind
  verifiers from two other model families.

## What it found

1. **The original grader made up results, in both directions.** There
   were 44 flips between refusal and decision, 30 of them on Claude
   Sonnet 4.6. Read as stored, the March data said invented authority
   broke Claude. The transcripts show the opposite.
2. **One reported effect never existed.** The stored data said a
   military-report format halved refusals. Regraded, the rates are 15%
   and 16%.
3. **The split between providers flipped.** In March, OpenAI and
   Anthropic models refused while Grok and the Chinese models decided.
   In October it ran the other way.
4. **Who the victims are didn't move decisions; the odds did.**
5. **Models trusted their own judgment over invented authority.** They
   carried out a strike they had just recommended 91% of the time, but
   one that a fabricated handoff said they had approved only 44% of the
   time.
6. **Silence was the token budget, not safety filters.** 849 of 861
   October non-answers ran out of tokens while reasoning. None of them
   came from a content filter on a Claude model.

## The predictions

24 pre-registered verdicts: 7 supported, 7 partly supported, 10 not
supported. The operator's guesses about which providers would refuse
were mostly wrong. The structural guesses were mostly right: that
victim identity wouldn't matter, that strike thresholds would be tight,
that models would defer to their own judgment, and that asking for an
opinion would get answers where asking for a decision wouldn't. The
misses are reported in full.

## Limits

- GLM 5.3 wrote the October code and analysis, was one of the two
  October judges, and was also a subject. The hand-labeled gold set
  covers March data only.
- Some trials failed twice, and one model rejected multi-turn requests
  systematically.
- The runner did not send the coercion follow-up for 124 of 277 October
  refusals. That is a refusal-detector gap of the same kind as the
  original grader defect.
