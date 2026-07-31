from prompts import build_prompt


def test_prompt_returns_string():

    prompt = build_prompt("AI")

    assert isinstance(prompt, str)


def test_prompt_contains_category():

    prompt = build_prompt("Programming")

    assert "Programming" in prompt


def test_prompt_not_empty():

    prompt = build_prompt("Life")

    assert len(prompt) > 0