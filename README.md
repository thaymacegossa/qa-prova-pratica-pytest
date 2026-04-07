# prova-pratica
Questão prática da primeira prova de QA


## Uso com Docker Compose

Pre-requisito: Docker e Docker Compose instalados.

1. Na raiz do projeto, construa a imagem:

```bash
   # Build só da aplicação (target app)
   docker compose build app

   # Build só dos testes (target tests)
   docker compose build tests
```

2. Roda a aplicacao no terminal:

```bash
   # Rodar app
   docker compose run --rm app

   # Rodar suíte completa de testes (serviço tests)
   docker compose --profile test run --rm tests

   # Ver logs do app
   docker compose logs -f app
```