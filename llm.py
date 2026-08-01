from groq import Groq

from config import GROQ_API_KEY, MODEL_NAME
from constants import DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE
from prompts import SYSTEM_PROMPT, build_prompt

client = Groq(api_key=GROQ_API_KEY)


def generate_quote(
    category: str,
    language: str = "English",
    style: str = "Inspirational",
    temperature: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS,
) -> str:
    """Generate a single quote using the Groq API.

    Args:
        category: Quote category (e.g. "Motivation").
        language: Quote language (e.g. "English", "தமிழ்").
        style: Quote style (e.g. "Inspirational", "Funny").
        temperature: Creativity (0.0 - 1.0).
        max_tokens: Maximum number of tokens for the response.

    Returns:
        The generated quote as a plain string.
    """
    if not GROQ_API_KEY:
        raise RuntimeError(
            "GROQ_API_KEY is missing. "
            "Copy .env.example to .env and add your Groq API key."
        )

    prompt = build_prompt(category, language, style)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return response.choices[0].message.content.strip()
