import streamlit as st
import pandas as pd
import plotly.express as px


# Carrega o arquivo CSV
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


# Função de um gráfico de linha interativo
def plot_chart(data, column_name):
    fig = px.line(data, x=data.index, y=column_name, title=f"Consumo de {column_name}")
    st.plotly_chart(fig)


# Função de construção do histograma
def plot_histogram(data, column_name):
    fig_hist = px.histogram(data, x=data.index, y=column_name, nbins=30, title=f"Consumo de {column_name}")
    st.plotly_chart(fig_hist)


def main():
    # Título do aplicativo
    st.markdown("<h1 style='text-align: center; color: green;'>Avaliação de Desempenho do Computador</h1>",
                unsafe_allow_html=True)

    # Upload do arquivo CSV
    uploaded_file = st.file_uploader("Faça o upload do arquivo CSV", type=['csv'])

    if uploaded_file is not None:
        data = load_data(uploaded_file)
        st.write("Dados Carregados:")
        st.write(data)

    # Sidebar para seleção de métrica
    options = ['CPU (%)', 'RAM (%)', 'Swap (%)']

    selected_options = st.sidebar.selectbox('Selecione as opções desejadas:', options)

    try:
        plot_histogram(data, selected_options)
        plot_chart(data, selected_options)
    except UnboundLocalError:
        st.error("Por favor, selecione um arquivo CSV")


if __name__ == "__main__":
    main()





