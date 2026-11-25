"""Describe Your Ex in One Word.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt: the
one-word verdict on a former partner. The ex was recalled, like a
defective product pulled off the shelves. Standard library only.
"""

import os

WORD = "Recalled"


def check_word(text):
    """Check the word against the competition gate before writing.

    The gate needs plain UTF-8 text of 1 to 111 characters, not
    only white space, in a single word: one word describing an ex,
    and nothing attached. Returns the cleaned text or raises
    ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("word must not be only whitespace")
    if len(cleaned) > 111:
        raise ValueError(
            "word is %d characters, over the 111 limit" % len(cleaned)
        )
    if len(cleaned.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return cleaned


def word_shape(text):
    """Measure the word for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A word padded with a second word, or one so
    long it reads like a sentence instead of a verdict, is caught
    here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_word(WORD)
    shape = word_shape(text)
    if shape["words"] != 1:
        raise ValueError("entry must be exactly one word")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
