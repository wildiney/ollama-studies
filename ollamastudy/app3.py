from ollama import chat
from pydantic import BaseModel


class Sentiment(BaseModel):
    classification: str
    sentiment: str


phrase = "Achei que deu ruim mas deu bom"

response = chat(
    messages=[
        {'role': 'user', 'content': "Classifique o sentimento da frase: ${phrase}"}
    ],
    model='llama3.1',
    format=Sentiment.model_json_schema()
)

sentiment = Sentiment.model_validate_json(response.message.content)
print(sentiment)
