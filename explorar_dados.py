import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Configurando o matplotlib para exibir corretamente os caracteres especiais em português
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.style.use('ggplot')

#Carregando o dataset
df = pd.read_csv('dados_usuarios.csv', sep=',', encoding='latin1')

print(f'Dataset carregado com sucesso! Formato: {df.shape[0]} linhas x {df.shape[1]} colunas')
print(f'50 primeiras linhas do dataset: {df.head(50)}')
print(df.info())

#Verificando valores ausentes
#Contagem de valores ausentes por coluna
valores_ausentes = df.isnull().sum()
percentual_ausentes = (valores_ausentes / len(df)) / 100

print(f'Valores ausentes por coluna:')
for coluna, ausentes in valores_ausentes.items():
    print(f'{coluna}: {ausentes} valores ausentes ({percentual_ausentes[coluna]:.2f}%)')

#Visualizando valores ausentes
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
plt.title('Mapa de valores ausentes')
plt.tight_layout()
plt.savefig('valores_ausentes.png')
#O dataset não possui valores ausentes

#EXPLORANDO OS DADOS E REALIZANDO CONVERSÕES
print(f'\n\nEstatísticas descritivas: ')
print(df.describe(include='object'))

#valores únicos por coluna:
print('\n\nValores únicos por coluna')
for col in df.columns: #Percorrendo valores de cada coluna
    print(f'{col}> {len(df[col].unique())} valores únicos')

#Distribuição por Estado:
print('\n\nDistribuição por Estado:')
estado_counts = df['state'].value_counts() #Contagem de valores da coluna 'state' (estado)
print(estado_counts)

#Distribuição por mês
print('\n\nDistribuição por mês: ')
mes_counts = df['month'].value_counts() #Contagem de valores da coluna 'month' (mês)
print(mes_counts)

#Range de anos
print('\n\nRange de anos:')
print(f'De {df.year.min()} a {df.year.max()}') #Exibe o ano de início e fim da pesquisa 

#Convertendo a coluna date para datetime
print('\n\nConvertendo a coluna date para datetime')
df['date'] = pd.to_datetime(df['date'])
print(f"Tipo da coluna date após conversão: {df['date'].dtype}")

#Verificando a distribuição dos valores na coluna number:
print('\n\Estatísticas da coluna number:')
print(df['number'].describe())
print("Contagem de zeros na coluna number: ", (df['number'] == 0).sum())
print(f"Porcentagem de zeros: {(df['number'] == 0).sum() / len(df) * 100:.2f}%")

#Criando visualizações exploratórias:
#Histograma da coluna number (gráfico):
plt.figure(figsize=(10, 6))
plt.hist(df['number'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribuição dos valores na coluna number')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.tight_layout()
plt.savefig('histogramaNumber.png')
print('Histograma da coluna number salvo como imagem')

#Boxplot da coluna number por ano
plt.figure(figsize=(14, 8))
sns.boxplot(x='year', y='number', data=df)
plt.title("Distribuição da coluna number por ano")
plt.xlabel('Ano')
plt.ylabel('Valor')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('boxplot_numberPorAno.png')
print('Boxplot da coluna number por ano salvo como imagem')

#Salvando o dataFrame com as conversões realizadas
df.to_csv('dados_usuario_processados.csv', index=False)
print('Novo dataframe salvo')