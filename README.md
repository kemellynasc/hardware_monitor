# Dashboard de Análise de Desempenho

Este projeto consiste em um dashboard interativo desenvolvido com Streamlit para análise de desempenho de máquinas. O dashboard permite o upload de arquivos CSV contendo dados de monitoramento de recursos do sistema, como CPU, RAM, SWAP e CACHE. Além disso, exibe gráficos e informações detalhadas sobre o desempenho das máquinas.

## Funcionalidades

- **Upload de Arquivos CSV**: Permite o upload de arquivos CSV contendo dados de monitoramento.
- **Informações da Máquina**: Exibe informações sobre o dispositivo que gerou os dados, como nome, processador, sistema operacional e quantidade de RAM.
- **Tabela de Dados**: Exibe uma tabela com os dados de monitoramento.
- **Médias das Métricas**: Calcula e exibe a média das métricas CPU, RAM, SWAP e CACHE.
- **Gráficos de Métricas**: Apresenta gráficos das variações das métricas ao longo do tempo.
- **Gráficos de Correlação**: Mostra a correlação entre as métricas CPU, RAM, SWAP e CACHE.
- **Informações do Disco**: Exibe dados sobre a taxa de transferência e latência do disco.
- **Equipe de Desenvolvimento**: Mostra informações sobre a equipe de desenvolvimento do projeto.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git

2. Navegue até o diretório do projeto:
   cd nome-do-repositorio
   
3. Crie um ambiente virtual e ative-o:
   python -m venv venv
  source venv/bin/activate  # Para Linux/Mac
  venv\Scripts\activate  # Para Windows

4. Instale as dependências:
   pip install -r requirements.txt

## Uso 
Execute o script principal: 
streamlit run nome_do_script.py
Acesse o dashboard através do navegador, usando o endereço fornecido pelo Streamlit (geralmente http://localhost:8501).

## Estrutura do Projeto

`main.py`: Script principal que contém a lógica do dashboard.
`requirements.txt`: Lista de dependências necessárias para rodar o projeto.
`data/` : Diretório onde os arquivos CSV devem ser armazenados.

## Equipe de Desenvolvimento

- Fernanda Helen de Paula Lira
- José Pereira da Silva Neto
- Kemelly Nascimento
- Nathália de Lima Santos
- Eraldo Coelho Dias Junior
- Anderson Luiz Souza Moreira
- Marco Antônio de Oliveira Domingues

