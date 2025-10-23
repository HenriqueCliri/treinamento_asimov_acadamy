Análise de Despesas de Viagens (Treinamento)
Este projeto é um notebook de análise de dados, desenvolvido como parte de um treinamento, focado em explorar e visualizar dados de despesas de viagens de servidores públicos, utilizando dados do ano de 2024.

O script realiza o carregamento, tratamento, análise e visualização dos dados, culminando na exportação de uma tabela consolidada e um gráfico com os principais insights.

📈 O que o script faz
O fluxo de trabalho principal do script pode ser resumido nas seguintes etapas:

Carregamento dos Dados:

Lê dois arquivos CSV principais: 2024_Viagem.csv e 2024_Passagem.csv.

Os arquivos são lidos com encoding Windows-1252, separador ; e decimal ,.

Limpeza e Engenharia de Features:

Cria uma coluna Despesas somando os valores de diárias, passagens e outros gastos.

Trata valores nulos na coluna Cargo, substituindo-os por "NÃO IDENTIFICADO".

Converte as colunas de data (Período - Data de início e Período - Data de fim) para o formato datetime.

Cria novas colunas: Mês da viagem e Dias de viagem (calculado a partir das datas de início e fim).

Análise Exploratória e Agregação:

Realiza diversas agregações (groupby) para entender os dados, como:

Despesa máxima, total e média por Cargo.

Contagem e proporção de viagens por Cargo.

Cria um DataFrame consolidado (df_viagens_consolidado) que agrupa por Cargo e calcula:

despesa_media

duracao_media

despesas_totais

destino_mais_frequente

n_viagens (número de viagens)

Filtragem e Foco:

Filtra a análise para focar apenas em "cargos relevantes", definidos como aqueles que representam mais de 1% do total de viagens.

Visualização de Dados:

Gera um gráfico de barras horizontais (barh) que mostra a Despesa média em viagens por cargo público (2024).

Gera um gráfico de dispersão (scatter) para visualizar a relação entre Dias de viagem e Despesas.

Exportação dos Resultados:

Salva o DataFrame final e filtrado (df_final) em um arquivo Excel (tabela_2024.xlsx).

Salva o gráfico de barras horizontais em um arquivo de imagem PNG (figura_2024.png).

🛠️ Tecnologias Utilizadas
Python 3

Pandas: Para manipulação e análise dos dados.

Matplotlib: Para a criação das visualizações.

Google Colab / Google Drive: O ambiente de execução (inferido pelos caminhos /content/drive/).

🚀 Como Executar
Este script foi projetado para ser executado em um ambiente Google Colab.

Pré-requisitos:

Tenha os arquivos de dados 2024_Viagem.csv e 2024_Passagem.csv em seu Google Drive.

O script espera que os arquivos estejam na seguinte pasta: MyDrive/AD/.

O script também salvará os resultados na pasta MyDrive/AD/output/. Certifique-se de que ela exista.

Estrutura de Pastas Esperada no Google Drive:

/MyDrive/
└── AD/
    ├── 2024_Viagem.csv
    ├── 2024_Passagem.csv
    └── output/
        (aqui serão criados os arquivos de saída)
Montar o Google Drive: Adicione esta célula no início do seu notebook para permitir o acesso aos arquivos:

Python

from google.colab import drive
drive.mount('/content/drive')
Executar o Notebook: Execute todas as células do notebook em ordem.

📊 Saídas (Outputs)
Ao final da execução, o script gerará dois arquivos na pasta /content/drive/MyDrive/AD/output/:

tabela_2024.xlsx: Uma planilha Excel contendo a tabela de dados consolidada e filtrada por cargos relevantes.

figura_2024.png: Uma imagem do gráfico de barras horizontais mostrando a despesa média por cargo.