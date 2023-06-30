import streamlit as st
import pandas as pd
# streamlit run '.\Lista de alunos.py'
st.set_page_config(page_title='DADOS ALUNOS', page_icon='🧑‍🎓', layout='wide')
st.title('**:red[VISUALIZAÇÃO DOS DADOS DAS TURMAS]**')

fundamental, informacoes_turmas, todos_fundamental = st.tabs(['ENSINO FUNDAMENTAL', 'INFORMAÇÕES TURMAS', 'TODOS ALUNOS FUNDAMENTAL'])

with fundamental:
    def lista_fundamental():
        alunos_fundamental = []
        for x in turmas:
            df = pd.DataFrame(pd.read_excel(fundamental, header=5, sheet_name=x))
            df = df.drop(columns=['Procedência modalidade/curso'])
            df['Turma'] = f'{x[-4]} ANO - {x[-1]}'
            alunos_fundamental.append(df)
        dataframe_fundamental = pd.concat(alunos_fundamental).dropna()
        return dataframe_fundamental
    st.markdown('**:red[FAÇA O UPLOAD DA TABELA COM AS TURMAS DO FUNDAMENTAL]**')
    fundamental = st.file_uploader(label='', type=['xls', 'xlsx'], label_visibility='hidden', key='fundamental')

    if fundamental:
        turmas = pd.read_excel(fundamental, None).keys()
        turma_selecionada = st.radio('**:red[SELECIONE A TURMA PARA VER OS DADOS]**', options=turmas, horizontal=True, key=1)
        df = pd.DataFrame(pd.read_excel(fundamental, header=5, sheet_name=turma_selecionada))
        df = df.drop(columns=['Procedência modalidade/curso'])
        colunas_turma = df.keys()
        filtro = st.radio('**:red[FILTRAR POR]**', options=colunas_turma, horizontal=True, key=2)
        df = df.sort_values(by=[filtro])
        st.dataframe(data=df, width=1500)

with informacoes_turmas:
    todas_turmas = []
    if fundamental:
        todas_turmas.extend(turmas)
    st.write(todas_turmas)

with todos_fundamental:
    filtro_todos = st.radio('**:red[FILTRAR POR]**', options=lista_fundamental().keys(), horizontal=True)
    st.header('**TODOS OS ALUNOS DO FUNDAMENTAL**')
    st.dataframe(data=lista_fundamental().sort_values(by=[filtro_todos]), width=1500)

    @st.cache_data
    def planilha(df):
        return df.to_csv(index=False).encode('utf-8')
    planilha_alunos = planilha(lista_fundamental())
    st.download_button(label="Baixar Lista", data=planilha_alunos, file_name='Lista Fundamental.csv')