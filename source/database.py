import sqlite3

CRIA_TABELAS = """
create table if not exists categoria (
    id_categoria integer primary key autoincrement,
    nome varchar(40) not null
);

create table if not exists palavras (
    id_palavra integer primary key autoincrement,
    palavra varchar not null,
    categoria_id integer references categoria(id_categoria)
);
"""

def conecta_bd():
    conexao = sqlite3.connect('jogo_da_forca.db')
    return conexao

def cria_tabelas(conexao):
    cursor = conexao.cursor()
    cursor.executescript(CRIA_TABELAS)
    conexao.commit()

def lista_categorias(conexao):
    cursor = conexao.cursor()
    cursor.execute("select * from categoria order by id_categoria;")
    resultado = cursor.fetchall()
    return resultado

def insere_categoria(conexao, nome):
     cursor = conexao.cursor()
     cursor.execute('insert into categoria (nome) values (?)', (nome,))
     conexao.commit()

if __name__ == '__main__':
    conexao = conecta_bd()
    cria_tabelas(conexao)
    #insere_categoria(conexao,'carros')
    resultado = lista_categorias(conexao)
    for r in resultado:
        print(r)
    conexao.close()

