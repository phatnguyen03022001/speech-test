# Speech Test

**Experimental English Speaking assessment research laboratory** for comparing speech recognition, pronunciation assessment, phoneme alignment, mispronunciation detection, fluency, prosody, content accuracy and score calibration methods. Exam domains: **PTE Speaking, IELTS Speaking and TOEIC Speaking**. Existing implementations and research results are predominantly PTE-focused; IELTS and TOEIC scoring are not implemented.

## Repository ownership

| Path | Responsibility |
| --- | --- |
| `shared/` | Exam-independent evaluation statistics and process-safety utilities used by current research; further reuse requires evidence |
| `pte/` | PTE Read Aloud / Repeat Sentence baseline and PTE research tools |
| `ielts/` | Reserved for future IELTS Speaking methodology experiments |
| `toeic/` | Reserved for future TOEIC Speaking methodology experiments |
| `tests/` | Existing regression and import contracts |
| `results/` | Immutable historical research findings, protocols and references |
| `.local/datasets/shared/` | Ignored, general-purpose speech corpora |
| `.local/datasets/pte/` | Ignored, PTE-specific datasets |
| `.local/datasets/ielts/`, `.local/datasets/toeic/` | Ignored, empty future exam-specific data locations |
| `.local/research/` | Ignored, private research artifacts and integrity receipts |

Several root-level PTE research scripts remain at root because relocating them would change existing path resolution, frozen script hashes or supported CLI contracts. Compatibility entrypoints for the moved scripts remain at root. Existing research benchmark artifacts and scientific conclusions are **not** rewritten.

## Scientific boundaries

- This is **not** a production scoring service. Research results are not production-readiness evidence.
- Trustworthy pronunciation assessment requires suitable independent **human-rated ground truth**; algorithm outputs alone are insufficient.
- **Pearson agreement is unverified** without independent Pearson-scored responses. No Pearson, IELTS or TOEIC scoring equivalence is claimed.
- Individual datasets keep their original licenses, access conditions and redistribution restrictions. Restricted raw data and per-record predictions must remain local and must not be committed.
- Existing scorers, thresholds, checkpoints and benchmark denominators are unchanged by the repository migration.

## Running regression tests

Python 3.14 and repository-declared `uv` version are required. Install/sync using the committed `uv.lock`, not global package mutations.

```sh
uv sync --locked
.venv/bin/python -m unittest discover -s tests -q
.venv/bin/python score.py --help
.venv/bin/python benchmark_evaluation.py --help
.venv/bin/python task_07_5_asr.py verify
```

The existing root entrypoints remain supported; experimental methods must not be described as official exam scoring. Local dataset compatibility symlinks preserve historical relative paths required by current scripts/manifests without duplicating corpus bytes.
