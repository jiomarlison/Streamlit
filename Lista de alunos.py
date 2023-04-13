import streamlit as st
import pandas as pd

st.set_page_config(page_title='DADOS ALUNOS', page_icon='🧑‍🎓', layout='wide')
st.title('**:red[VISUALIZAÇÃO DOS DADOS DAS TURMAS]**')

col1, col2, col3, col4 = st.tabs(['ENSINO FUNDAMENTAL', 'NOVO ENSINO MEDIO', 'ENSINO MEDIO', 'INFORMAÇÕES DE TODAS AS TURMAS'])

with col1:
    st.markdown('**:red[FAÇA O UPLOAD DA TABELA COM AS TURMAS DO FUNDAMENTAL]**')
    fundamental = st.file_uploader(label='', type=['xls', 'xlsx'], label_visibility='hidden', key='fundamental')
    if fundamental:
        df = pd.DataFrame(pd.read_excel(fundamental, header=5))
        colunas_turma = df.keys()
        turmas = pd.read_excel(fundamental, None).keys()
        turmas_fundamental = []
        for x in turmas:
            turmas_fundamental.append(x)
        turma_selecionada = st.selectbox('SELECIONE A TURMA PARA VER OS DADOS', options=turmas_fundamental)
        tabela = pd.read_excel(fundamental, header=5, sheet_name=None)
        st.dataframe(tabela[turma_selecionada].sort_values(by=['Nome']))

with col2:
    st.markdown('**:red[FAÇA O UPLOAD DA TABELA COM AS TURMAS DO NOVO ENSINO MÉDIO]**')
    novo_medio = st.file_uploader(label=' ', type=['xls', 'xlsx'], key='novo medio', label_visibility='hidden')
    if novo_medio:
        df = pd.DataFrame(pd.read_excel(novo_medio, header=5))
        colunas_turma = df.keys()
        turmas = pd.read_excel(novo_medio, None).keys()
        turmas_novo_medio = []
        for x in turmas:
            turmas_novo_medio.append(x)
        turma_selecionada = st.selectbox('SELECIONE A TURMA PARA VER OS DADOS', options=turmas_novo_medio)
        tabela = pd.read_excel(novo_medio, header=5, sheet_name=None)
        st.dataframe(tabela[turma_selecionada].sort_values(by=['Nome']))

with col3:
    st.markdown('**:red[FAÇA O UPLOAD DA TABELA COM AS TURMAS DO ENSINO MÉDIO]**')
    medio = st.file_uploader(label='', type=['xls', 'xlsx'], key='medio', label_visibility='hidden')
    if medio:
        df = pd.DataFrame(pd.read_excel(medio, header=5))
        colunas_turma = df.keys()
        turmas = pd.read_excel(medio, None).keys()
        turmas_medio = []
        for x in turmas:
            turmas_medio.append(x)
        turma_selecionada = st.selectbox('SELECIONE A TURMA PARA VER OS DADOS', options=turmas_medio)
        tabela = pd.read_excel(medio, header=5, sheet_name=None)
        st.dataframe(tabela[turma_selecionada].sort_values(by=['Nome']))

with col4:
    todas_turmas = []
    if fundamental:
        todas_turmas.extend(turmas_fundamental)

    if novo_medio:
        todas_turmas.extend(turmas_novo_medio)

    if medio:
        todas_turmas.extend(turmas_medio)

    st.write(todas_turmas)