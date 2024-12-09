from ollama import chat
from pydantic import BaseModel, ValidationError


class Sentiment(BaseModel):
    classification: str  # positivo, negativo, neutro
    sentiment: str  # admiração, raiva, etc.


# Frase a ser classificada
phrase = "Achei que deu ruim mas deu bom"

# Prompt bem definido para o modelo
prompt = f"""
Classifique o sentimento da frase a seguir.

Frase: "{phrase}"

Devolva a resposta no formato JSON com os campos:
- "classification" (positivo, negativo ou neutro)
- "sentiment" (admiracao, raiva, etc.)

Exemplo:
{{
    "classification": "positivo",
    "sentiment": "admiracao"
}}
"""

try:
    # Envia o prompt para o modelo
    response = chat(
        messages=[{'role': 'user', 'content': prompt}],
        model='llama3.1',
        format=Sentiment.model_json_schema(),
        temperature=0.0
    )

    # Valida a resposta usando Pydantic
    sentiment = Sentiment.model_validate_json(response.message.content)
    print("Classificação:", sentiment.classification)
    print("Sentimento:", sentiment.sentiment)

except ValidationError as e:
    print("Erro de validação:", e)
except Exception as e:
    print("Erro ao classificar o sentimento:", e)
