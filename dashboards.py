import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Visão por sexo
# Tempo_Livre_Apos_Escola
# Falta_Escolar

df = pd.read_csv("lpor_explorer.csv", sep=",")
df = df.sort_values("Sexo")

selecao = st.sidebar.selectbox("Sexo", df["Sexo"].unique())

df_filtered = df[df["Sexo"] == selecao]
df_filtered

col1, col2 = st.columns(2)

# this one is separated by proportion or grouping
fig_sex = px.bar(df_filtered, x="Sexo", y="Tempo_Livre_Apos_Escola", color="Tempo_Livre_Apos_Escola", title="tempo livre depois da escola")
col1.plotly_chart(fig_sex, use_container_width=True)

fig_alcohol = px.bar(df_filtered, x="Sexo", y="Alcool_Fim_Semana", color="Alcool_Fim_Semana", title="alcool no fim de semana")
col2.plotly_chart(fig_alcohol, use_container_width=True)


