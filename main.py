import pandas as pd
import customtkinter  # Supondo que você tenha uma biblioteca customtkinter personalizada
from funcoes import*


def main():
    root = customtkinter.CTk()
    root.geometry("650x500")

    custom_font = ("Roboto", 24)

    # Função para registrar um novo produto
    def rg():
        # Chama a função de registro (substitua com sua implementação)
        register(entry_nomeProduto_cadastro.get(), entry_Descricao_cadastro.get(),
                entry_valorProduto_cadastro.get(), entry_disponivelProduto_cadastro.get())
        
        # Limpa os campos após o registro
        entry_nomeProduto_cadastro.delete(0, 'end')
        entry_Descricao_cadastro.delete(0, 'end')
        entry_valorProduto_cadastro.delete(0, 'end')
        
        # Atualiza a listagem após o registro
        update_listagem()
        mostra_tela_listagem()

    # Função para mostrar o frame de cadastro
    def mostra_tela_registrar():
        frame_listagem.pack_forget()
        frame_cadastro.pack()

    # Função para mostrar o frame de listagem e atualizar os dados
    def mostra_tela_listagem():
        frame_cadastro.pack_forget()
        update_listagem()
        frame_listagem.pack()

    # Função para atualizar a listagem de produtos
    def update_listagem():
        # Limpa widgets antigos de listagem
        for widget in frame_listagem.winfo_children():
            widget.destroy()
        
        # Recupera os dados atualizados
        da = dados()
        
        # Exibe os produtos na listagem
        label_listagem = customtkinter.CTkLabel(master=frame_listagem, text="Listagem de produto", font=custom_font)
        label_listagem.pack(pady=12, padx=10)
        
        for index, row in da.iterrows():
            nome = row['Nome']
            valor = row['Valor']
            
            # Criando um label para exibir cada produto
            label_produto = customtkinter.CTkLabel(master=frame_listagem, text=f"{nome}: R${valor:.2f}", font=custom_font)
            label_produto.pack(pady=6, padx=10)
        
        # Botão para voltar ao cadastro
        button_voltarParaCastro = customtkinter.CTkButton(master=frame_listagem, text="Cadastrar novo produto", hover_color="green", command=mostra_tela_registrar)
        button_voltarParaCastro.pack(pady=12, padx=10)

    # Função para ler os dados do arquivo CSV
    def dados():
        db = pd.read_csv('cadastro_produto/bd_produto/produtos.csv', encoding='latin1')
        produtos = db[['Nome', 'Valor']]
        produtos_ordenados = produtos.sort_values(by='Valor')
        return produtos_ordenados

    # Frame de cadastro
    frame_cadastro = customtkinter.CTkFrame(master=root)
    frame_cadastro.pack(pady=20, padx=60, fill="both", expand=True)

    label_cadastro = customtkinter.CTkLabel(master=frame_cadastro, text="Cadastro de Produto", font=custom_font)
    label_cadastro.pack(pady=12, padx=10)

    entry_nomeProduto_cadastro = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text="Nome do produto")
    entry_nomeProduto_cadastro.pack(pady=12, padx=10)

    entry_Descricao_cadastro = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text="Descrição", width=140, height=72)
    entry_Descricao_cadastro.pack(pady=12, padx=10)

    entry_valorProduto_cadastro = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text="Valor do produto")
    entry_valorProduto_cadastro.pack(pady=12, padx=10)

    label_disponivelProduto_cadastro = customtkinter.CTkLabel(master=frame_cadastro, text="Disponível para venda", font=("Roboto", 18))
    label_disponivelProduto_cadastro.pack(pady=12, padx=10)

    entry_disponivelProduto_cadastro = customtkinter.CTkComboBox(master=frame_cadastro, values=["sim", "não"])
    entry_disponivelProduto_cadastro.pack(pady=12, padx=10)

    button_cadastrar = customtkinter.CTkButton(master=frame_cadastro, text="Cadastrar", hover_color="green", command=rg)
    button_cadastrar.pack(pady=12, padx=10)

    # Frame de listagem inicial
    frame_listagem = customtkinter.CTkFrame(master=root)
    frame_listagem.pack(pady=20, padx=60, fill="both", expand=True)

    # Inicialmente mostra o frame de cadastro
    mostra_tela_registrar()

    # Loop principal do Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()