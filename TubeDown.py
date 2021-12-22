#criando um menu de app com tkinter

from tkinter import *
import tkinter as tk
import os

def semComando():
    print("")

app = Tk()
app.title("TubeDown")
app.geometry("500x500")
app.configure(background="#dde")

barraDeMenus = Menu(app)
menuContatos = Menu(barraDeMenus,tearoff=0)
menuContatos.add_command(label="Novo", command=semComando)
menuContatos.add_command(label="Pesquisar", command=semComando)
menuContatos.add_command(label="Deletar", command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar", command=app.quit)
barraDeMenus.add_cascade(label="Contatos", menu=menuContatos)

menuManutencao = Menu(barraDeMenus,tearoff=0)
menuManutencao.add_command(label="Banco de Dados", command=semComando)
barraDeMenus.add_cascade(label="Manutenção", menu=menuManutencao)

menuSobre = Menu(barraDeMenus,tearoff=0)
menuSobre.add_command(label="TubeDown", command=semComando)
barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)


app.config(menu=barraDeMenus)

app.mainloop()