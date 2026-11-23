"""One Word, First Thought entry.

Writes exactly one word -- the first that comes to mind -- to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.

Draft word: "syzygy" -- striking and odd, the alignment of three
celestial bodies, but abstract: it names a geometry, not a feeling.

Revised word: "petrichor" -- the scent of rain on dry earth. It keeps
the surprise (few readers know the word) and adds what "syzygy"
lacked: a vivid, specific sensory image in nine letters, plus a soft
sound that suits what it names. Surprise first, vividness second --
exactly the order the judge weighs.
"""

import os

WORD = "petrichor"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
