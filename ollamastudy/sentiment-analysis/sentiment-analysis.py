import json
from ollama import chat
from pydantic import BaseModel


class Sentiment(BaseModel):
    classification: str
    sentiment: str


phrase = "O jogo foi bom, mas o árbitro estava péssimo."

response = chat(
    messages=[
        {'role': 'user', 'content': f"Classifique o sentimento da frase: {phrase}. Responda no formato JSON com as chaves 'classification' e 'sentiment'."}
    ],
    model='llama3.2',
    format="json"
)

content_str = response["message"]["content"]
content = json.loads(content_str)

sentiment = Sentiment.model_validate(content)
print(sentiment)
