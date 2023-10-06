import tkinter as tk
from tkinter import messagebox

def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

   
    if usuario == "usuario" and senha == "senha":
        messagebox.showinfo("Login bem-sucedido", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro de login", "Nome de usuário ou senha incorretos")


def redefinir_senha():
    messagebox.showinfo("Redefinir Senha", "Link para redefinir a senha enviado para o seu e-mail")


janela = tk.Tk()
janela.title("Painel de Login - Software de Mecânica")

label_usuario = tk.Label(janela, text="Nome de Usuário:")
label_senha = tk.Label(janela, text="Senha:")

entrada_usuario = tk.Entry(janela)
entrada_senha = tk.Entry(janela, show="*") 

botao_login = tk.Button(janela, text="Login", command=verificar_login)
botao_redefinir_senha = tk.Button(janela, text="Redefinir Senha", command=redefinir_senha)


label_usuario.pack()
entrada_usuario.pack()
label_senha.pack()
entrada_senha.pack()
botao_login.pack()
botao_redefinir_senha.pack()

janela.mainloop()
