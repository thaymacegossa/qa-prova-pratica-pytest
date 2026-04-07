# Prova Prática
**`Projeto de testes automatizados desenvolvido para prova de disciplina de Qualidade de Software`**

---

### 🤖 Tecnologias utilizadas:

- Python, agiliza a escrita de scripts de automação e o desenvolvimento do back-end;
- Unittest, oferece uma estrutura sólida e padronizada para a criação de testes unitários;
- Docker, garante que a aplicação e os testes rodem exatamente da mesma forma em qualquer computador, eliminando conflitos de ambiente;
- Git, gerenciamento das versões do código.

---

### 🛠️ Como Executar a Aplicação

Uso com Docker Compose
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
```

---

### Regras de Negócio Testadas
- O projeto deve gerenciar um inventário de produtos em um dataset.
- Cada produto é representado por nome, preço e quantidade.
- Deve ser possível cadastrar um produto, atualizar a quantidade de um produto existente e remover um produto pelo nome.

---

### Cobertura de Testes
1. Cobertura por arquivo

   <img width="750" height="384" alt="image" src="https://github.com/user-attachments/assets/373ecb79-cd0d-4754-98ef-3076b37d5668" />

2. Cobertura por função

   <img width="1019" height="907" alt="image" src="https://github.com/user-attachments/assets/d37e33d8-6356-4e8f-8255-307a2252a69a" />

3. Cobertura por classe

   <img width="987" height="502" alt="image" src="https://github.com/user-attachments/assets/def26cf4-2038-40b3-a7ac-cc7371f578c0" />
