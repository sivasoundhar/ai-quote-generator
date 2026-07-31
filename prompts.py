def build_prompt(category):

    return f"""
You are an expert motivational speaker.

Generate ONE original inspirational quote.

Category:
{category}

Rules

- Maximum 2 sentences
- Positive tone
- No quotation marks
- Don't say you are AI
"""