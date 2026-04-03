# 📌 Sobre o projeto

API RESTful desenvolvida com Flask, utilizando autenticação via JWT (JSON Web Token) e integração com banco de dados MySQL.

O objetivo do projeto é aplicar conceitos de:

Arquitetura backend;

Autenticação segura;

Organização de código em camadas;

# 🧠 Funcionalidades

✅ Cadastro de usuários

✅ Login com geração de token JWT

✅ Criptografia de senha


✅ Persistência em banco de dados

🚧 Rotas protegidas (em desenvolvimento)

# 🛠️ Tecnologias utilizadas

Python

Flask

Flask-JWT-Extended

SQLAlchemy

MySQL

Postman

# 📂 Estrutura do projeto

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


# ⚙️ Como executar o projeto

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

# 🔐 Autenticação

A API utiliza JWT (JSON Web Token) para autenticação.

Após o login, um token é retornado e deve ser utilizado nas próximas requisições protegidas.

# 📌 Endpoints

# 🧑‍💻 Registro de usuário

POST /register

{

  "name": "Usuario",
  
  "email": "usuarioteste@email.com",
  
  "password": "123456"
  
}

# 🔑 Login

POST /login

{

  "email": "usuarioteste@email.com",
  
  "password": "123456"
  
}


# 🖼️ Demonstração

# 📍 Cadastro de usuário

<img width="1919" height="1026" alt="Image" src="https://github.com/user-attachments/assets/188f3703-ee2d-4952-9cfa-d97793202593" />

# 📍 Login (retorno do token)

<img width="1919" height="1033" alt="Image" src="https://github.com/user-attachments/assets/162a289d-603c-46a2-a951-7c3d97046648" />

# 📍 Banco de dados MySQL

<img width="1912" height="1028" alt="Image" src="https://github.com/user-attachments/assets/f9b7e355-7b74-4165-a160-149fb8be3b51" />

# 📍 Estrutura do projeto

<img width="342" height="461" alt="Image" src="https://github.com/user-attachments/assets/24120f20-793f-4940-8a86-c2db51b78fa0" />

# 🚧 Melhorias futuras

 Rotas protegidas com JWT
 
 Refresh token
 
 Validação de dados
 
 Documentação com Swagger
 
 Deploy em produção
 
# 👨‍💻 Autor


# Matheus Fideles

 🔗 GitHub: https://github.com/matheusfideles-stack
 
 🔗 Linkedln : https://www.linkedin.com/in/matheus-fideles-46b932313/

# 📄 Licença

Este projeto está sob a licença MIT.

# ⭐ Se esse projeto te ajudou

Deixe uma ⭐ no repositório — isso ajuda muito!
