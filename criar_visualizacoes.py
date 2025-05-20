import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator

#Configurando o matplotlib para exibir corretamente os caracteres especiais em português
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.style.use('ggplot')

#Carregando o dataset
df = pd.read_csv('dados_usuario_limpos.csv', sep=',', encoding='latin1')

#Convertendo a coluna date para datetime
df['date'] = pd.to_datetime(df['date'])
df['full_date'] = pd.to_datetime(df['full_date'])

#VISUALIZAÇÃO 1 - Série temporal da média de 'number' por ano

#Agrupando por ano e calculando a média
yearly_avg = df.groupby('year')['number'].mean().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(yearly_avg['year'],yearly_avg['number'], marker='o', linestyle='-', linewidth=2, markersize=8)
plt.title("Média de valores por ano", fontsize=16) 
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Média', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(yearly_avg['year'], rotation=45)
plt.tight_layout()
plt.savefig('visualizaca1_serie_temporal_anual.png')
print("Visualização 1 salva como imagem")

#VISUALIZAÇÃO 2 - Distribuição de number por região