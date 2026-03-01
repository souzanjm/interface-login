import tkinter as tk # isso é p n ficar escrevendo tkinter toda hora
from tkinter import messagebox # para mostrar mensagens de erro ou sucesso (popups/alertas)
from database import criar_banco # para criar o banco de dados e a tabela de usuários, que cria o banco no database.py
from auth import cadastrar_usuario, verificar_login # para cadastrar novos usuários e verificar o login, que tem as funções de cadastro e login no auth.py

tentativas = 0
# cria o banco antes de iniciar a interface, para garantir que ele exista quando o usuário tentar se cadastrar ou entrar.
# se o banco ainda não existir, ele é criado automaticamente
# se já existir, nada acontece (por causa do IF NOT EXISTS no SQL)
criar_banco()

def entrar(): # função que é chamada quando o usuário clica no botão "Entrar"
    global tentativas

    usuario = entry_usuario.get() # pega o texto que o usuário digitou no campo de usuário
    senha = entry_senha.get() # pega o texto que o usuário digitou no campo de senha

    resultado = verificar_login(usuario, senha)
   
    if resultado:
        tentativas = 0
        messagebox.showinfo("Sucesso", f"Bem-vinda, {usuario}!")
        abrir_dashboard(usuario)
    else:
        tentativas += 1

        if tentativas >= 3:
            messagebox.showerror("Bloqueado", "Muitas tentativas! Sistema bloqueado.")
            janela.destroy()
        else:
            messagebox.showerror("Erro", f"Tentativa {tentativas}/3")

def cadastrar():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if cadastrar_usuario(usuario, senha):
        messagebox.showinfo("Cadastro", "Usuário cadastrado!")
    else:
        messagebox.showerror("Erro", "Usuário já existe!")

def abrir_dashboard(nome_usuario):
    dashboard = tk.Toplevel()
    dashboard.title("Dashboard")
    dashboard.geometry("400x300")

    tk.Label(
        dashboard,
        text=f"Bem-vinda, {nome_usuario}!",
        font=("Helvetica", 16, "bold")
    ).pack(pady=20)

    tk.Button(
        dashboard,
        text="Logout",
        command=dashboard.destroy
    ).pack(pady=10)

# --------- INTERFACE ---------

janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("350x250")
janela.configure(bg="#f5f5f5")

frame = tk.Frame(janela, bg="#ffffff", padx=20, pady=20) # cria um frame branco dentro da janela, com um pouco de padding (espaçamento interno) para deixar os elementos mais organizados
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="Login", font=("Helvetica", 16, "bold"), bg="#ffffff").grid(
    row=0, column=0, columnspan=2, pady=(0, 15)
)

tk.Label(frame, text="Usuário", bg="#ffffff").grid(row=1, column=0, sticky="w")
entry_usuario = tk.Entry(frame)
entry_usuario.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Senha", bg="#ffffff").grid(row=2, column=0, sticky="w")
entry_senha = tk.Entry(frame, show="*")
entry_senha.grid(row=2, column=1, pady=5)

tk.Button(frame, text="Entrar", bg="#4CAF50", fg="white", command=entrar).grid(
    row=3, column=0, columnspan=2, pady=10
)

tk.Button(frame, text="Cadastrar", command=cadastrar).grid(
    row=4, column=0, columnspan=2
)

janela.mainloop()