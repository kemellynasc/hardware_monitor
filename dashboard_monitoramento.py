import streamlit as st
import pandas as pd
import datetime
import platform
import plotly.express as px
import os
import psutil

# Carrega o arquivo CSV
@st.cache_data
def upload_file(caminho: str) -> pd.DataFrame:
    arquivo = pd.read_csv(caminho)
    return arquivo

# Função para exibir as informações do computador que gerou os dados
# Pensar em como validar isso
def show_computer_info() -> None:
    # Nome do dispositivo
    device_name = platform.node()

    # Processador
    processor = platform.processor()

    # Nome do Sistema
    name_system = platform.system()

    # Quantidade de RAM
    total_ram = round(psutil.virtual_memory().total / (1024.0 ** 3), 2)  # Convertendo para GB e arredondando para 2 casas decimais

    st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>Informações da Máquina Que Gerou os Dados</h2>", unsafe_allow_html=True)
    row1_col1, row1_col2, row1_col3, row1_col4 = st.columns(4)
    row2_col1, row2_col2, row2_col3, row2_col4 = st.columns(4)
    row1_col1.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>Nome do Dispositivo</h3>", unsafe_allow_html=True)
    row1_col2.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>Processador do Dispositivo</h3>", unsafe_allow_html=True)
    row1_col3.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>Nome do Systema</h3>", unsafe_allow_html=True)
    row1_col4.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>RAM Total</h3>", unsafe_allow_html=True)
    row2_col1.markdown(f"<h4 style='text-align: center; font-size: 20px; margin-bottom: 20px;'>{device_name}</h4>", unsafe_allow_html=True)
    row2_col2.markdown(f"<h4 style='text-align: center; font-size: 20px; margin-bottom: 20px;'>{processor}</h4>", unsafe_allow_html=True)
    row2_col3.markdown(f"<h4 style='text-align: center; font-size: 20px; margin-bottom: 20px;'>{name_system}</h4>", unsafe_allow_html=True)
    row2_col4.markdown(f"<h4 style='text-align: center; font-size: 20px; margin-bottom: 20px;'>{total_ram}</h4>", unsafe_allow_html=True)
    
    st.divider()

# Função para exibir a tabela
def show_table(data: pd.DataFrame) -> None:
    st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>Tabela de Monitoramento de Recursos do Sistema</h2>", unsafe_allow_html=True)
    st.dataframe(data, use_container_width=True)
    st.write(
        """
        Essa tabela representa o monitoramento do sistema ao longo do tempo, com dados coletados em intervalos regulares. Cada linha corresponde a uma leitura de dados em um determinado momento, mostrando o percentual de uso de CPU, RAM, CACHE e SWAP. Esses dados são essenciais para avaliar o desempenho e a utilização dos recursos do sistema, permitindo identificar possíveis problemas e otimizar o uso dos recursos disponíveis.
        """
    )
    st.divider()

# Função para exibir o percentual de cada métrica
def show_avg_of_metrics(data: pd.DataFrame) -> None:
    st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>Média das Métricas Analisadas</h2>", unsafe_allow_html=True)
    cpu_avg = data['cpu (%)'].mean()
    ram_avg = data['ram (%)'].mean()
    swap_avg = data['swap (%)'].mean()
    cache_avg = data['cache (%)'].mean()

    # Exibindo a média das métricas
    col1, col2, col3, col4 = st.columns(4)
    col1.metric('RAM (%) AVG', round(ram_avg, 2))
    col2.metric('SWAP (%) AVG', round(swap_avg, 2))
    col3.metric('CACHE (%) AVG', round(cache_avg, 2))
    col4.metric('CPU (%) AVG', round(cpu_avg, 2))

    st.divider()

# Função para exibir os gráficos das métricas
def show_metrics_graph(data: pd.DataFrame) -> None:
    # Mostrando o gráfico
    st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>Gráfico de Percentual dos Recursos do Sistema</h2>", unsafe_allow_html=True)
    # st.header("Tabela de Monitoramento de Recursos do Sistema")
    st.line_chart(data)
    st.write("Esse gráfico apresenta a variação do percentual (eixo y) das métricas CPU, RAM, SWAP e CACHE ao longo de um intervalo de tempo (eixo x).")
    st.divider()

    fig_cpu_by_index = px.area(
        data['cpu (%)'],
        title="<b>Percentual da CPU</b>".upper(),
        x=data['cpu (%)'].index,
        y="cpu (%)",
        orientation="v",
        color_discrete_sequence=["green"] * len(data['cpu (%)']),
    )

    fig_ram_by_index = px.area(
        data['ram (%)'],
        title="<b>Percentual da RAM</b>".upper(),
        x=data['ram (%)'].index,
        y="ram (%)",
        orientation="v",
        color_discrete_sequence=["turquoise"] * len(data['cpu (%)']),
    )

    fig_swap_by_index = px.area(
        data['swap (%)'],
        title="<b>Percentual da SWAP</b>".upper(),
        x=data['swap (%)'].index,
        y="swap (%)",
        orientation="v",
        color_discrete_sequence=["#FF4B4B"] * len(data['swap (%)']),
    )

    fig_cache_by_index = px.area(
        data['cache (%)'],
        title="<b>Percentual da CACHE</b>".upper(),
        x=data['cache (%)'].index,
        y="cache (%)",
        orientation="v",
        color_discrete_sequence=["gray"] * len(data['cache (%)']),
    )
    
    # Definindo duas colunas para exibir os gráficos
    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)
    row3_col1, row3_col2 = st.columns(2)
    row4_col1, row4_col2 = st.columns(2)
    row5_col1, row5_col2 = st.columns(2)
    row6_col1, row6_col2 = st.columns(2)
    
    row1_col1.plotly_chart(fig_cpu_by_index, use_container_width=True)
    row2_col1.write("variação do percentual de cpu ao longo de um intervalo de tempo")
    row1_col2.plotly_chart(fig_ram_by_index, use_container_width=True)
    row2_col2.write("variação do percentual de memória ram ao longo de um intervalo de tempo")
    st.divider()
    row3_col1.plotly_chart(fig_cache_by_index, use_container_width=True)
    row4_col1.write("variação do percentual de memória cache ao longo de um intervalo de tempo")
    row3_col2.plotly_chart(fig_swap_by_index, use_container_width=True)
    row4_col2.write("variação do percentual de memória swap ao longo de um intervalo de tempo")
    
    # Colocar aqui os gráficos de disco;
    
    # Obtendo a correlação das métricas
    correlacao_metrics = data.corr()

    # fig = px.imshow(correlacao_metrics, title='Correlação entre CPU, RAM, SWAP e CACHE')
    fig = px.imshow(correlacao_metrics)

    st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>Gráfico de Correlação entre CPU, RAM, SWAP e CACHE</h2>", unsafe_allow_html=True)

    st.plotly_chart(fig, use_container_width=True)
    st.write("-1 -> significa que à medida que uma métrica aumenta, a outra diminui")
    st.write(" 0 -> significa que não há correlação entre as métricas")
    st.write(" 1 -> significa que à medida que uma métrica aumenta, a outra aumenta")
    st.write(
        """
        Assim, valores que se aproximam do -1 indicam uma relação de correlação inversa. 
        valores que se aproximam do 1 indicam uam correlação direta e valores que se aproximam
        do 0 indicam uma baixa correlação.
        """
    )
    st.divider()

# Função para calcular a média dos arquivos carregados
def calculate_avg_metrics(lista_arquivos: list):
    dfs = [upload_file(arquivo) for arquivo in lista_arquivos]
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

    st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>Gráfico da Média de Cada Recurso do Sistema</h2>", unsafe_allow_html=True)
    st.plotly_chart(fig)
    st.divider()

# Função para Exibir Dados Do Disco
def show_disk_data(data: pd.DataFrame) -> None:
    try:
        disk_transfer_rate = data['taxa de transferencia de disco (GB/s)'].mean() #(disk_info.read_bytes + disk_info.write_bytes)/(1024**3)

        disk_latency = data['taxa de latencia de disco(seg)'].mean() #(disk_info.read_time + disk_info.write_time)/1000.0
        
        st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>Informações do Disco da Máquina Que Gerou os Dados</h2>", unsafe_allow_html=True)
        row1_col1, row1_col2 = st.columns(2)
        row2_col1, row2_col2 = st.columns(2)
        row1_col1.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>Taxa de Transferência</h3>", unsafe_allow_html=True)
        row1_col2.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>Latência do Disco</h3>", unsafe_allow_html=True)
        row2_col1.markdown(f"<h4 style='text-align: center; font-size: 25px; margin-bottom: 20px;'>{round(disk_transfer_rate, 2)} GB/s</h4>", unsafe_allow_html=True)
        row2_col2.markdown(f"<h4 style='text-align: center; font-size: 25px; margin-bottom: 20px;'>{round(disk_latency, 2)} segundos</h4>", unsafe_allow_html=True)
    except:
        st.error("Não é possível exibir as métricas de Disco")
    st.divider()

def show_footer_page():
    st.markdown("""
                    <style>
                        .st-emotion-cache-cnbvxy li {
                            margin: 10px auto;
                            padding: 0px;
                            font-size: 20px;
                            list-style: none;
                        }
                        .st-emotion-cache-cnbvxy a {
                            color: white;
                            text-decoration: none;
                            margin-left: 50px;
                        }
                        
                        ul {
                            list-style: none;
                        }
                        /*
                        .st-emotion-cache-cnbvxy li:hover {
                            border: 2px solid crimson;
                            
                        }*/
                        
                        .st-emotion-cache-cnbvxy a:hover {
                            color: black;
                            background: white;
                        }
                        
                        .container {
                            display: flex;
                            justify-content: center;
                        }
                        .equipe {
                            text-align: center;
                            font-size: 40px;
                            color: green;
                        }
                    </style>
                    <h3 class="equipe">Equipe Desenvolvedora:</h3>
                    <div class="container">
                        <ul>
                            <li><a target="_blank" href="https://github.com/fhplira"><b>Fernanda Helen de Paula Lira - IFPE Paulista</b></a></li>
                            <li><a target="_blank" href="https://github.com/Neto-Pereira25"><b>José Pereira da Silva Neto - IFPE Recife</b></a></li>
                            <li><a target="_blank" href="https://github.com/kemellynasc"><b>Kemelly Nascimento - IFPE Paulista</b></a></li>
                            <li><a target="_blank" href="https://github.com/nathalialimaa"><b>Nathália de Lima Santos - IFPE Recife</b></a></li>
                            <li><a target="_blank" href="https://lattes.cnpq.br/5301729624897209"><b>Eraldo Dias - IFPE Paulista</b></a></li>
                            <li><a target="_blank" href="https://gitlab.com/alsmoreira"><b>Anderson Luiz Souza Moreira - IFPE Recife</b></a></li>
                            <li><a target="_blank" href="http://lattes.cnpq.br/7139685024425123"><b>Marco Antônio de Oliveira Domingues - IFPE Recife</b></a></li>
                        </ul>
                    </div>
                """, unsafe_allow_html=True)
    st.divider()
    st.markdown(f"""<footer style='text-align: center; color: green; font-size: 24px;'><b> © {datetime.datetime.now().year} -  Todos os Direitos Reservados ao GPADS </b></footer>""", unsafe_allow_html=True)

def main():
    # configurações da página
    st.set_page_config(
        layout="wide",
        page_title="Dashboard Análise de Desempenho",
        page_icon=":bar_chart:",
        initial_sidebar_state="auto"
    )
    
    # Título do aplicativo
    st.markdown("<h1 style='text-align: center; color: green;'> 📊 &mdash; Análise de Desempenho das Máquinas (Campus IFPE-Paulista)</h1>", unsafe_allow_html=True)
    st.divider()
    
    try:
        #### Carregando os Dados ####
        arquivos = os.listdir(os.path.join(os.path.abspath('.'), platform.node()))
        arquivos_selecionados = st.sidebar.multiselect('Lista de arquivos para cálculo de média: ', arquivos)

        # Criando lista de arquivos com caminho completo
        list_arq = [os.path.join(os.path.join(os.path.abspath('.'), platform.node()), arquivo) for arquivo in arquivos_selecionados]
    
    
        dfs = [upload_file(arquivo) for arquivo in list_arq]
        df_concat = pd.concat(dfs)
    except:
        st.error("Selecione pelo menos um arquivo")
    
    # Exibindo os Dados
    try:
        if len(df_concat) != 0:
            show_computer_info()
            
            show_table(df_concat)
            
            show_avg_of_metrics(df_concat)
            
            show_metrics_graph(df_concat)
            
            # Exibir Métricas de Disco
            # # Taxa de Leitura e Escrita em Disco, 
            show_disk_data(df_concat)
            
            # st.divider()
            
            media = calculate_avg_metrics(list_arq)
            plotar_histograma_media(media, 100)
    except:
        st.error("Não foi possível exibir o dashboard")
    
    # Footer
    show_footer_page()

if __name__ == "__main__":
    main()