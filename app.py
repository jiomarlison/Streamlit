import streamlit as st
import pandas as pd

lista_colunas = []
lista_abas = []

arquivo = st.file_uploader('Envie o arquivo', ['xls', 'xlsx'])

planilha = pd.read_excel(arquivo)
abas = pd.read_excel(arquivo, None).keys()

for x in planilha.keys(), :
    lista_colunas.append(x)
for y in abas:
    lista_abas.append(y)

st.write(f'Abas: {lista_abas}')
st.write(f'Colunas: {lista_colunas}')
st.dataframe(planilha)