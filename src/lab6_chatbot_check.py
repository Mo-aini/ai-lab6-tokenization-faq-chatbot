"""Lab 6 - FAQ chatbot behaviour checks and a scripted transcript (TF-IDF backend).
Run: python src/lab6_chatbot_check.py
"""
try:
    from .lab6_chatbot import build_bot, reply, FAQ
except ImportError:                     # so it also runs as: python src/<file>.py
    from lab6_chatbot import build_bot, reply, FAQ


def main():
    engine = build_bot()
    assert "it_help.txt" in reply(engine, "How do I reset my password?")
    assert reply(engine, "") == "Please enter a question."
    assert "No matching FAQ" in reply(engine, "volcano geology")
    assert "Possible matches" in reply(engine, "password recovery")
    # the two added FAQs
    assert "printer_help" in reply(engine, "What should I do if the printer prints blank pages?")
    assert "it_password" in reply(engine, "How do I connect to campus Wi-Fi?")
    print("FAQ behaviour checks passed (", len(FAQ), "FAQs )\n")

    for query in ["How do I reset my password?",          # exact answer
                  "What should I do if the printer prints blank pages?",  # added FAQ, exact
                  "printer shows empty paper",            # suggestion response
                  "wifi not working",                     # no match: TF-IDF splits Wi-Fi into wi + fi
                  "",                                     # empty input
                  "volcano geology"]:                     # unsupported input
        print("You:", repr(query))
        print("Bot:", reply(engine, query))
        print()


if __name__ == "__main__":
    main()
