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

create table if not exists jogadores(
    id_jogador integer primary key autoincrement, 
    nome varchar not null,
    pontos integer not null
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
    categorias = cursor.fetchall()
    return categorias

def insere_categoria(conexao, nome):
     cursor = conexao.cursor()
     cursor.execute('insert into categoria (nome) values (?)', (nome,))
     conexao.commit()

def lista_palavras(conexao, categoria):
    cursor = conexao.cursor()
    cursor.execute("select palavra from palavras join categoria on(id_categoria = categoria_id) where categoria.nome = ?;", (categoria,))
    palavras = cursor.fetchall()
    return palavras

def existe_jogador(conexao, nome):
    cursor = conexao.cursor()
    cursor.execute("select count(*) from jogadores where lower(nome) = ?;", (nome.strip().lower(),))
    total = cursor.fetchall()
    print('total', total[0][0])
    if total[0][0] == 0:
        return False 
    else: 
        return True
   

def insere_jogador(conexao, nome):
    cursor = conexao.cursor()
    cursor.execute("insert into jogadores (nome, pontos) values (?, 0);", (nome,))
    conexao.commit()
    print('jogador cadastrado')

def atualiza_pontos(conexao, nome, pontos):
    cursor = conexao.cursor()
    cursor.execute('select pontos from jogadores where nome = ?', (nome,))
    pontos_armazenados = cursor.fetchall()

    if pontos > pontos_armazenados[0][0]:
        cursor.execute("update jogadores set pontos = ? where nome = ?;", (pontos, nome))
        conexao.commit()

    print('***** pontos atualizados!')

def get_recorde(conexao):
    cursor = conexao.cursor()
    cursor.execute("select nome, max(pontos) from jogadores where pontos = (select max(pontos) from jogadores) group by nome order by 2 desc;")
    return cursor.fetchall()


if __name__ == '__main__':
    conexao = conecta_bd()
    cria_tabelas(conexao)
    #insere_categoria(conexao,'carros')
    resultado = lista_categorias(conexao)
    for r in resultado:
        print(r)
    palavras = lista_palavras(conexao, 'frutas')  
    print(palavras)
    for palavra in palavras:
        print(palavra)  
    res = existe_jogador(conexao, 'Rangel')
    print(res)

    #atualiza_pontos(conexao, 'rangel', 37)

    # consulta o recorde de pontos
    recorde = get_recorde(conexao)

    if len(recorde) > 1:
        print(recorde)
    elif len(recorde) == 0:
        print('Recorde: 0')
    else:
        print(f'Recorde: {recorde[0][1]} ({recorde[0][0].title()})')
    
    conexao.close()

