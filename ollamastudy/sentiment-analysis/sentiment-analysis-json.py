from ollama import chat
from pydantic import BaseModel, ValidationError


class Sentiment(BaseModel):
    classification: str
    sentiment: str


phrase = "Achei que deu ruim mas deu bom"

prompt = f"""
Classifique o sentimento da frase a seguir.

Frase: "{phrase}"

Devolva a resposta no formato JSON com os campos:
- "classification" (positivo, negativo ou neutro)
- "sentiment" (admiração, raiva, etc.)

Exemplo:
{{
    "classification": "positivo",
    "sentiment": "admiração"
}}
"""

try:
    response = chat(
        messages=[{'role': 'user', 'content': prompt}],
        model='llama3.2',
        format=Sentiment.model_json_schema()
    )

    sentiment = Sentiment.model_validate_json(response.message.content)
    print("Classificação:", sentiment.classification)
    print("Sentimento:", sentiment.sentiment)

except ValidationError as e:
    print("Erro de validação:", e)
except Exception as e:
    print("Erro ao classificar o sentimento:", e)
