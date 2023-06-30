import streamlit as st
import pandas as pd

# streamlit run
meta = st.number_input("Meta do Dia dos Funcionarios: ", min_value=1)

dados_funcionarios = pd.DataFrame(
    {
        "Funcionario": [10, 15, 23, 55],
        "Produção": [70, 80, 75, 85],
        "Acertos": [65, 60, 70, 70],
    }
)
dados_funcionarios["Erros"] = dados_funcionarios["Produção"] - dados_funcionarios["Acertos"]

dados_metas = pd.DataFrame(
    {
        "Funcionario": dados_funcionarios["Funcionario"],
        "Meta": (dados_funcionarios["Produção"] / meta) * 100,
        "Taxa de Acerto": (dados_funcionarios["Acertos"] / dados_funcionarios["Produção"]) * 100
    }
)

dados, metas = st.tabs(["Dados", "Metas"])
with dados:
    st.header("Dados")
    tabela_dados = st.data_editor(
        dados_funcionarios,
        use_container_width=True,
        disabled=["Funcionario", "Erros"]
    )


total_produzido = tabela_dados["Produção"].sum()
dados_metas["% Total"] = (tabela_dados["Produção"] / total_produzido) * 100

with metas:
    st.header("Metas")
    st.dataframe(
        dados_metas,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Meta": st.column_config.ProgressColumn(
                "Porcentagem da meta",
                help="Porcentagem Já Feita Sobre a Meta Estabelecida",
                format="%.1f%%",
                min_value=0,
                max_value=100,
            ),
            "Taxa de Acerto": st.column_config.NumberColumn(
                "Taxa de Acerto",
                format="%.1f%%",
            ),
            "% Total": st.column_config.NumberColumn(
                help="Porcentagem Sobre a Produção Total",
                format="%.1f%%",
            )
        }
    )
st.header(f"Total Produzido: {total_produzido}")
st.dataframe(tabela_dados)