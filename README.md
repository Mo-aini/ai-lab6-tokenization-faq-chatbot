# AI Lab 6 - Tokenization and FAQ Chatbot

Lab 6 for the AI lab course (CAI601400), NLP fundamentals part 1. I compare whitespace tokens, a Unicode word-like regex and the sub-word tokens of a real encoder on tricky inputs, then build a small command line FAQ chatbot that answers only exact questions and offers suggestions (TF-IDF or sentence embeddings) for everything else.

## Files

- `main.py` runs everything that does not need typing
- `src/lab6_guided_tokens.py` guided example 6.1, whitespace vs word-like tokens
- `src/lab6_tokens.py` the token comparison on 8 inputs (punctuation, `can't` with a straight and a curly apostrophe, an email, `CS4944 version 2.1`, an empty string, Urdu text, a file name) plus the all-MiniLM-L6-v2 WordPiece tokens
- `src/lab6_search.py` the `Retriever` class from the manual (`tfidf` and `embedding` backends)
- `src/lab6_chatbot.py` the interactive FAQ chatbot (5 FAQs, 2 of them added by me)
- `src/lab6_chatbot_check.py` behaviour checks (exact match, empty input, off-topic, suggestions) and a scripted transcript
- `outputs/output.txt` output of `main.py` on my machine
- `outputs/chatbot_transcript_tfidf.txt`, `outputs/chatbot_transcript_embedding.txt` two chatbot sessions
- `report/` the written report (DOCX and PDF). Labs 6, 7 and 8 were written up in one report; this lab is section 2

## How to run

Python 3.10+ is needed. The embedding parts download `sentence-transformers/all-MiniLM-L6-v2` (about 90 MB) the first time and run on CPU.

```
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py                   # add --no-model to skip the encoder tokenizer
```

The chatbot is interactive:

```
python src/lab6_chatbot.py                      # TF-IDF
python src/lab6_chatbot.py --backend embedding  # sentence embeddings
```

Type `exit` to stop.

## Results

| Input | Whitespace | Word-like | Model sub-words |
|-------|------------|-----------|-----------------|
| `AI, search!` | 2 | 2 | 4 |
| `I can't log in.` | 4 | 5 | 7 |
| `help@example.com` | 1 | 3 | 5 |
| `CS4944 version 2.1` | 3 | 4 | 7 |
| `یہ ایک مثال ہے` (Urdu) | 4 | 4 | 11 |

Whitespace keeps punctuation glued to words, the regex breaks `can't` into `can` + `t` and destroys the email, and the encoder splits rare strings like `CS4944` into `cs ##49 ##44`. Urdu has the same word count with spaces but needs 11 sub-word pieces.

FAQ chatbot (TF-IDF): an exact question gets the answer with its source, `printer shows empty paper` gets the blank-pages FAQ as a suggestion (similarity 0.238), and `wifi not working` and `volcano geology` fall back to the help desk. With TF-IDF `wifi` does not match `Wi-Fi` because the hyphen splits it into `wi` and `fi`. The embedding backend puts the Wi-Fi FAQ first for that question (0.345), but it also suggests something for `volcano geology` because there is no score threshold.

## Author

Rasikh Ali (42365)

MIT License, see LICENSE.
