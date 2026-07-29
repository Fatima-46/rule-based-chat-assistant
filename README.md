# Rule-Based Chat Assistant

A conversational assistant built in Python with a Streamlit UI. It matches user
messages against a set of predefined rules, and falls back to a live Wikipedia
lookup when nothing matches — so it can hold a basic conversation *and* answer
general knowledge questions.

**Live demo:** <ADD-YOUR-STREAMLIT-LINK-HERE>

![screenshot](docs/screenshot.png)

## How it works

1. The user's message is cleaned (lowercased, punctuation stripped).
2. It's checked against a table of rules (`RULES`), each mapping a set of
   keywords to a canned response, using word-boundary matching so short
   keywords like `"hi"` don't accidentally match inside unrelated words.
3. If no rule matches, the app queries the
   [Wikipedia REST summary API](https://en.wikipedia.org/api/rest_v1/page/summary/)
   for the user's message and returns the summary (with a link to the full
   article) instead of a dead end.
4. Streamlit renders the chat interface and keeps message history in session
   state.

## Tech stack

- Python 3
- Streamlit — UI
- Requests — Wikipedia REST API calls
- Pytest — unit tests

## Project structure
.
├── app.py # main Streamlit app: rules, matching, Wikipedia fallback
├── test_app.py # unit tests for the matching logic
├── requirements.txt
└── README.md
## Key concepts to know before reading the code

- **Rule-based NLP matching** — how keyword/intent tables work before you get
  to ML-based intent classification.
- **Word-boundary vs. substring matching** — why `"hi" in "this is weird"`
  is a bug, not a feature.
- **Consuming a REST API** — sending a GET request, checking the status code,
  parsing JSON, handling network failures gracefully.
- **Streamlit session state** — how the chat history persists across reruns
  without a database.

## Running locally

```bash
git clone https://github.com/Fatima-46/rule-based-chat-assistant.git
cd rule-based-chat-assistant
pip install -r requirements.txt
streamlit run app.py
```

## Running tests

```bash
pytest
```

## Possible extensions

- Swap the rule table for an intent classifier (e.g. scikit-learn or a small
  transformer) to compare rule-based vs. ML-based matching.
- Add conversation memory so follow-up questions use prior context.
- Deploy behind a simple FastAPI backend instead of only Streamlit.

## License

MIT — see [LICENSE](LICENSE).
