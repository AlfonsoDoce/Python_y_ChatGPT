import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

modelo = "text-davinci-002"
prompt = "¿Cuál es la capital de Francia?"

respuesta = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=1,
)

texto_generado = respuesta.choices[0].text.strip()
print(texto_generado)



