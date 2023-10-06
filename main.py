from tkinter import *
from tkinter import ttk
import mysql.connector
conexao = mysql.connector.connect(
    host='aws.connect.psdb.cloud',
    user='qi5mny5pgbx5i3t97l6a',
    password='pscale_pw_IcLyAgT4dkYhFAuLKrQC1WwN9vU1oCaPJnRAII9M62X',
    database='db_gerenciamento_oficina_4bi',
)
cursor = conexao.cursor()

janela1 = Tk()
janela1.iconbitmap('icone.ico')
janela1.title('MechPro')    
janela1.geometry('500x500')
janela1.resizable(width=False, height=False)
janela1.config(bg='orange')


janela1.mainloop()  

cursor.close()
conexao.close()