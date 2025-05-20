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
#Agrupando por região e calculando a média
region_avg = df.groupby('region')['number'].mean().sort_values(ascending=False).reset_index()

plt.figure(figsize=(12, 6))
bars = plt.bar(region_avg['region'], region_avg['number'], color=sns.color_palette('viridis', len(region_avg)))
plt.title('Média de valores por região', fontsize=16)
plt.xlabel('Região', fontsize=12)
plt.ylabel('Média', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')

# Adicionando valores nas barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 5,
             f'{height:.1f}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('visualizacao2_distribuicao_por_regiao.png')
print("Visualização 2 salva como 'visualizacao2_distribuicao_por_regiao.png'")

# Visualização 3: Mapa de calor da média de 'number' por mês e ano
print("\n\n4. Visualização 3: Mapa de calor da média de 'number' por mês e ano")
print("-" * 50)

# Agrupando por ano e mês, calculando a média
heatmap_data = df.groupby(['year', 'month_num'])['number'].mean().reset_index()
heatmap_pivot = heatmap_data.pivot(index='month_num', columns='year', values='number')

plt.figure(figsize=(14, 8))
sns.heatmap(heatmap_pivot, cmap='YlOrRd', annot=False, fmt='.1f', linewidths=.5)
plt.title('Média de Valores por Mês e Ano', fontsize=16)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Mês', fontsize=12)

# Ajustando os rótulos do eixo y para nomes dos meses
month_names = {1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun', 
               7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'}
plt.yticks(np.arange(0.5, 12.5), [month_names[i] for i in range(1, 13)])

plt.tight_layout()
plt.savefig('visualizacao3_heatmap_mes_ano.png')
print("Visualização 3 salva como 'visualizacao3_heatmap_mes_ano.png'")

# Visualização 4: Top 10 estados com maiores médias de 'number'
print("\n\n5. Visualização 4: Top 10 estados com maiores médias de 'number'")
print("-" * 50)

# Agrupando por estado e calculando a média
state_avg = df.groupby('state_code')['number'].mean().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(12, 6))
bars = plt.barh(state_avg['state_code'], state_avg['number'], color=sns.color_palette('viridis', len(state_avg)))
plt.title('Top 10 Estados com Maiores Médias', fontsize=16)
plt.xlabel('Média', fontsize=12)
plt.ylabel('Estado', fontsize=12)
plt.grid(True, alpha=0.3, axis='x')

# Adicionando valores nas barras
for bar in bars:
    width = bar.get_width()
    plt.text(width + 5, bar.get_y() + bar.get_height()/2.,
             f'{width:.1f}', ha='left', va='center', fontsize=10)

plt.tight_layout()
plt.savefig('visualizacao4_top10_estados.png')
print("Visualização 4 salva como 'visualizacao4_top10_estados.png'")

# Visualização 5: Boxplot da distribuição de 'number' por mês
print("\n\n6. Visualização 5: Boxplot da distribuição de 'number' por mês")
print("-" * 50)

plt.figure(figsize=(14, 8))
sns.boxplot(x='month', y='number', data=df, order=['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
                                                   'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'])
plt.title('Distribuição de Valores por Mês', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Valor', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('visualizacao5_boxplot_meses.png')
print("Visualização 5 salva como 'visualizacao5_boxplot_meses.png'")

# Visualização 6: Evolução temporal por região
print("\n\n7. Visualização 6: Evolução temporal por região")
print("-" * 50)

# Agrupando por ano e região, calculando a média
region_year_avg = df.groupby(['year', 'region'])['number'].mean().reset_index()

plt.figure(figsize=(14, 8))
for region in df['region'].unique():
    data = region_year_avg[region_year_avg['region'] == region]
    plt.plot(data['year'], data['number'], marker='o', linestyle='-', linewidth=2, label=region)

plt.title('Evolução da Média de Valores por Região ao Longo dos Anos', fontsize=16)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Média', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(title='Região', fontsize=10)
plt.xticks(df['year'].unique(), rotation=45)
plt.tight_layout()
plt.savefig('visualizacao6_evolucao_por_regiao.png')
print("Visualização 6 salva como 'visualizacao6_evolucao_por_regiao.png'")

print("\nTodas as visualizações foram criadas com sucesso!")
