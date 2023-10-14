import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

modelo = "text-davinci-002"
prompt = "¿De qué se trata la pelicula El Padrino II?"

respuesta = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=1,
    temperature=1,
    max_tokens=100
)

texto_generado = respuesta.choices[0].text.strip()
print(texto_generado)
