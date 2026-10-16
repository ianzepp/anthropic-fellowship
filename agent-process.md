# Directing AI agents at scale: the Faber process

This page measures how the Faber language project is built. One
operator directs teams of AI agents through [Vivi](https://github.com/ianzepp/vivi),
a local mailspace for agents, using the [Tugboat](https://github.com/ianzepp/tugboat)
protocol. Tugboat separates the roles: an orchestrator (Mind),
implementers (Hands), planners, independent auditors, and advisory
"heads". Implementers do not audit their own work.

All numbers come from [`scripts/vivi_stats.py`](scripts/vivi_stats.py),
run read-only against the project's Vivi database on 2026-10-16. The raw
output is [`data/vivi-faberlang-2026-10-16.json`](data/vivi-faberlang-2026-10-16.json).
It contains counts only; no message content leaves the database.

## Scale

Window: 2026-07-09 to 2026-10-16, about 14 weeks.

| Measure | Count |
| --- | ---: |
| Messages between agents and the operator | 54,081 |
| Mailspace events (sends, reads, moves) | 123,300 |
| Work items, of which done | 6,258 / 4,713 |
| Work assignments to agents | 2,209 |
| Commits across the Faber repositories | 23,749 |

Most commits are in `radix`, the compiler monorepo (19,115). It is
private for now. The public Faber repositories are listed in
[`evidence.md`](evidence.md).

## Who talks

| Role | Messages | Share |
| --- | ---: | ---: |
| Mind (orchestrator) | 23,216 | 43% |
| Hands (implementers) | 15,850 | 29% |
| Operator (Ian Zepp) | 2,871 | 5% |
| Auditors | 2,676 | 5% |
| Merge lane | 2,126 | 4% |
| Planners | 2,070 | 4% |
| Head-CTO (correctness review) | 1,058 | 2% |
| Other roles (reviewers, hunters, lint, triage, docs, heads) | 4,214 | 8% |

The operator writes about one message in twenty. That is direction,
not implementation: goals, campaigns, rulings on disputed questions,
and corrections when the process drifts.

## What independent review catches

Auditors are separate agents from the implementers. They review
delivered work against its specification and the live repository, and
file a verdict. Since 2026-09-18 the operator's rule has been to run
each audit verdict as a pair of models from two different families,
with a third agent synthesizing the two reports.

| Verdict | Reports | Share |
| --- | ---: | ---: |
| Clean pass | 118 | 18% |
| Admitted as delivered | 101 | 15% |
| Admitted with residual issues recorded | 260 | 40% |
| Sent back for revision | 79 | 12% |
| Blocked from shipping | 68 | 10% |
| Other (inventories, re-audits) | 32 | 5% |
| **Total** | **658** | |

About one audit in five turned work back. Two in five passed only with
recorded defects that became follow-up work. Fewer than one in five
found nothing.

## What these numbers do and don't show

- **They show** that AI-written code regularly fails independent
  review, and that the process is built to catch it. The review layer,
  not the model, is what makes the output trustworthy.
- **They don't show** a comparison with human-written code. There is no
  human baseline in this data.
- Rework mostly goes out as new tasks, not as retries of the same item:
  only 13 of 2,194 work items have more than one assignment. The audit
  verdicts are the better measure of rework.

## Reproducing

```bash
python3 -I scripts/vivi_stats.py ~/work/faberlang/.vivi/mail.sqlite --repos ~/work/faberlang/radix ~/work/faberlang/faber
```

The database is private; the script and its output are public.
