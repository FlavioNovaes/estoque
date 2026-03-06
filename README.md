# 📦 Sistema de Controle de Estoque

Este projeto é um **sistema de controle de estoque** desenvolvido utilizando **Python e Django**.
O objetivo do sistema é permitir o gerenciamento de produtos, quantidades e informações relacionadas ao estoque de forma organizada.

O projeto foi desenvolvido como parte dos meus estudos em **desenvolvimento web com Django**, aplicando conceitos de backend, banco de dados e estrutura de aplicações web.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-Framework-green)
![Status](https://img.shields.io/badge/Status-Estável-brightgreen)

---

## 🚀 Tecnologias Utilizadas

* Python
* Django
* SQLite (banco de dados padrão do Django)
* HTML
* CSS

---

## ⚙️ Funcionalidades

* 📦 Cadastro de produtos
* ✏️ Atualização de informações de produtos
* 🗑 Remoção de produtos
* 📋 Listagem de produtos em estoque
* 🔎 Organização e gerenciamento de dados

---

## 📂 Estrutura do Projeto

```
estoque/
│
├── estoque/          # Configurações principais do projeto Django
│
├── produtos/         # Aplicação responsável pela lógica de estoque
│
├── db.sqlite3        # Banco de dados SQLite
│
├── manage.py         # Arquivo de gerenciamento do Django
│
└── README.md
```

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```
git clone https://github.com/FlavioNovaes/estoque.git
```

### 2️⃣ Entrar na pasta do projeto

```
cd estoque
```

### 3️⃣ Criar ambiente virtual (recomendado)

```
python -m venv venv
```

### 4️⃣ Ativar o ambiente virtual

**Windows**

```
venv\Scripts\activate
```

**Linux / Mac**

```
source venv/bin/activate
```

### 5️⃣ Instalar dependências

```
pip install django
```

### 6️⃣ Rodar as migrações

```
python manage.py migrate
```

### 7️⃣ Iniciar o servidor

```
python manage.py runserver
```

Depois disso, abra no navegador:

```
http://127.0.0.1:8000/
```

---

## 🧠 Objetivo do Projeto

Este projeto foi criado com o objetivo de praticar:

* Desenvolvimento web com **Django**
* Estrutura de projetos backend
* Manipulação de dados com banco de dados
* Criação de aplicações **CRUD**
* Organização de aplicações web em Python

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos como:

* Arquitetura de projetos Django
* Modelos (**Models**)
* Views e Templates
* Migrações de banco de dados
* CRUD com Django

---

## 📈 Possíveis Melhorias Futuras

* Sistema de autenticação de usuários
* Controle de permissões (admin / usuário)
* Dashboard com estatísticas de estoque
* API REST com Django REST Framework
* Interface mais moderna com Bootstrap ou Tailwind

---


