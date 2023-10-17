import tkinter as tk
import string
from tkinter import messagebox

root = tk.Tk()
root.title('Jogo da forca')
root.geometry('500x600')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=1)

# adicionando uma imagem inicial / fazer uma lista de imagens
imagem_inicial = tk.PhotoImage(file='./imagens/IMG_1161.png')

imagens = [tk.PhotoImage(file="imagens/IMG_1161.png"),tk.PhotoImage(file="imagens/IMG_1162.png"),tk.PhotoImage(file="imagens/IMG_1163.png"),
           tk.PhotoImage(file="imagens/IMG_1164.png"),tk.PhotoImage(file="imagens/IMG_1165.png"),tk.PhotoImage(file="imagens/IMG_1166.png"),
           tk.PhotoImage(file="imagens/IMG_1167.png"),tk.PhotoImage(file="imagens/IMG_1168.png")]
# redimensionando a imagem
imagem_resuzida = imagem_inicial.subsample(2,2)

imagens_reduzidas = []
for imagem in imagens:
    imagens_reduzidas.append(imagem.subsample(2,2))
    

# criando os widgets
frame_topo = tk.Frame(root, highlightbackground="blue", highlightthickness=2)
frame_topo.grid(column=0, row=1, columnspan=2)

frame_topo2 = tk.Frame(root, highlightbackground="blue", highlightthickness=2)
frame_topo2.grid(column=1, row=1, columnspan=2)

# exibindo a imagem
posicao_imagem = 0

label_imagem = tk.Label(frame_topo, image=imagens_reduzidas[posicao_imagem])
#label_imagem.pack()
label_imagem.grid(row=1, column=0)

label_teste = tk.Label(frame_topo2, text= 'teste')
label_teste.grid(row=1, column=0)

# frame palavra selecionada
frame_palavra = tk.Frame(root)
frame_palavra.grid(row=2, column=0, pady=10, columnspan=2)

palavra = 'VERMELHO'
label_palavra = []

posicao_da_letra = 0
for letra in palavra:
    label_palavra.append(tk.Label(frame_palavra, text='  ', border=1, bg='#ffe1cf'))
    label_palavra[posicao_da_letra].grid(row=2, column=posicao_da_letra, ipadx=8, ipady=5, padx=5)
    posicao_da_letra += 1

print('dicionario palavra', label_palavra)

# label_palavra = tk.Label(frame_palavra, text='', border=2, bg='red')
# label_palavra.grid(row=2, column=0, ipadx=8, ipady=5, padx=5)

# label_palavra2 = tk.Label(frame_palavra, text='', border=2, bg='red')
# label_palavra2.grid(row=2, column=1, ipadx=8, ipady=5, padx=5)

# frame para as letras do alfabeto
frame_alfabeto = tk.Frame(root, highlightbackground="red", highlightthickness=2)
frame_alfabeto.grid(row=3, column=0, pady=30, columnspan=2)

alfabeto = string.ascii_uppercase  # Obtém o alfabeto em letras maiúsculas
linhas = []  # Inicializa uma lista para armazenar as linhas
print(alfabeto)
alfabeto_lista = list(string.ascii_uppercase)

# Divide o alfabeto em linhas alternadas de seis e sete letras
for i in range(0, len(alfabeto), 13):
    print(i)
    linha = alfabeto[i:i+6]  # Linha com seis letras
    linhas.append(linha)
    if i + 6 < len(alfabeto):
        linha = alfabeto[i+6:i+13]  # Linha com sete letras
        linhas.append(linha)
print('linhas da lista',linhas)

# Imprime as quatro linhas
for linha in linhas:
    print('cada linha',linha)

button_dict={}
option= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
contador = 0
for i in option:
    def clique_botao(x=i):
        if x in palavra:
            print(x)
            posicoes = [i for i, letra in enumerate(palavra) if letra == x]
            for posicao in posicoes:
                label_palavra[posicao].config(text=x)
        else:
            global posicao_imagem
            posicao_imagem += 1
            print(x)
            print('nao')
            label_imagem.config(image=imagens_reduzidas[posicao_imagem])
            if posicao_imagem == 7:                
                messagebox.showinfo('Foi mal!', f'Infelizmente você perdeu! A palavra era: {palavra}', parent=root)
            
        button_dict[x].grid_forget()
       
    for linha, sublista in enumerate(linhas):
        if i in sublista:
            posicao_na_sublista = sublista.index(i)
            posicao_na_lista = linha, posicao_na_sublista
            break  # Se encontrarmos a letra, podemos sair do loop
        print('posicao da LETRA',posicao_na_lista)
    
    button_dict[i]=tk.Button(frame_alfabeto, text=alfabeto_lista[contador], command=clique_botao)
    button_dict[i].grid(row=posicao_na_lista[0], column=posicao_na_lista[1], ipadx=6, ipady=4)
    contador += 1

letras_lista = ['ABCDEF', 'GHIJKLM', 'NOPQRS', 'TUVWXYZ']
letra_procurada = 'R'  # A letra que você deseja encontrar

# Iterar pelas sublistas e procurar a letra
for linha, sublista in enumerate(letras_lista):
    if letra_procurada in sublista:
        posicao_na_sublista = sublista.index(letra_procurada)
        posicao_na_lista = linha, posicao_na_sublista
        break  # Se encontrarmos a letra, podemos sair do loop
print(posicao_na_lista[0])

root.mainloop()

