from app import clean_input, match_rule


def test_clean_input_strips_punctuation():
    assert clean_input("Hello, World!") == "hello world"


def test_match_rule_greeting():
    assert "Hello" in match_rule("hi there")


def test_match_rule_unknown_returns_none():
    assert match_rule("quantum entanglement") is None
