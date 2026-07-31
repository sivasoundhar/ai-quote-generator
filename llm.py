from groq import Groq

from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


def generate_quote(prompt, temperature, max_tokens):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return response.choices[0].message.content.strip()