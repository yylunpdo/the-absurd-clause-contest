#!/usr/bin/env python3
"""The Absurd Clause Contest — entry program (Python stdlib only).

Writes a single original English sentence, phrased as a clause buried
deep inside a terms-of-service agreement: deadpan legal boilerplate
that quietly turns absurd. The text is at most 200 characters.
"""

import os

CLAUSE = (
    "By accepting these terms, you grant us a perpetual, irrevocable "
    "licence to your soul, including any souls you acquire later, which "
    "we may sublicense to our affiliates, subsidiaries, and the Moon."
)


def main():
    text = CLAUSE.strip()
    assert 1 <= len(text) <= 200, "clause must be 1-200 characters, got %d" % len(text)
    assert "\n" not in text, "clause must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
