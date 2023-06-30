import streamlit as st
import datetime
import numpy as np

# PEGA TODOS OS ANOS A PARTIR DE 100 ANOS ATRAS ATÉ O ANO ATUAL
datas = np.arange(np.datetime64(f'{int(str(datetime.datetime.today().year)) - 100}'),
                  np.datetime64(f'{datetime.date.today().year + 1}'))
anos = [int(str(anos)) for (anos) in datas]

st.markdown("**Campos com :red[*] são obrigatórios**")

nome = st.text_input("**Nome:red[*]**", placeholder="Digite seu nome")
sobrenome = st.text_input("**Sobrenome:red[*]**", placeholder="Digite seu sobrenome")
telefone = st.text_input("**Telefone:red[*]**", placeholder="Digite seu telefone")

st.markdown("**Selecione sua data de nascimento:red[*]**")
dia, mes, ano = st.columns(3)
with dia:
    dia_selecionado = st.number_input("Dia", min_value=1, max_value=31, value=1)
with mes:
    mes_selecionado = st.number_input("Mês", min_value=1, max_value=12, value=1)
with ano:
    ano_selecionado = st.number_input("Ano", min_value=min(anos), max_value=max(anos), value=max(anos))
try:
    data_nascimento = st.date_input("DATA", datetime.date(ano_selecionado, mes_selecionado, dia_selecionado),
                                    disabled=True)
except ValueError:

    st.warning("**Data Invalida**")


def dados():
    st.success("**Tudo Certo**")


email = st.text_input("**Digite seu email:red[*]**", placeholder="exemplo@gmail.com")
try:
 botao_cadastras = st.button("Cadastrar",
                            disabled=(False if nome and sobrenome and telefone and data_nascimento and email else True),
                            on_click=dados)
except NameError:
    st.error("**Preencha todos os campos corretamente!**")
