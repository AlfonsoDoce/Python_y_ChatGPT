import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

modelo = "text-davinci-002"
prompt = "elija un buen nombre para un elefante"

respuesta = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=3,
    temperature=1,
    max_tokens=50
)

for idx, opcion in enumerate(respuesta.choices):
    texto_generado = opcion.text.strip()
    print(f"Respuesta {idx + 1}: {texto_generado}\n")