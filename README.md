# 💰 Sistema de Controle Financeiro Pessoal (CLI & POO)

[![Python Version](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Um sistema de controle financeiro pessoal executado via terminal, reestruturado sob o paradigma de **Programação Orientada a Objetos (POO)**. Este projeto faz parte da minha jornada de transição de carreira de **Professor de Matemática para Desenvolvedor Backend Python**, aplicando conceitos avançados de arquitetura de software, modularização e boas práticas de código.

---

## ⚙️ Funcionalidades

- **Gestão de Fluxo de Caixa:** Entradas (receitas) e saídas (despesas) tratadas como modelos de dados bem definidos.
- **Validação de Saldos e Regras de Negócio:** Bloqueio e tratamento para operações que excedam o saldo disponível.
- **Extrato e Histórico Dinâmico:** Visualização clara do histórico de movimentações e saldo consolidado.
- **Interface CLI Interativa:** Menu em loop contínuo com tratamento robusto de exceções e entradas do usuário.
- **Armazenamento em Memória / Persistência:** Estrutura modular preparada para persistência de dados isolada da interface.

---

## 🛠️ Arquitetura e Conceitos Aplicados

- **Linguagem:** Python 3.13+
- **Programação Orientada a Objetos (POO):** Encapsulamento, criação de classes/modelos para representar entidades do domínio e separação clara de responsabilidades.
- **Arquitetura Modular:** Separação entre a interface de linha de comando (`src/cli/` ou `main.py`), modelos de dados (`src/models/` ou `docs/modulos`) e lógica de aplicação.
- **Versionamento e Git Flow:** Commits semânticos (`refatoracao-poo`, `refactor(cli)`) e uso de Pull Requests para integração contínua no GitHub.

---

## 📂 Estrutura do Projeto

```text
sistema-de-financas/
├── docs/
│   └── imagens/          # Screenshots e demonstrações visuais da aplicação
├── src/                  # Código-fonte principal refatorado em POO
│   ├── models/           # Classes e entidades do sistema (ex: Conta, Transacao)
│   └── ...               # Serviços e utilitários
├── .gitignore            # Arquivos e pastas ignorados pelo Git
├── main.py               # Ponto de entrada (CLI) da aplicação
└── README.md             # Documentação do projeto
```

---

## ▶️ Como Executar o Projeto

Certifique-se de ter o Python 3.13 (ou superior) instalado na sua máquina. Não é necessária a instalação de dependências externas.

**1 - Clone o repositório:**

```Bash
git clone [https://github.com/samuel-svaz-dev/sistema-de-financas.git](https://github.com/samuel-svaz-dev/sistema-de-financas.git)
```

**2 - Navegue até o diretório do projeto:**

```Bash
cd sistema-de-financas
```


**3 -Execute a aplicação:**

```Bash
python main.py
```

---

## 🚧 Roadmap de Evolução
[x] Refatoração para POO: Migração da arquitetura funcional/procedural para Orientada a Objetos.

[ ] Persistência Estruturada (JSON/SQLite): Implementação de banco de dados ou arquivos JSON para persistência permanente.

[ ] Categorização de Transações: Separação por categorias (Ex: Alimentação, Moradia, Lazer).

[ ] Testes Automatizados: Cobertura de testes unitários com pytest para validação das regras de negócio.

## 📸 Demonstração do Sistema
(Confira os registros visuais do funcionamento da aplicação na pasta docs/imagens)

## 👤 Autor
**Samuel Vaz**

Professor de Matemática & Desenvolvedor Backend Python.

Sinta-se à vontade para entrar em contato, sugerir melhorias no código ou acompanhar meu portfólio de transição de carreira!

GitHub: @samuel-svaz-dev

LinkedIn: Samuel Vaz