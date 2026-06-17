from services.supabase_service import buscar_contatos
from services.zapi_service import enviar_mensagem
from utils.logger import logger


def main():

    logger.info("Iniciando envio")

    try:

        contatos = buscar_contatos()

        if not contatos:
            logger.warning(
                "Nenhum contato encontrado"
            )
            return

        logger.info(
            f"{len(contatos)} contatos carregados"
        )

        for contato in contatos:

            nome = contato["nome"]
            telefone = contato["telefone"]

            logger.info(
                f"Enviando para {nome}"
            )

            status, resposta = enviar_mensagem(
                nome,
                telefone
            )

            if (
                status == 200
                and "error" not in resposta.lower()
            ):

                logger.info(
                    "Mensagem enviada com sucesso"
                )

            else:

                logger.error(
                    (
                        f"Falha ao enviar para "
                        f"{nome} | "
                        f"status={status} | "
                        f"resposta={resposta}"
                    )
                )

    except Exception as erro:

        logger.exception(
            f"Erro na execução: {erro}"
        )

    logger.info(
        "Processo concluído"
    )


if __name__ == "__main__":
    main()