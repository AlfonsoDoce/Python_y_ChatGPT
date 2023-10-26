##leccion15
import openai
import os
import spacy
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

preguntas_anteriores = []
respuestas_anteriores = []


def filtras_lista_negra(texto, lista_negra):
    token = modelo_spacy(texto)
    resultado = []

    for t in token:
        if t.token.lowe() not in lista_negra
            resultado.append(t.texto)
        else:
            resultado.append("[xxx]")
    return " ".join(resultado)

def preguntar_chat_gpt(prompt, modelo="text-davinci_002"):
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=150,
        temperature=1.5
    )
    respuesta_sin_controlar = respuesta.choices[0].text.strip()
    respuesta_controlada = filtrar_lista_negrarespuesta_sin_controlar, palabras_prohibidas)
    return respuesta_controlada


print("Bienvenido a nuestro chatbot básico. Escribe 'salir' cuando quieras terminar")

while True:
    ingreso_usuario = input("\nTu:")
    if ingreso_usuario.lower() == "salir":
        break

    prompt = f"El usuario pregunta: {ingreso_usuario}\nChatGPT responde:"
    respuesta_gpt = preguntar_chat_gpt(prompt)
    print(f"Chatbot: {respuesta_gpt}")
