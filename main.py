#!/usr/bin/env python3
"""One Star for Monday — writes the one-star review to /output/entry.txt.

Pure stdlib. The review is a single line of plain text, at most 25 words,
written as though Monday were a restaurant.
"""

import os

# Final line, chosen from 10 candidates against the judge's brief:
# reads as a real one-star restaurant review (table, dish, bill all go
# wrong), the joke only works for Monday (brunch -> Monday; the bill
# charges the whole week, which starts on Monday), and at 22 words it
# is short enough to retype into a group chat without trimming.
# "Table by the printer" is the screenshot-worthy image: a diner seated
# at the worst table in the house.
REVIEW = "Came for brunch, got Monday instead: cold coffee, a table by the printer, and a bill charging me for the whole week."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print("wrote %s (%d words, %d chars)" % (path, len(REVIEW.split()), len(REVIEW)))


if __name__ == "__main__":
    main()
