# Análise de Despesas de Viagens (Projeto de Treinamento)

## 🎯 Objetivo

Analisar dados de viagens de servidores públicos (referentes a 2024) para identificar padrões de gastos, duração e frequência por cargo. Este projeto foi desenvolvido como parte de um treinamento em Análise de Dados com Python.

## ✨ Principais Funcionalidades

- **Carregamento e Limpeza:** Lê arquivos `.csv` de viagens, trata dados ausentes (`NaN`) e formata colunas de data e valores monetários.
- **Engenharia de Features:** Cria novas colunas para análise, como `Despesas` (soma dos gastos), `Dias de viagem` e `Mês da viagem`.
- **Análise Agregada:** Utiliza `groupby` para consolidar dados por `Cargo`, calculando métricas como despesa média, despesa total, duração média e número de viagens.
- **Visualização:** Gera gráficos com `matplotlib` para ilustrar os resultados, incluindo um gráfico de barras da despesa média por cargo.
- **Exportação:** Salva a tabela de análise final (`df_final`) em um arquivo Excel (`.xlsx`) e o gráfico principal em uma imagem (`.png`).

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Pandas:** Para toda a manipulação e análise dos DataFrames.
- **Matplotlib:** Para a criação dos gráficos.
- **Google Colab:** Ambiente de desenvolvimento (inferido pelo uso do Google Drive).

## 🚀 Como Executar

### 1. Pré-requisitos

- Acesso a um ambiente Python (como Google Colab ou Jupyter Notebook).
- Os arquivos de dados de origem:
    - `2024_Viagem.csv`
    - `2024_Passagem.csv`

### 2. Execução

1.  **Montar o Google Drive (se estiver no Colab):**
    ```python
    from google.colab import drive
    drive.mount('/content/drive')
    ```
2.  **Definir o Ano:**
    Certifique-se de que a variável `ano` esteja correta no início do script:
    ```python
    ano = 2024
    ```
3.  **Executar o Script:**
    Rode todas as células do notebook.

## 📊 Saídas do Projeto

O script gerará dois arquivos principais na pasta `/content/drive/MyDrive/AD/output/`:

1.  `tabela_2024.xlsx`: Uma planilha Excel com os dados consolidados da análise por cargo.
2.  `figura_2024.png`: A imagem do gráfico de barras "Despesa média em viagens por cargo público (2024)".
