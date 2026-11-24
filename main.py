"""Real-Life Patch Notes: The Comedy Changelog.

One-line patch note for a bug in real life, written to /output/entry.txt.
The note must be 1-160 characters of UTF-8 text, in the terse register
of a real software release note.
"""

import os

PATCH_NOTE = (
    # The joke: the body's internal clock is a scheduler that wakes you
    # early for no reason, then naps through the one moment it matters.
    "v2.7.1: fixed a bug where the body woke up ten minutes before "
    "the alarm, then fell asleep again two minutes before it rang."
)

MAX_CHARS = 160


def main() -> None:
    note = PATCH_NOTE.strip()
    if not note:
        raise SystemExit("patch note is empty")
    if len(note) > MAX_CHARS:
        raise SystemExit(f"patch note is {len(note)} chars, over the 160 limit")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(note + "\n")
    print(f"wrote {len(note)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
