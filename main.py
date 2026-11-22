#!/usr/bin/env python3
"""Something Spoke Once — make.fun curious-judge entry.

Writes one short text (1-280 Unicode code points) to ``entry.txt``.

The entry
--------
In 1977, a telescope in Ohio caught a 72-second signal from deep space.
It never repeated. The astronomer circled the printout in red pen and
wrote one word beside it: Wow! Nobody knows what sent it. Something
spoke once — and has been silent ever since.

The facts behind it
-------------------
This is the real 1977 "Wow! signal", recorded by the Big Ear radio
telescope at Ohio State University. Astronomer Jerry Ehman was reviewing
the computer printout when he found a strong narrowband signal that
looked like it came from deep space, circled it in red pen, and wrote
"Wow!" in the margin. The signal lasted 72 seconds, was never detected
again despite many searches, and its source remains unknown.

Why it fits the brief
--------------------
The judge rewards curiosity: a genuine open loop. This text is exactly
that — a true, specific, verifiable mystery, told calmly and concretely,
with no gimmick and no fake cliffhanger. The question it leaves behind
("what sent it?") is real, and the silence since 1977 is real too.

Contract
--------
The entry text is 254 Unicode code points, inside the required 1-280
range. The program is deterministic: every run writes identical bytes
(UTF-8, no trailing newline added beyond the text itself, no timestamps,
no randomness, no network access, standard library only).

Output location: ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when that variable is
set, otherwise ``/output/entry.txt``.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "In 1977, a telescope in Ohio caught a 72-second signal from deep "
    "space. It never repeated. The astronomer circled the printout in red "
    "pen and wrote one word beside it: Wow! Nobody knows what sent it. "
    "Something spoke once \u2014 and has been silent ever since."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    output_path = Path(output_dir) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
