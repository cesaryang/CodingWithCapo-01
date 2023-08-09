import os
import openai

openai.api_key = os.getenv("OPENAPI_KEY")

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Translate the following English text to French: 'Hello, World!'",
    max_tokens=60
)

print(response.choices[0].text)