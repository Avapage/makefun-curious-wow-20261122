"""Something Spoke Once — make.fun entry for make-the-ai-judge-feel-curious-20261122-2311.

The entry is a single short text (1-280 Unicode code points) written to
``entry.txt``. It is built to make an AI judge feel curious: a genuine open
loop grounded in a real, specific, verifiable mystery.

The facts: in 1977 the Big Ear radio telescope at Ohio State University
caught a powerful 72-second narrowband signal from deep space. It never
repeated, despite many follow-up searches. Astronomer Jerry Ehman, reviewing
the computer printout, circled the signal's intensity values in red pen and
wrote one word beside them: "Wow!" No natural or human-made source has ever
been confirmed. Something spoke once — and has been silent ever since.

Contract (from the competition kit): the program must write exactly ONE
short text to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (or ``/output/entry.txt``
when that variable is unset), and the text must be 1-280 Unicode code
points long. This entry is 254 code points.

Standard library only, no network, deterministic: every run writes the
same bytes.
"""

import os
import sys

ENTRY_TEXT = (
    "In 1977, a telescope in Ohio caught a 72-second signal from deep space. "
    "It never repeated. The astronomer circled the printout in red pen and "
    "wrote one word beside it: Wow! Nobody knows what sent it. "
    "Something spoke once \u2014 and has been silent ever since."
)

MIN_CODE_POINTS = 1
MAX_CODE_POINTS = 280


def main() -> int:
    n = len(ENTRY_TEXT)
    if not (MIN_CODE_POINTS <= n <= MAX_CODE_POINTS):
        print(
            f"error: entry text is {n} code points, "
            f"must be {MIN_CODE_POINTS}-{MAX_CODE_POINTS}",
            file=sys.stderr,
        )
        return 1
    if not ENTRY_TEXT.strip():
        print("error: entry text is empty or only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
