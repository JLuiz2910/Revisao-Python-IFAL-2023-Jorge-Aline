import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def executar_codigo(arquivo):
    try:
        exec(open(arquivo).read())
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def realizar_pesquisa():
    termo_pesquisa = entrada_pesquisa.get()

    # Limpar os botões existentes antes de criar novos
    for widget in frame.winfo_children():
        widget.destroy()

    pasta = filedialog.askdirectory(title="Selecionar pasta")  # Selecionar a pasta a ser pesquisada
    if not pasta:  # Verificar se o usuário selecionou uma pasta
        return

    arquivos = os.listdir(pasta)
    arquivos_py = [arquivo for arquivo in arquivos if arquivo.endswith(".py")]

    # Filtrar arquivos com base no termo de pesquisa
    arquivos_filtrados = []
    for arquivo in arquivos_py:
        if termo_pesquisa.lower() in arquivo.lower():
            arquivos_filtrados.append(arquivo)

    for arquivo in arquivos_filtrados:
        btn = tk.Button(frame, text=arquivo, command=lambda a=arquivo: executar_codigo(os.path.join(pasta, a)))
        btn.pack()

root = tk.Tk()
root.title("Lista de Códigos Python")

frame_pesquisa = tk.Frame(root)
frame_pesquisa.pack(padx=20, pady=10)

entrada_pesquisa = tk.Entry(frame_pesquisa)
entrada_pesquisa.pack(side=tk.LEFT, padx=5)
btn_pesquisar = tk.Button(frame_pesquisa, text="Pesquisar", command=realizar_pesquisa)
btn_pesquisar.pack(side=tk.LEFT)

frame = tk.Frame(root)
frame.pack(padx=20, pady=10)

root.mainloop()
