import csv
import tkinter as tk
import os
import customtkinter
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd


def register(name, description, price, available):
    diretorio = 'cadastro_produto/bd_produto'
    arquivo_csv = os.path.join(diretorio, 'produtos.csv')

    # Verifica se o diretório existe, se não, cria-o
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    # Verifica se o arquivo existe, se não, cria-o com cabeçalho
    if not os.path.exists(arquivo_csv):       
        with open(arquivo_csv, mode='w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['Nome', 'Descricao', 'Valor', 'Disponivel'])


    # Adiciona a nova linha
    num = price.replace(",",".")

    with open(arquivo_csv, mode='a', newline='') as arquivo:
        writer = csv.writer(arquivo)  
        writer.writerow([name, description, float(num), available])
    
    messagebox.showinfo("Registro Sucesso", "Registro realizado com sucesso!")


