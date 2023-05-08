import streamlit as st

st.set_page_config(layout='wide', page_title='FRUIT FLOW SISTEMAS')
st.title(':teal[**Fruit Flow**]')

st.text_input(label=':blue[**Usuário**]',
              placeholder='Nome de usuário ou Email')
st.text_input(label=':blue[**Senha**]',
              placeholder='Digite sua senha',
              type="password")
st.button(label='Acessar')


adicionar, ver, atualizar, remover = st.columns(4)
with adicionar:
    st.header("ADICIONAR")