##leccion13
import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def clasificar_texto(texto):
    categorias = [
        "arte",
        "ciencia",
        "economía",
        "educación",
        "entretenimiento",

    ]
    prompt = f"Por favor clasifica el siguiente texto '{texto}' en una de estas categorías: {','.join(categorias)}. La categoría es: "
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        max_tokens=50,
        temperature=0.5
    )
    return respuesta.choices[0].text.strip()

texto_para_clasificar = input("Ingrese un texto: ")
clasificacion = clasificar_texto(texto_para_clasificar)
print(clasificacion)



