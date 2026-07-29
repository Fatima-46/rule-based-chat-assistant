# InternGrow_RuleBasedAssistant

Intelligent Rule-Based Assistant built with Python and Streamlit.

[![Live App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://interngrowrulebasedassistant-6tr9py2ms3sm7fxznwk2hu.streamlit.app/)

**🔗 Live Demo:** [interngrowrulebasedassistant-6tr9py2ms3sm7fxznwk2hu.streamlit.app](https://interngrowrulebasedassistant-6tr9py2ms3sm7fxznwk2hu.streamlit.app/)

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
1. Push `app.py`, `requirements.txt`, and this `README.md` to a GitHub repo
2. Go to https://share.streamlit.io and sign in with GitHub
3. Click "New app", pick the repo, branch `main`, main file `app.py`
4. Click "Deploy" — you'll get a free public URL

## InternGrow Submission
- GitHub repo: `InternGrow_RuleBasedAssistant`
- Live app link: https://interngrowrulebasedassistant-6tr9py2ms3sm7fxznwk2hu.streamlit.app/
- Record a short video walking through the code + live app, post on LinkedIn tagging @InternGrow, and submit via the WhatsApp submission form
