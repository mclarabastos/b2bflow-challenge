import os
import requests
from dotenv import load_dotenv

load_dotenv()

INSTANCE = os.getenv("ZAPI_INSTANCE")
TOKEN = os.getenv("ZAPI_TOKEN")


def enviar_mensagem(nome, telefone):

    url = (
        f"https://api.z-api.io/"
        f"instances/{INSTANCE}"
        f"/token/{TOKEN}"
        f"/send-text"
    )

    payload = {
        "phone": telefone,
        "message": (
            f"Olá, {nome}! Tudo bem com você?"
        )
    }

    try:

        resposta = requests.post(
            url,
            json=payload,
            timeout=10
        )

        return (
            resposta.status_code,
            resposta.text
        )

    except requests.RequestException as erro:

        return (
            500,
            str(erro)
        )