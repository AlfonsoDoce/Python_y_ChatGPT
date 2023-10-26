##leccion12
import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def crear_contenido(tema, tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Por favor escribe un artículo corto sobre el tema: {tema}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura

    )
    return respuesta.choices[0].text.strip()

def resumir_texto(texto, tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Por favor resume el siguiente texto: {texto}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()

##esta es la instrucción para la primera función: crear contenido
#tema = input("Elije un tema para tu artículo: ")
#tokens = int(input("Cuantos tokens máximos tendrá tu artículo: "))
#temperatura = int(input("Del 1 al 10, qué tan creativo quieres que sea tu artículo: ")) / 10
#articulo_creado = crear_contenido(tema, tokens, temperatura)
#print(articulo_creado)

##esta es la instrucción para la segunda función: resumir texto
original = input("Pega aquí el artículo que quieres resumir (sin saltos de línea,archivo plano): ")
tokens = int(input("Cuantos tokens máximos tendrá tu resumen: "))
temperatura = int(input("Del 1 al 10, qué tan creativo quieres que sea tu resumen: ")) / 10
resumen = resumir_texto(original, tokens, temperatura)
print(resumen)