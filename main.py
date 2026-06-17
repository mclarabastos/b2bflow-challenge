from services.supabase_service import buscar_contatos


def main():
    contatos = buscar_contatos()

    print(f"\n{len(contatos)} contatos encontrados\n")

    for contato in contatos:
        print(
            f"{contato['nome']} - "
            f"{contato['telefone']}"
        )


if __name__ == "__main__":
    main()