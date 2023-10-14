import os
import spacy
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

modelo = "text-davinci-002"
prompt = "Cuenta una historia breve sobre un viaje a un pais europeo"

respuesta = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=1,
    max_tokens=100
)

texto_generado = respuesta.choices[0].text.strip()
print(texto_generado)

print("***")

modelo_spacy = spacy.load("es_core_news_md")
analisis = modelo_spacy(texto_generado)

##for token in analisis:
  ##  print(yoken.text, token.pos_)

##for ent in analisis.ents:
  ##  print(ent.text, ent.label_)

ubicacion = None

for ent in analisis.ents:
    if ent.label_ == "LOC":
        ubicacion = ent
        break
if ubicacion:
    prompt2 = f"Dime más acerca de {ubicacion}"
    respuesta2 = openai.Completion.create(
        engine=modelo,
        prompt=prompt2,
        n=1,
        max_tokens=100
    )
    print(respuesta2.choices[0].text.strip())
