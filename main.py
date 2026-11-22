#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Something spoke once — a short text about the Wow! signal.

Writes one text to /output/entry.txt: a genuine open loop grounded in
true facts. In 1977 the Big Ear radio telescope at Ohio State
University caught a 72-second narrowband signal from deep space;
astronomer Jerry Ehman circled the printout in red pen and wrote
"Wow!" beside it. The signal never repeated, and no one knows what
sent it. Standard library only, no network, deterministic: every run
writes the same bytes.

Output contract: UTF-8 text of 1 to 280 Unicode code points, not only
white space. The text below is 254 code points, so it fits with room
to spare and no truncation is ever applied.
"""

import os
from pathlib import Path

TEXT = (
    "In 1977, a telescope in Ohio caught a 72-second signal from deep "
    "space. It never repeated. The astronomer circled the printout in "
    "red pen and wrote one word beside it: Wow! Nobody knows what sent "
    "it. Something spoke once \u2014 and has been silent ever since."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
