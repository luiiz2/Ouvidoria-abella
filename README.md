
# 📢 Ouvidoria - Sistema de Manifestações (Python + MySQL)

Este projeto é um **sistema de ouvidoria em Python**, onde usuários podem cadastrar, listar, filtrar, buscar e excluir manifestações como **reclamações, elogios e sugestões**.

A aplicação utiliza **MySQL** como banco de dados e módulos de conexão customizados para organizar melhor o código.

---

## 🚀 Funcionalidades

- 📄 Listar todas as manifestações
- 🔍 Filtrar manifestações por tipo (reclamação, elogio ou sugestão)
- ➕ Cadastrar nova manifestação
- 🔢 Exibir total de manifestações
- 🔎 Buscar manifestação por código
- ❌ Excluir manifestação pelo código
- ⛔ Encerrar o sistema

---

## 🛠 Requisitos para rodar

### ✔️ Python 3

Verifique se o Python 3 está instalado:

```bash
python --version
```

Se não estiver instalado, baixe aqui: https://www.python.org/downloads/

### ✔️ MySQL Server

Você precisa ter o MySQL instalado e em execução.

Download: https://dev.mysql.com/downloads/mysql/

Crie um usuário com senha (por exemplo: `root/12345`).

### ✔️ Conector Python ↔ MySQL (versão específica)

Este projeto exige a biblioteca `mysql-connector-python` na versão **8.4.0**.

Instale com:

```bash
pip install mysql-connector-python==8.4.0
```

⚠️ Importante: outras versões podem causar erros ao usar `cursor(prepared=True)`.

---

## 💾 Estrutura do Banco de Dados

Crie o banco de dados com:

```sql
CREATE DATABASE ouvidoria;
USE ouvidoria;

CREATE TABLE manifestacoes (
    nome VARCHAR(100),
    tipo VARCHAR(20),
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    manifestaçao TEXT
);
```

---

## 📁 Estrutura de Arquivos

```
ouvidoria/
├── Ouvidoria-Samu-Luiz.py        # Script principal com o menu e funcionalidades
├── operacoesbd.py                # Módulo de funções para conectar e manipular o banco
└── README.md                     # Instruções do projeto
```

---

## ✅ Pronto!

Agora você pode rodar o projeto com:

```bash
python Ouvidoria-Samu-Luiz.py
```
