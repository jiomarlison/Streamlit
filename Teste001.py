import datetime
import streamlit as st
import pandas as pd
import numpy as np
import sqlite3

horarios = ["SEGUNDA_A_SEXTA", "SABADO", "DOMINGO_E_FERIADOS"]
pontos_saidas = ["KM-25", "PETROLINA"]
cabecalho = ["Veiculo", "Hora", "Rota"]
lista_rotas = []
ano_atual = datetime.datetime.today().year
conexao = sqlite3.connect("feriados.db")
cursor = conexao.cursor()

st.header("Segue abaixo todos os horarios")
st.subheader("Separados por Dia e Local de Saida")
for horario in horarios:
    for ponto in pontos_saidas:
        with st.expander(f":red[Horario:] ***{horario}*** :blue[Ponto de Saida:] ***{ponto}***", expanded=False):
            st.subheader('', anchor=f"{horario}_{ponto}")
            st.write(
                pd.DataFrame(
                    data=np.full(
                        (10, len(cabecalho)),
                        'a'
                    ),
                    index=[x for x in range(1, 11)],
                    columns=pd.MultiIndex.from_product([[horario], [ponto], cabecalho])
                ).to_html(),
                unsafe_allow_html=True
            )
            lista_rotas.append(pd.MultiIndex.from_product([[horario], [ponto]]))

feriados = pd.DataFrame(
    {
        "Dias do Ano": pd.date_range(
            start=f"{ano_atual}-01-01",
            end=f"{ano_atual}-12-31",
            freq="d"
        ),
        "Feriado": '',
        "Tipo": ''
    }
)

feriados["Feriado"].loc[feriados['Dias do Ano'] == f"02/11/{ano_atual}"] = "Finados"
feriados["Feriado"].loc[feriados['Dias do Ano'] == f"15/11/{ano_atual}"] = "Proclamação da Republica"
feriados["Feriado"].loc[feriados['Dias do Ano'] == f"25/12/{ano_atual}"] = "Natal"

st.sidebar.header("Login Administrador")
if (st.sidebar.text_input("Usuario") == st.secrets['autentificacao']['usuario'] and
        st.sidebar.text_input("Senha", type='password') == st.secrets['autentificacao']['senha']):
    feriados = pd.DataFrame(
        st.data_editor(
            feriados,
            column_config={
                'Dias do Ano': st.column_config.DateColumn(
                    format="DD/MM/YYYY",
                    disabled=True
                ),
                'Feriado': st.column_config.TextColumn(
                    max_chars=50,
                    help="**Digite o nome do feriado** :red[(EX: Carnaval, São João, Natal)]",
                ),
                'Tipo': st.column_config.TextColumn(
                    max_chars=50,
                    help="**Digite o(s) tipo(s) do(s) feriado(s)** :red[(EX: Nacional, Estadual, Municipal)]",
                )
            },
            use_container_width=True,
            hide_index=True,
            num_rows='dynamic',
            key="df_feriados"
        )
    )

feriados['Feriado'] = feriados['Feriado'].replace({None: ''})
feriados = feriados.loc[feriados['Feriado'] != '']
feriados.to_sql(name="feriados", con=conexao, if_exists='replace')
st.dataframe(
    feriados,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Dias do Ano": st.column_config.DateColumn(
            format="DD/MM/YYYY",
            disabled=True
        )
    }
)
st.download_button("Baixar CSV dos Feriados",
                   data=pd.DataFrame(feriados).set_index("Feriado").to_csv(),
                   file_name="Feriados.csv",
                   key="download_arquivo_feriados"
                   )

# st.dataframe(
#     pd.read_sql(
#         'SELECT * FROM feriados',
#         con=conexao,
#         # parse_dates={"Dias do Ano": {"format": "%d/%m/%y"}}
#     ),
#     use_container_width=True
# )

st.sidebar.header("Ir para")
for rota in lista_rotas:
    st.sidebar.markdown(f'* [{rota[0][0]} - {rota[0][1]}](#{rota[0][0]}_{rota[0][1]})')
