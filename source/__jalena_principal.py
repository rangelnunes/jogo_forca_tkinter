import tkinter as tk 
import string
from tkinter import messagebox
import time
import random

root = tk.Tk()
root.title('Jogo da forca com Tkinter')
#root.geometry('500x600')
root.resizable(False,False)

# essa variavel serve para controlar a execucao do jogo
executando = True

# definindo as funções
def cronometro_decrescente(tempo_em_segundos):
    global executando
    botao_iniciar.configure(state='disabled')
    botao_parar.configure(state='normal')
    for i in option:
        button_dict[i].configure(state='normal')
    while tempo_em_segundos >= 0:
        minutos, segundos = divmod(tempo_em_segundos, 60)
        label_cronometro.config(text=f"Tempo Restante: {minutos:02d}:{segundos:02d}")
        root.update()
        time.sleep(1)
        tempo_em_segundos -= 1
        if not executando:
            break

    label_cronometro.config(text=f"Tempo Esgotado: {minutos:02d}:{segundos:02d}")
    botao_iniciar.configure(state='normal')
    botao_parar.configure(state='disabled')

def stop():
    global executando
    executando = False 

def close():
    global executando
    executando = False 
    root.quit()


# a janela sera dividida em frames
frame_pontuacao = tk.Frame(root, border=1, highlightbackground="orange")
frame_pontuacao.grid(row=0, column=0, columnspan=3, sticky=tk.EW, pady=15)

label_pontuacao = tk.Label(frame_pontuacao, text="Pontos: 0")
label_pontuacao.config(font=('Arial', 14, 'bold'))
label_pontuacao.pack(side=tk.LEFT, padx=20)

label_recorde = tk.Label(frame_pontuacao, text="Recorde: 0")
label_recorde.config(font=('Arial', 14, 'bold'))
label_recorde.pack(side=tk.RIGHT, padx=20)

# primeiro frame: tera imagens e outros widgets
#frame_topo = tk.Frame(root, highlightbackground="red", highlightthickness=2, borderwidth=1)
frame_topo = tk.Frame(root)
frame_topo.grid(row=1, column=0, columnspan=3, sticky=tk.EW)
#frame_topo.columnconfigure(1, weight=2)

# definindo uma lista de imagens que serão usadas no jogo
imagens = [tk.PhotoImage(file="imagens/IMG_1161.png"),tk.PhotoImage(file="imagens/IMG_1162.png"),tk.PhotoImage(file="imagens/IMG_1163.png"),
           tk.PhotoImage(file="imagens/IMG_1164.png"),tk.PhotoImage(file="imagens/IMG_1165.png"),tk.PhotoImage(file="imagens/IMG_1166.png"),
           tk.PhotoImage(file="imagens/IMG_1167.png"),tk.PhotoImage(file="imagens/IMG_1168.png")]

# imagens = [tk.PhotoImage(file="imagens/ampulheta/ampulheta01.png"),tk.PhotoImage(file="imagens/ampulheta/ampulheta02.png"),tk.PhotoImage(file="imagens/ampulheta/ampulheta03.png"),
#            tk.PhotoImage(file="imagens/ampulheta/ampulheta04.png"),tk.PhotoImage(file="imagens/ampulheta/ampulheta05.png"),tk.PhotoImage(file="imagens/ampulheta/ampulheta06.png"),
#            tk.PhotoImage(file="imagens/ampulheta/ampulheta07.png"),tk.PhotoImage(file="imagens/ampulheta/ampulheta08.png")]


# reduzindo o tamanho das imagens
imagens_reduzidas = []
for imagem in imagens:
    #imagens_reduzidas.append(imagem.subsample(2,2))
    imagens_reduzidas.append(imagem.subsample(3,3))

# exibindo a imagem
posicao_da_imagem_na_lista = 0

imagens_forca = tk.Label(frame_topo, image=imagens_reduzidas[posicao_da_imagem_na_lista])
#imagens_forca.grid(row=0, column=0, sticky=tk.EW)
imagens_forca.pack(side=tk.LEFT)

# outras informações do Jogo
label_categoria = tk.Label(frame_topo, text='Categoria:')
#label_categoria.grid(row=0, column=1)
label_categoria.pack(expand=True, anchor=tk.S)

label_valor_categoria = tk.Label(frame_topo, text='Cores')
label_valor_categoria.config(font=('Arial', 14, 'bold'))
#label_valor_categoria.grid(row=1, column=1, sticky=tk.N)
label_valor_categoria.pack(expand=True, anchor=tk.N)

# frame para o cronometro
frame_cronometro = tk.Frame(root)
frame_cronometro.grid(row=2, column=0, columnspan=3, pady=15)

tempo_em_segundos = 30
#cronometro_decrescente(tempo_em_segundos)
label_cronometro = tk.Label(frame_cronometro, text=f"Tempo Restante: {00:02d}:{tempo_em_segundos:02d}", border=1, bg='#fff8e7')
label_cronometro.config(font=('Futura', 13, 'bold'), foreground='#3C3B3B')
label_cronometro.grid(row=0, column=1, ipadx=5, ipady=4)

# frame para a palavra a ser descoberta
frame_palavra = tk.Frame(root, highlightthickness=2, borderwidth=1)
frame_palavra.grid(row=3, column=0, columnspan=3, pady=10)
#frame_palavra.columnconfigure(1, weight=1)

lista_de_palavras = ['VERMELHO', 'AZUL', 'VERDE', 'AMARELO', 'LARANJA', 'ROXO', 'ROSA', 'PRETO', 'BRANCO', 'MARROM']
palavra = random.choice(lista_de_palavras)
label_palavra = []
#frame_palavra.columnconfigure(len(palavra))

posicao_da_letra = 0
for letra in palavra:
    label_palavra.append(tk.Label(frame_palavra, text='', border=1, bg='#ffe1cf'))
    label_palavra[posicao_da_letra].grid(row=1, column=posicao_da_letra, ipadx=8, ipady=5, padx=5)
    posicao_da_letra += 1

# frame para as letras do alfabeto
frame_alfabeto = tk.Frame(root)
frame_alfabeto.grid(row=4, column=0, columnspan=3, pady=20)

# alfabeto = tk.Label(frame_alfabeto, text='alfabeto')
# alfabeto.grid(row=1, column=2, sticky=tk.EW)

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

# imagem de fundo para o botao
#imagem_botao_alfabeto = tk.PhotoImage(file='./imagens/botao.png')

contador = 0
for i in option:
    def clique_botao(x=i):        
        if x in palavra:
            posicoes = [i for i, letra in enumerate(palavra) if letra == x]
            for posicao in posicoes:
                label_palavra[posicao].config(text=x)
        else:
            global posicao_da_imagem_na_lista
            posicao_da_imagem_na_lista += 1
            print(x)
            print('nao')
            imagens_forca.config(image=imagens_reduzidas[posicao_da_imagem_na_lista])
            root.update()
            print('imagem',posicao_da_imagem_na_lista)
            if posicao_da_imagem_na_lista == 7:                
                messagebox.showinfo('Foi mal!', f'Infelizmente você perdeu! A palavra era: {palavra}', parent=root)
        # testando se ainda possuem espaços vazios
        labels_vazios = 0
        for i in range(len(palavra)):
            if label_palavra[i].cget('text') == '':
                labels_vazios += 1
        print('vazios', labels_vazios)
        if labels_vazios == 0:
            messagebox.showinfo('Uhuhu', 'Parabéns! Você acertou!', parent=root) 
            stop()                               


        button_dict[x].grid_forget()

    for linha, sublista in enumerate(linhas):
        if i in sublista:
            posicao_na_sublista = sublista.index(i)
            posicao_na_lista = linha, posicao_na_sublista
            break  # Se encontrarmos a letra, podemos sair do loop
    
    button_dict[i]=tk.Button(frame_alfabeto, state='disabled',text=alfabeto_lista[contador], command=clique_botao, foreground='#3C3B3B', width=4, height=2)
    button_dict[i].grid(row=posicao_na_lista[0], column=posicao_na_lista[1], ipadx=5, ipady=5)
    # if posicao_na_lista[0] % 2 == 0:
    #     print('par')
    #     button_dict[i].pack(fill=tk.BOTH, expand=True, side=tk.LEFT, ipadx=5, ipady=5)
    # else:
    #     print('impar')
    #     button_dict[i].pack(side=tk.LEFT,ipadx=5, ipady=5)
    
    
    contador += 1

# frame botoes
frame_botoes = tk.Frame(root)
frame_botoes.grid(row=5, column=0, columnspan=3, pady=12)

botao_iniciar = tk.Button(frame_botoes, text='Iniciar', command= lambda: cronometro_decrescente(tempo_em_segundos))
botao_iniciar.grid(row=0, column=0, ipadx=5, ipady=5, padx=5)

botao_parar = tk.Button(frame_botoes, text='Parar', command=stop, state='disabled')
botao_parar.grid(row=0, column=1, ipadx=5, ipady=5, padx=5)

botao_sair = tk.Button(frame_botoes, text='Sair', command=close)
botao_sair.grid(row=0, column=2, ipadx=5, ipady=5, padx=5)


root.mainloop()
