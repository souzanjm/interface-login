import sqlite3
import hashlib

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def cadastrar_usuario(username, senha):
    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    senha_hash = hash_senha(senha)

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, senha_hash)
        )
        conexao.commit()
        return True
    except:
        return False
    finally:
        conexao.close()

def verificar_login(username, senha):
    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    senha_hash = hash_senha(senha)

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, senha_hash)
    )

    usuario = cursor.fetchone()
    conexao.close()

    return usuario is not None