# 🔐 Sistema de Login com Interface Gráfica
### 📌 Sobre o Projeto

O Sistema de Login com Tkinter é uma aplicação em Python desenvolvida para praticar:

Interface gráfica

Integração com banco de dados SQLite

Autenticação de usuários

Organização modular do código

O projeto simula um sistema real de login com cadastro, autenticação e controle de tentativas, sendo ideal para consolidar fundamentos de desenvolvimento backend + interface.

### ✨ Funcionalidades

✔ Cadastro de novos usuários
✔ Login com verificação de credenciais
✔ Integração com banco de dados SQLite
✔ Bloqueio automático após 3 tentativas incorretas
✔ Dashboard personalizada com nome do usuário
✔ Sistema de Logout
✔ Separação do projeto em múltiplos arquivos (arquitetura modular)

### 🗂 Estrutura do Projeto
projeto-login/

│

├── main.py        # Interface gráfica e controle da aplicação

├── auth.py        # Funções de autenticação (login e cadastro)

├── database.py    # Criação e gerenciamento do banco de dados

├── .gitignore

└── README.md

### 🚀 Como Funciona
1️⃣ Inicialização

O banco de dados é criado automaticamente ao iniciar a aplicação.

Caso já exista, nada é sobrescrito.

2️⃣ Cadastro

O usuário insere nome e senha.

O sistema verifica se o usuário já existe.

Caso não exista, salva no banco.

3️⃣ Login

Verifica as credenciais no banco.

Se corretas → abre o Dashboard.

Se incorretas → incrementa contador de tentativas.

Após 3 erros → sistema é encerrado.

4️⃣ Dashboard

Exibe mensagem personalizada:

Bem-vinda, [nome do usuário]!

Permite Logout retornando ao sistema principal.

### 🧠 Conceitos Praticados

Manipulação de interface com tkinter

Modularização de código

Controle de fluxo

Tratamento de erros

Banco de dados SQLite

Lógica de autenticação

Controle de estado (tentativas de login)

### 💻 Tecnologias Utilizadas

Python 3

Tkinter

SQLite

### ▶️ Exemplo de Uso

Ao iniciar:

Tela de Login
Usuário: maria
Senha: ********

Login bem-sucedido:

Bem-vinda, maria!

Após 3 tentativas incorretas:

Muitas tentativas! Sistema bloqueado.

---

## 👩🏻‍💻 Author

Tatiane Souza  
