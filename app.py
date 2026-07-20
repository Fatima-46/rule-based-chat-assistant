"""
InternGrow Python Programming Track - Task 4
Intelligent Rule-Based Assistant (Web App - Streamlit)

Features:
- Conditional conversation bot with clean input processing
- Pre-mapped responses for common intents (greetings, thanks, bot info, etc.)
- Upgrade: for unknown queries, scrapes a real-time Wikipedia summary
  using requests + BeautifulSoup
"""

import re
import requests
from bs4 import BeautifulSoup
import streamlit as st

# ----------------------------
# Rule-based response mapping
# ----------------------------
# Each entry: (list of trigger keywords/patterns, response)
RULES = [
    (["hello", "hi", "hey"], "Hello! I'm your rule-based assistant. Ask me anything."),
    (["how are you"], "I'm just code, but I'm running smoothly! How can I help you?"),
    (["your name", "who are you"], "I'm a simple rule-based chatbot built for the InternGrow internship."),
    (["thank", "thanks"], "You're welcome! Happy to help."),
    (["bye", "goodbye", "exit", "quit"], "Goodbye! Have a great day."),
    (["help"], "You can greet me, ask who I am, or ask about any topic — "
                "if I don't have a rule for it, I'll look it up on Wikipedia for you."),
    (["time"], "I don't have access to a live clock, but your device can show you the current time."),
    (["joke"], "Why do programmers prefer dark mode? Because light attracts bugs!"),
]


def clean_input(text):
    """Lowercase and strip punctuation for reliable matching."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)
    return text


def match_rule(user_input):
    """Check the cleaned input against known rule keywords."""
    cleaned = clean_input(user_input)
    for keywords, response in RULES:
        for keyword in keywords:
            if keyword in cleaned:
                return response
    return None


def scrape_wikipedia_summary(query):
    """
    Upgrade feature: for queries with no matching rule, fetch a short
    real-time summary from Wikipedia using requests + BeautifulSoup.
    """
    try:
        search_url = "https://en.wikipedia.org/w/index.php"
        params = {"search": query, "title": "Special:Search", "fulltext": "1"}
        headers = {"User-Agent": "Mozilla/5.0 (InternGrow-RuleBasedAssistant)"}

        response = requests.get(search_url, params=params, headers=headers, timeout=8)
        response.raise_for_status()

        # If Wikipedia redirected straight to an article page, use it directly.
        # Otherwise, grab the first search result link.
        soup = BeautifulSoup(response.text, "html.parser")

        if "Special:Search" in response.url:
            first_result = soup.select_one("div.mw-search-result-heading a")
            if not first_result:
                return None
            article_url = "https://en.wikipedia.org" + first_result["href"]
        else:
            article_url = response.url

        article_response = requests.get(article_url, headers=headers, timeout=8)
        article_soup = BeautifulSoup(article_response.text, "html.parser")

        paragraphs = article_soup.select("#mw-content-text p")
        for p in paragraphs:
            text = p.get_text().strip()
            if text and len(text) > 60:
                # Trim to a short summary (first 2-3 sentences)
                sentences = re.split(r"(?<=[.!?])\s+", text)
                summary = " ".join(sentences[:3])
                return summary, article_url

        return None
    except requests.RequestException:
        return None


# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Rule-Based Assistant", page_icon="🤖")
st.title("🤖 Intelligent Rule-Based Assistant")
st.caption("InternGrow Python Programming Track — Task 4")

st.write(
    "Try greetings like *hello*, *how are you*, *your name*, *joke*, or *help*. "
    "Ask about anything else (e.g. *Albert Einstein*, *Python programming language*) "
    "and I'll look it up on Wikipedia."
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="user_input")

if st.button("Send") and user_input.strip():
    rule_response = match_rule(user_input)

    if rule_response:
        bot_response = rule_response
    else:
        with st.spinner("Looking that up on Wikipedia..."):
            result = scrape_wikipedia_summary(user_input)
        if result:
            summary, url = result
            bot_response = f"{summary}\n\n(Source: {url})"
        else:
            bot_response = "Sorry, I couldn't find a rule or a Wikipedia match for that. Try rephrasing?"

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Assistant", bot_response))

st.divider()

# Display conversation history (most recent at top)
for speaker, message in reversed(st.session_state.chat_history):
    if speaker == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Assistant:** {message}")

if st.button("Clear conversation"):
    st.session_state.chat_history = []
    st.rerun()
