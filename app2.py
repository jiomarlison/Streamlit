import streamlit as st
import datetime as dt
import sqlite3
import conectar

st.set_page_config(page_title="SISTEMA DE PONTO", layout="centered")

hoje = dt.datetime.now().strftime('%d/%m/%Y')
hora = dt.datetime.now().strftime('%H:%M:%S')
data_hora = dt.datetime.now().strftime('%d/%m/%Y-%H:%M:%S')
matriculas_validas = [11111, 22222, 33333]

opcoes_sidebar = ['Inserir Usuario', 'Ver Usuarios', 'Atualizar Informações', 'Deletar Usuario', 'Registar Ponto']
sidebar = st.sidebar.selectbox(label='Selecione a função', options=opcoes_sidebar)

if sidebar == 'Inserir Usuario':
    st.header('INSERIR NOVO USUARIO')
    nova_matricula = st.text_input('Digite a matricula')
    novo_nome = st.text_input('Digite o nome')


    def registar_funcionario():
        if not nova_matricula:
            st.warning('Digite uma matricula')
        elif not novo_nome:
            st.warning('Digite um nome')
        else:
            conectar.criar(nova_matricula, novo_nome)
            st.success('Registro de usuario feito com sucesso')


    st.button(label='Registar Novo Usuario', on_click=registar_funcionario)

elif sidebar == 'Ver Usuarios':
    st.header('USUARIOS')
    st.json(conectar.ler())

elif sidebar == 'Registar Ponto':
    def registrar_informacoes():
        if not matricula:
            st.warning('Digite a matricula')
        elif not senha:
            st.warning('Digite a senha')
        else:
            conectar.registrar_ponto(matriculas_validas, data_hora)
            st.success(f'Registro feito com sucesso - Matricula: {matricula}, Data: {hoje} - Hora: {hora}')
            st.text(conectar.registros_ponto(matricula))



    st.header('SISTEMA DE REGISTRO DE PONTO')
    st.subheader(f'Data: {hoje} - Hora: {hora}')
    st.divider()
    matricula = st.text_input(label='Digite sua mátricula')
    senha = st.text_input(label='Digite a senha', type='password')
    botao = st.button(label='Registrar', on_click=registrar_informacoes)

elif sidebar == 'Deletar Usuario':
    st.header('DELETAR USUARIO')
    deletar_matricula = st.text_input('Digite a Matricula')


    def deletar_usuario():
        conectar.deletar(deletar_matricula)


    st.button(label='Deletar', on_click=deletar_usuario)
