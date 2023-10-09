import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import string
import time

root = tk.Tk()
root.title('Jogo da ampulheta em Tkinter')
root.resizable(False,False)

# funções ########################################################################

# esta variável serve para controlar a execucao do jogo
executando = True

def show_word():
    global label_palavra
    label_palavra[0].pack_forget()
    label_palavra = []

    posicao_da_letra = 0
    for i in range(len(palavra)):
        label_palavra.append(tk.Label(frame_palavra, text='', border=1, bg='#ffe1cf'))
        label_palavra[i].pack(side=tk.LEFT, ipadx=8, ipady=5, padx=5)
        #label_palavra[i].grid(row=1, column=posicao_da_letra, ipadx=8, ipady=5, padx=5)
        posicao_da_letra += 1

def start(tempo_em_segundos = 30):
    global executando
    executando = True
    botao_iniciar.configure(state='disabled')
    botao_parar.configure(state='normal')
    show_word()
    for i in option:
        button_dict[i].configure(state='normal')
    while tempo_em_segundos >= 0:
        minutos, segundos = divmod(tempo_em_segundos, 60)
        #label_cronometro.config(text=f"Tempo Restante: {minutos:02d}:{segundos:02d}")
        label_cronometro.config(text=f"{minutos:02d}:{segundos:02d}")
        root.update()
        time.sleep(1)
        tempo_em_segundos -= 1
        if not executando:
            break

    #label_cronometro.config(text=f"Tempo Esgotado: {minutos:02d}:{segundos:02d}")
    label_cronometro.config(text=f"{minutos:02d}:{segundos:02d}")
    botao_iniciar.configure(state='normal')
    botao_parar.configure(state='disabled')

def stop():
    global executando
    botao_iniciar.configure(state='normal')
    botao_parar.configure(state='disabled')
    executando = False 

def close():
    global executando
    executando = False 
    root.quit()

# janela da aplicacao ############################################################

# frame para o topo com a pontuacao do jogo e o recorde
frame_pontuacao = tk.Frame(root)
frame_pontuacao.pack(fill=tk.X)

label_pontuacao = tk.Label(frame_pontuacao, text="Pontos: 0")
label_pontuacao.config(font=('Arial', 14, 'bold'))
label_pontuacao.pack(side=tk.LEFT, padx=20)

label_recorde = tk.Label(frame_pontuacao, text="Recorde: 0")
label_recorde.config(font=('Arial', 14, 'bold'))
label_recorde.pack(side=tk.RIGHT, padx=20)

# frame para a sequencia de imagens e as categorias
frame_topo = tk.Frame(root)
frame_topo.pack()

# definindo uma lista de imagens que serão usadas no jogo
imagens = [tk.PhotoImage(file="imagens/IMG_1161.png"),tk.PhotoImage(file="imagens/IMG_1162.png"),tk.PhotoImage(file="imagens/IMG_1163.png"),
           tk.PhotoImage(file="imagens/IMG_1164.png"),tk.PhotoImage(file="imagens/IMG_1165.png"),tk.PhotoImage(file="imagens/IMG_1166.png"),
           tk.PhotoImage(file="imagens/IMG_1167.png"),tk.PhotoImage(file="imagens/IMG_1168.png")]

# reduzindo o tamanho das imagens
imagens_reduzidas = []
for imagem in imagens:
    imagens_reduzidas.append(imagem.subsample(2,2))

# exibindo a imagem inicial
posicao_da_imagem_na_lista = 0

imagens_forca = tk.Label(frame_topo, image=imagens_reduzidas[posicao_da_imagem_na_lista])
imagens_forca.pack(side=tk.LEFT)

# outras informações ao lado da imagem. Ex.: categoria da palavra
label_categoria = tk.Label(frame_topo, text='Categoria:')
label_categoria.pack(expand=True, anchor=tk.S, padx=30)

label_valor_categoria = tk.Label(frame_topo, text='Cores')
label_valor_categoria.config(font=('Arial', 14, 'bold'))
label_valor_categoria.pack(expand=True, anchor=tk.N, padx=30)

# frame para o cronometro
frame_cronometro = tk.Frame(root)
frame_cronometro.pack(fill=tk.X, pady=10)

background_relogio = Image.open('./imagens/relogio_digital.png')
background_relogio_reduzido = background_relogio.resize((90,60), Image.ANTIALIAS)
background_relogio_label = ImageTk.PhotoImage(background_relogio_reduzido)

tempo_em_segundos = 30
label_cronometro = tk.Label(frame_cronometro, text=f"{00:02d}:{tempo_em_segundos:02d}", border=1, image=background_relogio_label, compound='center')
label_cronometro.config(font=('Futura', 13, 'bold'), foreground='#46eb34')
label_cronometro.pack()

# frame para a palavra a ser descoberta
frame_palavra = tk.Frame(root)
frame_palavra.pack(fill=tk.X, pady=10)

# pesquisa no bd a palavra, de acordo com a categoria selecionada
lista_de_palavras = ['VERMELHO', 'AZUL', 'VERDE', 'AMARELO', 'LARANJA', 'ROXO', 'ROSA', 'PRETO', 'BRANCO', 'MARROM']
palavra = random.choice(lista_de_palavras)
label_palavra = []

label_palavra.append(tk.Label(frame_palavra, text='Clique no botão Iniciar e descubra a palavra escondida', border=1, bg='#ffe1cf'))
label_palavra[0].pack(fill=tk.X)

#show_word()

# frame para o alfabeto
frame_alfabeto = tk.Frame(root, pady=10)
frame_alfabeto.pack(fill=tk.BOTH, expand=True)

alfabeto = string.ascii_uppercase  # Obtém o alfabeto em letras maiúsculas
linhas = []  # Inicializa uma lista para armazenar as linhas
print(alfabeto)
alfabeto_lista = list(string.ascii_uppercase)

# Divide o alfabeto em linhas alternadas de seis e sete letras
linhas = []  # Inicializa uma lista para armazenar as linhas

for i in range(0, len(alfabeto), 13):
    print(i)
    linha = alfabeto[i:i+6]  # Linha com seis letras
    linhas.append(linha)
    if i + 6 < len(alfabeto):
        linha = alfabeto[i+6:i+13]  # Linha com sete letras
        linhas.append(linha)
print('linhas da lista',linhas)


button_dict={}
option= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

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
            stop()
            messagebox.showinfo('Uhuhu', 'Parabéns! Você acertou!', parent=root) 
            #stop()                               


        button_dict[x].grid_forget()

    for linha, sublista in enumerate(linhas):
        if i in sublista:
            posicao_na_sublista = sublista.index(i)
            posicao_na_lista = linha, posicao_na_sublista
            break  # Se encontrarmos a letra, podemos sair do loop
    
    button_dict[i]=tk.Button(frame_alfabeto, state='disabled',text=option[contador], command=clique_botao, foreground='#3C3B3B', width=4, height=2)
    button_dict[i].grid(row=posicao_na_lista[0], column=posicao_na_lista[1], ipadx=5, ipady=5, sticky=tk.EW)
    #button_dict[i].grid()
    
    contador += 1

# frame para os botoes
frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=8)

imagem_iniciar = Image.open('./imagens/start.png')
imagem_iniciar_reduzida = imagem_iniciar.resize((35,35), Image.ANTIALIAS)
icone_botao_iniciar = ImageTk.PhotoImage(imagem_iniciar_reduzida)

botao_iniciar = tk.Button(frame_botoes, text='Iniciar', command = start, image=icone_botao_iniciar, compound=tk.LEFT, border=0)
botao_iniciar.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5)

imagem_parar = Image.open('./imagens/stop.png')
imagem_parar_reduzida = imagem_parar.resize((35,35), Image.ANTIALIAS)
icone_botao_parar = ImageTk.PhotoImage(imagem_parar_reduzida)

botao_parar = tk.Button(frame_botoes, text='Parar', command=stop, state='disabled', image=icone_botao_parar, compound=tk.LEFT)
botao_parar.pack(side=tk.LEFT, ipadx=5, ipady=5, padx=5)

imagem_sair = Image.open('./imagens/exit.png')
imagem_sair_reduzida = imagem_sair.resize((35,35), Image.ANTIALIAS)
icone_botao_sair = ImageTk.PhotoImage(imagem_sair_reduzida)

botao_sair = tk.Button(frame_botoes, text='Sair', command=close, image=icone_botao_sair, compound=tk.LEFT)
botao_sair.pack(ipadx=5, ipady=5, padx=5)

root.mainloop()