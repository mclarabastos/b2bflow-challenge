from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)


def buscar_contatos():
    resposta = (
        supabase
        .table("contatos")
        .select("*")
        .limit(3)
        .execute()
    )

    return resposta.data