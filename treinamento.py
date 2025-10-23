ano = 2024
caminho_dados = f'/content/drive/MyDrive/AD/{ano}_Viagem.csv'

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

df_viagens = pd.read_csv(caminho_dados, encoding="Windows-1252", sep=";", decimal=",")

#formatação para duas casas após a vírgula
pd.set_option('display.float_format', '{:.2f}'.format)

#criando nova coluna de despesas
df_viagens['Despesas'] = df_viagens['Valor diárias'] + df_viagens['Valor passagens'] + df_viagens['Valor outros gastos']

#tratação de dados nulos na coluna de Cargo
df_viagens['Cargo'] = df_viagens['Cargo'].fillna('NÃO IDENTIFICADO')

df_viagens.groupby("Cargo")["Despesas"].max().reset_index().sort_values(by="Despesas", ascending=False)

#convertendo colunas de datas
df_viagens["Período - Data de início"] = pd.to_datetime(df_viagens["Período - Data de início"], format="%d/%m/%Y")
df_viagens["Período - Data de fim"] = pd.to_datetime(df_viagens["Período - Data de fim"], format="%d/%m/%Y")

#criando coluna de mês da viagem
df_viagens['Mês da viagem'] = df_viagens['Período - Data de início'].dt.month_name()

#formatação de data
pd.to_datetime(df_viagens["Período - Data de início"], format="%d/%m/%Y")

#criação de de coluna de dias de viagem
df_viagens['Dias de viagem'] = (df_viagens['Período - Data de fim'] - df_viagens['Período - Data de início']).dt.days

#criação da tabela Proporção de viagens
viagens_por_cargo = (df_viagens['Cargo'].value_counts(normalize=True) * 100).rename('Proporção de Viagens').reset_index()

df_viagens["Nome do órgão superior"].str.upper().str.replace('MINISTÉRIO', 'MIN.')

df_viagens.groupby("Cargo")['Despesas'].sum().reset_index().sort_values(by="Despesas", ascending=False)

filtro_mais_de_1_pct = viagens_por_cargo['Proporção de Viagens'] > 1

viagens_por_cargo[filtro_mais_de_1_pct]

filtro_eh_tecnico = viagens_por_cargo['Cargo'].str.startswith('TECNICO')

viagens_por_cargo[filtro_eh_tecnico]

viagens_por_cargo[filtro_eh_tecnico | filtro_mais_de_1_pct]

filtro_com_mais_de_10m_em_desp = df_viagens['Despesas'] > 100000.00

maiores_gastos = df_viagens[filtro_com_mais_de_10m_em_desp]

df_viagens.groupby(maiores_gastos['Cargo'])['Despesas'].sum().reset_index().sort_values(by="Despesas", ascending=False)

viagens_por_cargo = (df_viagens['Cargo'].value_counts(normalize=True) * 100).rename('Proporção de viagens').reset_index()

filtro_mais_de_1_pct = viagens_por_cargo['Proporção de Viagens'] > 1

viagens_por_cargo[filtro_mais_de_1_pct]

filtro_eh_tecnico = viagens_por_cargo['Cargo'].str.startswith('TECNICO')

viagens_por_cargo[filtro_eh_tecnico]

viagens_por_cargo[filtro_eh_tecnico | filtro_mais_de_1_pct]

gastos_medio_por_cargo = df_viagens.groupby('Cargo')['Despesas'].mean().reset_index()

gastos_medio_por_cargo[gastos_medio_por_cargo['Despesas'] > 10_000]

df_viagens['Cargo'].value_counts(dropna=False)

df_viagens.dropna(subset='Cargo')

df_viagens

# %% [markdown]
# 

# %%
(df_viagens
 .groupby('Cargo')
 .agg(despesa_media=('Despesas', 'mean'),
      duracao_media=('Dias de viagem', 'mean'),
      despesas_totais=('Despesas', 'sum'),
      destino_mais_frequente=('Destinos', pd.Series.mode),
      n_viagens=('Nome', 'count')
      )
 .reset_index()
 )

# %%
df_cargos = df_viagens['Cargo'].value_counts(normalize=True).reset_index()
df_cargos

# %%
df_viagens_consolidado = (df_viagens
 .groupby('Cargo')
 .agg(despesa_media=('Despesas', 'mean'),
      duracao_media=('Dias de viagem', 'mean'),
      despesas_totais=('Despesas', 'sum'),
      destino_mais_frequente=('Destinos', pd.Series.mode),
      n_viagens=('Nome', 'count')
      )
 .reset_index()
 )

cargos_relevantes = df_cargos.loc[df_cargos['proportion'] > 0.01, 'Cargo']

filtro = df_viagens_consolidado['Cargo'].isin(cargos_relevantes)

df_final = df_viagens_consolidado[filtro]

df_final = df_final.sort_values(by="n_viagens", ascending=False)

df_final.plot(x="Cargo", y="n_viagens", kind="bar")

fig, ax = plt.subplots(figsize=(16,6))

ax.barh(df_final['Cargo'], df_final['despesa_media'], color='#4AADB6')
ax.invert_yaxis()
ax.set_facecolor('#CFD8DC')

fig.suptitle('Despesa média em viagens por cargo público (2024)')

plt.figtext(0.75, 0.89,'Font: Portal da Transparência', fontsize=8)

plt.xlabel("Despesa Média")

plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.yticks(fontsize=8)

plt.show()

fig, ax = plt.subplots(figsize=(16, 6))

ax.scatter(df_viagens['Dias de viagem'], df_viagens['Despesas'], alpha=0.2)

ax.set_xlim(0, 100)
ax.set_ylim(0, 25_000)

filtro = df_viagens['Despesas'] > 175_000
df_viagens[filtro]

path_passagens = f'/content/drive/MyDrive/AD/{ano}_Passagem.csv'

df_passagens = pd.read_csv(path_passagens, encoding='Windows-1252', sep=';', decimal=',')

df_passagens[df_passagens['Identificador do processo de viagem'] == 20073775]

df_viagens.merge(df_passagens)

caminho_dados = f'/content/drive/MyDrive/AD/output/tabela_{ano}.xlsx'
df_final.to_excel(caminho_dados, index=False)# index=False

caminho_figura = f'/content/drive/MyDrive/AD/output/figura_{ano}.png'

fig, ax = plt.subplots(figsize=(16,6))

ax.barh(df_final['Cargo'], df_final['despesa_media'], color='#4AADB6')
ax.invert_yaxis()
ax.set_facecolor('#CFD8DC')

fig.suptitle('Despesa média em viagens por cargo público (2024)')

plt.figtext(0.75, 0.89,'Font: Portal da Transparência', fontsize=8)

plt.xlabel("Despesa Média")

plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.yticks(fontsize=8)

plt.savefig(caminho_figura, bbox_inches='tight') #método bbox_incher, serve basicamente para encaixar a figura