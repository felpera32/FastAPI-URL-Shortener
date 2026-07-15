# FastAPI URL Shortener 

Um encurtador de URLs desenvolvido em Python utilizando FastAPI e PostgreSQL.

O projeto permite transformar URLs longas em links menores através da geração de códigos únicos, armazenando os dados no banco e realizando o redirecionamento para o endereço original.

## Tecnologias

- Python
- FastAPI
- PostgreSQL
- Uvicorn

## Funcionalidades

- Criar links encurtados
- Gerar códigos únicos para URLs
- Armazenar URLs no PostgreSQL
- Redirecionar usuários através do código gerado
- Definir tempo de expiração dos links

## Estrutura

```text
App/
├── Connection/   # Conexão com banco de dados
├── Database/     # Operações relacionadas ao banco
├── Generator/    # Geração dos códigos dos links
├── Routes/       # Rotas da API
├── Server/       # Configuração do servidor FastAPI
├── Service/      # Regras de negócio
└── Validators/   # Validação de dados

main.py           # Inicialização da aplicação
```

## Executando

Clone o projeto:

```bash
git clone https://github.com/felpera32/LinkForge.git
cd LinkForge
```

Crie o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure o banco PostgreSQL e as variáveis necessárias.

Execute:

```bash
uvicorn main:app --reload
```

A documentação da API estará disponível em:

```
http://127.0.0.1:8000/docs
```