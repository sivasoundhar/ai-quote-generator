SYSTEM_PROMPT = """
You are a professional AI quote writer.

Rules:

- Generate ONLY one quote.
- Keep it under 40 words.
- Make it original.
- Do not use emojis.
- Do not explain the quote.
- Do not use bullet points.
- Return only the quote.
"""


def build_prompt(
    category: str,
    language: str,
    style: str,
):

    return f"""
Generate one {style} quote.

Category:
{category}

Language:
{language}

Requirements:

- Maximum 40 words
- Inspiring
- Natural
- Easy to understand
- Return only the quote
"""