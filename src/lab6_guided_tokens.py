"""Lab 6 - guided example 6.1: whitespace vs word-like tokens.
Run: python src/lab6_guided_tokens.py
"""
import re


def main():
    for text in ["I can't submit CS4944 late!", "rasikh.ali@example.edu", "", "یہ ایک مثال ہے"]:
        whitespace = text.split()
        words = re.findall(r"\b\w+\b", text)
        print("Original:", repr(text))
        print("  Whitespace:", whitespace, len(whitespace))
        print("  Word-like:", words, len(words))


if __name__ == "__main__":
    main()
