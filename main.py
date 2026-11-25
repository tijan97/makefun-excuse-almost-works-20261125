#!/usr/bin/env python3
"""make.fun entry: The Excuse That Almost Works.

Writes a single one-line excuse -- the text a gamer sends their boss to
skip work during GTA 6 launch week -- to /output/entry.txt.

The excuse is deliberately mundane: a flooded kitchen and a plumber who
can only come tomorrow morning. A tired manager has heard every wild
story twice; a boring, specific, slightly embarrassing household mishap
with a narrow appointment window is the one that almost gets believed.
"""

import os

EXCUSE = (
    "Sorry, the washing machine flooded the kitchen and the landlord's "
    "plumber can only come tomorrow between 8 and 1."
)


def main() -> None:
    output_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
