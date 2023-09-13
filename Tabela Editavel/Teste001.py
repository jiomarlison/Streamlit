import streamlit as st
import pandas as pd
import numpy as np

horarios = ["SEGUNDA_A_SEXTA", "SABADO", "DOMINGO_E_FERIADOS"]
pontos_saidas = ["KM-25", "PETROLINA"]
cabecalho = ["Veiculo", "Hora", "Rota"]
lista_rotas = []
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

st.sidebar.header("Ir para")
for rota in lista_rotas:
    st.sidebar.markdown(f'* [{rota[0][0]} - {rota[0][1]}](#{rota[0][0]}_{rota[0][1]})')
