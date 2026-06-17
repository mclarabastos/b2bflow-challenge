# B2bflow-challenge

Aplicação em Python que lê contatos armazenados no Supabase e envia mensagens personalizadas via WhatsApp usando a Z-API.

A mensagem enviada para cada contato é:

```
Olá, <nome_contato>! Tudo bem com você?
```

## Tecnologias

- Python 3.10
- Supabase
- Z-API
- requests
- python-dotenv

## Estrutura do projeto

```
b2bflow-challenge/
├── services/
│   ├── supabase_service.py
│   └── zapi_service.py
├── utils/
│   └── logger.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup da tabela no Supabase

Crie uma tabela chamada `contatos` com as seguintes colunas:

| Coluna   | Tipo   |
| -------- | ------ |
| id       | bigint |
| nome     | text   |
| telefone | text   |

Exemplo de insert:

```sql
INSERT INTO contatos (nome, telefone) VALUES
('Maria', '5521999999999'),
('João', '5521988888888');
```

O telefone deve estar no formato internacional sem espaços ou símbolos: `DDI + DDD + número`.

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

```env
SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE=
ZAPI_TOKEN=
ZAPI_CLIENT_TOKEN=
```

- `SUPABASE_URL` e `SUPABASE_KEY` estão disponíveis em Settings > API no painel do Supabase.
- `ZAPI_INSTANCE`, `ZAPI_TOKEN` e `ZAPI_CLIENT_TOKEN` estão disponíveis no painel da Z-API, na página da instância e em Segurança.

## Como instalar

```bash
git clone https://github.com/mclarabastos/b2bflow-challenge.git
cd b2bflow-challenge
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Como executar

```bash
python main.py
```

## Exemplo de saída

```
2026-06-17 13:33:12,122 | INFO | Iniciando envio
2026-06-17 13:33:13,119 | INFO | 3 contatos carregados
2026-06-17 13:33:13,119 | INFO | Enviando para Maria
2026-06-17 13:33:13,211 | INFO | Mensagem enviada com sucesso
2026-06-17 13:33:13,211 | INFO | Enviando para João
2026-06-17 13:33:13,293 | INFO | Mensagem enviada com sucesso
2026-06-17 13:33:13,293 | INFO | Enviando para Ana
2026-06-17 13:33:13,377 | INFO | Mensagem enviada com sucesso
2026-06-17 13:33:13,377 | INFO | Processo concluído
```

## Boas práticas aplicadas

- Credenciais isoladas em `.env`, fora do controle de versão
- Separação de responsabilidades entre serviços (`supabase_service`, `zapi_service`)
- Logs com timestamp para acompanhar o fluxo de execução
- Tratamento de erros com try/except em todas as chamadas externas
- Leitura limitada a 3 registros conforme especificação do desafio
