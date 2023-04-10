import sqlite3


def criar(matricula, nome):
    conexao = sqlite3.connect('sistema_de_ponto.db')
    cursor = conexao.cursor()

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS funcionarios(ID integer primary key autoincrement, MATRICULA integer, NOME text)')
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS registro_ponto(ID integer primary key autoincrement, MATRICULA int, REGISTRO text)')
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS loggin(ID integer primary key autoincrement, MATRICULA int, SENHA text)')

    dados = [matricula, nome]
    cursor.execute('INSERT INTO funcionarios(MATRICULA, NOME) values(?, ?)', dados)

    conexao.commit()
    cursor.close()
    conexao.close()


def ler():
    conexao = sqlite3.connect('sistema_de_ponto.db')
    cursor = conexao.cursor()

    resultado = cursor.execute('SELECT rowid, MATRICULA, NOME FROM funcionarios').fetchall()

    cursor.close()
    conexao.close()

    return resultado


def registros_ponto(matricula):
    conexao = sqlite3.connect('sistema_de_ponto.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT rowid, MATRICULA, REGISTRO FROM registro_ponto').fetchall()
    cursor.close()
    conexao.close()


def atualizar():
    conexao = sqlite3.connect('sistema_de_ponto.db')
    cursor = conexao.cursor()

    cursor.close()
    conexao.close()

    pass


def deletar(matricula):
    conexao = sqlite3.connect('sistema_de_ponto.db')
    cursor = conexao.cursor()

    cursor.execute(f'DELETE FROM funcionarios WHERE MATRICULA = {matricula}')

    conexao.commit()
    cursor.close()
    conexao.close()


def registrar_ponto(matricula, registro):
    conexao = sqlite3.connect('sistema_de_ponto.db')
    cursor = conexao.cursor()

    dados = [matricula, registro]
    cursor.execute('INSERT INTO registro_ponto(MATRICULA, REGISTRO) values(?, ?)', dados)

    conexao.commit()
    cursor.close()
    conexao.close()

