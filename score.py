"""Compatibility entrypoint for the original PTE Read Aloud / Repeat Sentence baseline."""

from pte.score import *  # noqa: F401,F403 - preserve legacy import surface

if __name__ == "__main__":
    from pte.score import main
    raise SystemExit(main())
