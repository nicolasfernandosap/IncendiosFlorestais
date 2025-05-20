import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re

#Configurando o matplotlib para exibir corretamente os caracteres especiais em português
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.style.use('ggplot')

#Carregando o dataset
df = pd.read_csv('dados_usuario_processados.csv', sep=',', encoding='latin1')

#Convertendo a coluna date para datetime novamente pois foi salva como string novamente no .csv
df['date'] = pd.to_datetime(df['date'])

print(f"Padronizando nomes de Estados: ")
#Mapeamento para padronizar nomes de Estados:

estados_map = {
    'Acre': 'AC',
    'Alagoas': 'AL',
    'Amapa': 'AP',
    'Amazonas': 'AM',
    'Bahia': 'BA',
    'Ceara': 'CE',
    'Distrito Federal': 'DF',
    'Espirito Santo': 'ES',
    'Goias': 'GO',
    'Maranhao': 'MA',
    'Mato Grosso': 'MT',
    'Minas Gerais': 'MG',
    'Pará': 'PA',
    'Paraiba': 'PB',
    'Pernambuco': 'PE',
    'Piau': 'PI',
    'Rio': 'RJ',
    'Rondonia': 'RO',
    'Roraima': 'RR',
    'Santa Catarina': 'SC',
    'Sao Paulo': 'SP',
    'Sergipe': 'SE',
    'Tocantins': 'TO'
}

#Aplicando o mapeamento
df['state_code'] = df['state'].map(estados_map)
print('Estados entes da padronização:')
print(df['state'].value_counts().head())
print('Estados após a padronização:')
print(df['state_code'].value_counts().head())

#Padronizando nomes de meses:
print('Padronizando nomes de meses:')
meses_map = {
    'Janeiro': 1,
    'Fevereiro': 2,
    'Março': 3,
    'Abril': 4,
    'Maio': 5,
    'Junho': 6,
    'Julho': 7,
    'Agosto': 8,
    'Setembro': 9,
    'Outubro': 10,
    'Novembro': 11,
    'Dezembro': 12
}

#Aplicando o mapeamento
df['month_num'] = df['month'].map(meses_map)
df = df.dropna(subset=['month_num'])
print("Meses antes da padronização: ")
print(df['month'].value_counts().head())
print("Meses após a padronização: ")
print(df['month_num'].value_counts().head())

#Criando uma coluna de data completa (ano-mes-dia)
df['full_date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month_num'].astype(int).astype(str).str.zfill(2) + '-01', format='%Y-%m-%d')

print("Primeiras 5 linhas com colunas de datas completas: ")
print(df[['year', 'month', 'month_num', 'full_date']].head())

#Tratando valores zeros na coluna number
zeros_count = (df['number'] == 0).sum()
print(f"Número de zeros na coluna number: {zeros_count} ({zeros_count/len(df)*100:.2}%)")

#Os zeros podem representar ausência real de eventos, por isso mantidos
#Mapeamento de Estados para regiões
regioes_map = {
    'AC': 'Norte', 'AP': 'Norte', 'AM': 'Norte', 'PA': 'Norte', 'RO': 'Norte', 'RR': 'Norte', 'TO': 'Norte',
    'AL': 'Nordeste', 'BA': 'Nordeste', 'CE': 'Nordeste', 'MA': 'Nordeste', 'PB': 'Nordeste', 
    'PE': 'Nordeste', 'PI': 'Nordeste', 'RN': 'Nordeste', 'SE': 'Nordeste',
    'DF': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste',
    'ES': 'Sudeste', 'MG': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'RS': 'Sul', 'SC': 'Sul'
}

#Aplicando o mapeamento
df['region'] = df['state_code'].map(regioes_map)
print("Distribuição por região: ")
print(df['region'].value_counts())

#Salvando o dataFrame limpo e padronizado como 'dados_usuario_limpos.csv':
df.to_csv('dados_usuario_limpos.csv', index=False)
print("Limpeza e padronização de dados concluídas com sucesso!")