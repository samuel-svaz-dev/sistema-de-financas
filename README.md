# 💰 Sistema de Controle Financeiro Pessoal

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Um sistema de controle financeiro pessoal simplificado executado via terminal. Este projeto foi desenvolvido com o objetivo de consolidar conceitos fundamentais de lógica de programação, modularização de código e persistência de dados em Python.

**Nota de Contexto:** Este projeto faz parte do meu portfólio focado na transição de carreira de Professor de Matemática para Desenvolvedor Backend Python. Tento por meio desse projeto aplicar os conceitos que venho estudando e pesquisando.

---

## ⚙️ Funcionalidades

- **Gestão de Fluxo de Caixa:** Cadastro modular de receitas e despesas.
- **Validação de Consistência:** Bloqueio inteligente de despesas que superem o saldo disponível em conta.
- **Extrato Dinâmico:** Histórico completo de movimentações realizadas.
- **Persistência em Arquivo:** Armazenamento e leitura de dados via arquivo local (`financas.txt`), garantindo a preservação das informações entre as sessões.
- **Interface CLI Interativa:** Menu estruturado em loop com validações contra inputs inválidos do usuário.

---

## 🛠️ Tecnologias e Conceitos Aplicados

- **Linguagem:** Python 3.13
- **Modularização:** Divisão de responsabilidades entre fluxo de controle (`main.py`) e lógica de negócio (`funcoes_calculo/`).
- **I/O de Arquivos:** Manipulação de leitura e escrita para persistência de dados local.
- **Versionamento:** Boas práticas de commits com Git e organização de repositório no GitHub.

---

## 📂 Estrutura do Projeto

```text
sistema-de-financas/
├── apresentacao/         # Elementos visuais e demonstrações do sistema
├── funcoes_calculo/      # Módulos contendo as regras de negócio e persistência
├── imagens/              # Imagens utilizadas na documentação
├── financas.txt          # Arquivo de persistência local dos dados
├── main.py               # Ponto de entrada do programa e fluxo do menu
└── README.md             # Documentação do projeto

```

---

## ▶️ Como Executar o Projeto

Certifique-se de ter o Python 3.13 (or superior) instalado em sua máquina. Não há necessidade de instalar dependências externas.

1. Clone este repositório:
```bash
git clone [https://github.com/samuel-svaz-dev/sistema-de-financas.git](https://github.com/samuel-svaz-dev/sistema-de-financas.git)

```


2. Navegue até o diretório do projeto:
```bash
cd sistema-de-financas

```


3. Execute a aplicação:
```bash
python main.py

```



---

## 🚧 Roadmap de Evolução

O projeto está em constante evolução. Os próximos passos planejados são:

* [ ] **Refatoração para POO:** Migrar a arquitetura funcional atual para Programação Orientada a Objetos (OOP).
* [ ] **Persistência Estruturada (JSON):** Substituir o arquivo TXT por armazenamento JSON para melhor estruturação dos dados.
* [ ] **Categorização:** Adicionar categorias para despesas (Ex: Alimentação, Transporte) e receitas.
* [ ] **Testes Automatizados:** Implementar testes unitários utilizando `pytest` para garantir a integridade dos cálculos.

---

## 👤 Autor

**Samuel Vaz**
*Professor de Matemática & Desenvolvedor Backend Python em Construção.*

Fique à vontade para se conectar comigo, dar feedbacks sobre o código ou sugerir melhorias!

* **GitHub:** [@samuel-svaz-dev](https://github.com/samuel-svaz-dev)
* **LinkedIn:** [Samuel Vaz](https://www.linkedin.com/in/samuel-souza-vaz-1bb547378/)

```

```
