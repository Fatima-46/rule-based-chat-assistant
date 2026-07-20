# InternGrow_RuleBasedAssistant

Intelligent Rule-Based Assistant built with Python and Streamlit.

## Features
- Conditional conversation bot with clean input processing (lowercasing, punctuation stripping)
- Pre-mapped responses for common intents: greetings, thanks, bot identity, jokes, help, etc.
- Upgrade: for unknown queries, scrapes a real-time summary from Wikipedia using `requests` + `BeautifulSoup`
- Simple chat-style interface with conversation history

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy live for free (Streamlit Community Cloud)
1. Create a GitHub repo named `InternGrow_RuleBasedAssistant`
2. Upload `app.py`, `requirements.txt`, and this `README.md` to the repo root
3. Go to https://share.streamlit.io and sign in with GitHub
4. Click "New app", pick this repo, branch `main`, main file `app.py`
5. Click "Deploy" — you'll get a free public URL

## InternGrow Submission
- GitHub repo: `InternGrow_RuleBasedAssistant`
- Live app link: (your Streamlit URL after deploying)
- Record a short video walking through the code + live app, post on LinkedIn tagging @InternGrow, and submit via the WhatsApp submission form
