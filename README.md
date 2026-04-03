📌 Sobre o projeto

API RESTful desenvolvida com Flask, utilizando autenticação via JWT (JSON Web Token) e integração com banco de dados MySQL.

O objetivo do projeto é aplicar conceitos de:

arquitetura backend
autenticação segura
organização de código em camadas
🧠 Funcionalidades
✅ Cadastro de usuários
✅ Login com geração de token JWT
✅ Criptografia de senha
✅ Persistência em banco de dados
🚧 Rotas protegidas (em desenvolvimento)
🛠️ Tecnologias utilizadas
Python
Flask
Flask-JWT-Extended
SQLAlchemy
MySQL
Postman

📂 Estrutura do projeto
Projeto back-end/
│── database/
│   └── db.py
│
│── models/
│   └── user.py
│
│── routes/
│   └── user_routes.py
│
│── app.py
│── config.py
│── requiremente.txt
⚙️ Como executar o projeto
🔧 Pré-requisitos
Python instalado
MySQL rodando
Git
▶️ Rodando localmente
# Clonar repositório
git clone https://github.com/matheusfideles-stack/API-RESTful.git

# Entrar na pasta
cd API-RESTful

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
venv\Scripts\activate

# Instalar dependências
pip install -r requiremente.txt

# Rodar aplicação
python app.py
🔐 Autenticação

A API utiliza JWT (JSON Web Token) para autenticação.

Após o login, um token é retornado e deve ser utilizado nas próximas requisições protegidas.

📌 Endpoints
🧑‍💻 Registro de usuário
POST /register
{
  "name": "Usuario",
  "email": "usuarioteste@email.com",
  "password": "123456"
}
🔑 Login
POST /login
{
  "email": "usuarioteste@email.com",
  "password": "123456"
}
🖼️ Demonstração
📍 Cadastro de usuário

📍 Login (retorno do token)

📍 Banco de dados MySQL

📍 Estrutura do projeto

🚧 Melhorias futuras
 Rotas protegidas com JWT
 Refresh token
 Validação de dados
 Documentação com Swagger
 Deploy em produção
👨‍💻 Autor

Matheus Fideles

🔗 GitHub: https://github.com/matheusfideles-stack
🔗 Linkedln : https://www.linkedin.com/in/matheus-fideles-46b932313/

📄 Licença

Este projeto está sob a licença MIT.

⭐ Se esse projeto te ajudou

Deixe uma ⭐ no repositório — isso ajuda muito!
