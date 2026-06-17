import os
import requests
from dotenv import load_dotenv

load_dotenv()

INSTANCE = os.getenv("ZAPI_INSTANCE")
TOKEN = os.getenv("ZAPI_TOKEN")
CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")


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
            f"Olá, {nome} tudo bem com você?"
        )
    }

    headers = {
        "Client-Token": CLIENT_TOKEN
    }

    try:

        resposta = requests.post(
            url,
            json=payload,
            headers=headers,
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