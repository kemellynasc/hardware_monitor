import streamlit as st
import pandas as pd
import plotly.express as px
import os
import platform

# Carrega o arquivo CSV
@st.cache_data
def carregar_arquivo(caminho) -> pd.DataFrame:
    arquivo = pd.read_csv(caminho)
    return arquivo


# Função de um gráfico de linha interativo
def plotar_chart(data, metrica, altura_chart) -> None:
    fig = px.line(data, x=data.index, y=metrica)
    fig.update_layout(xaxis_title="Medições", yaxis_title="Percentual")
    fig.update_layout(yaxis=dict(range=[0, altura_chart]))
    st.plotly_chart(fig)


# Função de construção do histograma
def plotar_histograma(data, metrica, altura_hist) -> None:
    fig_hist = px.bar(data, x=data.index, y=metrica)
    fig_hist.update_traces(marker_color='rgb(225,136,17)', marker_line_color='rgb(8,48,107)',
                        marker_line_width=1.5, opacity=0.6)
    fig_hist.update_layout(yaxis=dict(range=[0, altura_hist]))
    st.plotly_chart(fig_hist)


# Função para calcular a média dos arquivos carregados
def calcular_media_arquivos(lista_arquivos: list):
    dfs = [carregar_arquivo(arquivo) for arquivo in lista_arquivos]
    df_concatenado = pd.concat(dfs)
    media = df_concatenado.mean()
    return media


# Função para carregar o histograma com a média dos dados
def plotar_histograma_media(media, altura_graf: int) -> None:
    eixo_y = media.tolist()
    fig = px.bar(media, x=media.index, y=eixo_y, labels={'x': 'Media das métricas', 'y': 'Percentual'})

    fig.update_traces(marker_color='rgb(156,202,0)', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, opacity=0.6)
    fig.update_layout(yaxis=dict(range=[0, altura_graf]))
    fig.update_layout(xaxis_title="Media das métricas", yaxis_title="Percentual")

    st.plotly_chart(fig)


def main():
    # Título do aplicativo
    st.markdown("<h1 style='text-align: center; color: green;'>Análise de Desempenho das Máquinas "
                "(Campus IFPE-Paulista)</h1>",
                unsafe_allow_html=True)

    # Upload do arquivo CSV
    arquivo_carregado = st.file_uploader("Faça o upload do arquivo CSV para análise individual", type=['csv'])

    if arquivo_carregado is not None:
        data = carregar_arquivo(arquivo_carregado)
        st.write("Arquivo Carregado: " + arquivo_carregado.name)
        st.dataframe(data, use_container_width=True)
        st.divider()

        # Parâmetros carregados no gráfico de linha
        percentual_ram = 'ram (%)'
        percentual_swap = 'swap (%)'
        percentual_cpu = 'cpu (%)'
        lista_parametros = [percentual_ram, percentual_swap, percentual_cpu]

        # Opção de selecionar um parâmetro para o histograma
        parametro = data.columns.tolist()
        parametro_selecionado = st.sidebar.selectbox('Selecione a métrica que deseja visualizar no histograma do arquivo carregado:', parametro)

        try:
            st.subheader("Gráfico do arquivo " + arquivo_carregado.name, divider='orange')
            plotar_chart(data, lista_parametros, 100)
            st.divider()
            st.subheader("Arquivo selecionado: " + arquivo_carregado.name + ". Exibindo dados de " + parametro_selecionado,
                        divider='orange')
            plotar_histograma(data, parametro_selecionado, 100)
        except UnboundLocalError:
            st.error("Por favor, selecione um arquivo CSV")

    # Seção para carregar arquivos de leitura e realizar o cálculo da média dos mesmos
    st.divider()
    arquivos = os.listdir(os.path.join(os.path.abspath('.'), platform.node()))
    arquivos_selecionados = st.sidebar.multiselect('Lista de arquivos para cálculo de média: ', arquivos)

    if arquivos_selecionados:
        try:
            media = calcular_media_arquivos([os.path.join(os.path.join(os.path.abspath('.'), platform.node()), arquivo) for arquivo in arquivos_selecionados])
            st.subheader("Média das métricas dos arquivos selecionados", divider='orange')
            plotar_histograma_media(media, 100)
        except ValueError:
            st.error("Por favor, selecione arquivos na barra lateral para exibir o histograma com a média das métricas.")


if __name__ == "__main__":
    main()
