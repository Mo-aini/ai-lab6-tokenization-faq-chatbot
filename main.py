# Lab 6 - runs the tokenization experiment and the FAQ chatbot checks
import platform
import sys

from src import lab6_chatbot_check, lab6_guided_tokens, lab6_search, lab6_tokens


def section(title):
    print("=" * 72)
    print(title)
    print("=" * 72)


def main():
    use_model = "--no-model" not in sys.argv
    print("AI Lab 6: Tokenization & FAQ Chatbot | Rasikh Ali (42365)")
    print("Python %s, %s" % (platform.python_version(),
                             "with all-MiniLM-L6-v2 on CPU" if use_model else "TF-IDF only (--no-model)"))
    print()
    section("LAB 6 / 6.1  Guided example: whitespace vs word-like tokens")
    lab6_guided_tokens.main()
    print()
    section("LAB 6 / Task  Token comparison on tricky inputs")
    lab6_tokens.main(use_model=use_model)
    print()
    section("LAB 6 / 6.5  Retriever demo (TF-IDF)")
    lab6_search.main()
    print()
    section("LAB 6 / 6.6  FAQ chatbot checks and scripted transcript")
    lab6_chatbot_check.main()


if __name__ == "__main__":
    main()
