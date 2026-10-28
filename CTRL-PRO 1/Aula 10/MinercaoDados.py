from pydoc import describe

import pandas as pd
import numpy as np
from scipy.datasets import ascent
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
#Carrega o dataset
df = pd.read_csv('dados_vendas_aula_python.csv')

#1.1 Visão Geral
#Mostra as primeiras 5 linhas e os tipos de dados
print('---Primeiras Linhas---')
print(df.head())

#1.2 Estatística Descritiva
#Mostrar Media, Contagem, Desvio Padrão. min, max etc...
print("\n--- Resumo Estatístico ---")
print(df.describe().round(2))

#1.3 Verificação a "Sauda" dos Dados
print('\n--- Valores Ausente por Coluna ---')
print(df.isnull().sum())

#2.1 Tratando valores Nulos
# Camos preencher os metodos de pagamentos vazio com 'outros'
df['metodo_pagamento'] = df['metodo_pagamento'].fillna('Outros')
print(df.isnull().sum())

#2.2 Corrigindo tipo de Dado
#Converter a coluna 'dara para datetime permite minerar por mês/dia
df['data']= pd.to_datetime(df['data'])
print(df['data'])

#2.3 Tratamento Outilines (Anomalias)
#Como vimos no describe, o valor maximo de 150.000 parece erro.
#Vamos remover qualquer linha onde o valor unitario seja absurdo
df = df[df['valor_unitario'] < 1000].copy()
print(df)
print(df.describe().round(2))

print((f'Limpeza concluida. Total de linhas restantes: {len(df)}'))

#-----------------------Mineração de Dados-------------------
#3.1 Qula cidade mais gasta na loja?
vendas_cidade = df.groupby('cidade')['valor_total'].sum().sort_values(ascending=False)
print('Faturamento por Cidade: \n', vendas_cidade)


#3.2 Comportamento por Categoria
#Criando um tabela dinâmico (pivot Table) para ver a quantidade vendida por cidade e categoria
tabela_dinamica = df.pivot_table(index='cidade', columns='categoria',
                                 values='quantidade', aggfunc='sum')

print("\nDistribuição de Categorias por cidade")
print(tabela_dinamica.fillna(0))



# -----------------------Graficos------------------
#Configuração de estilo para os graficos ficarem modernos
sns.set_theme(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

#4.1 Histograma de Distrivuiçãoo de Preço
#Serve para entender a concentação de preço dos produtos
plt.figure()
sns.histplot(df['valor_unitario'], bins=30, kde=True, color='skyblue')
plt.title("Distibruição de Valores Unitarios (Após Limpeza)")
plt.xlabel("Preço (R$)")
plt.ylabel("Frequencia")
plt.show()

#4.2 GRafico de Barras: Faturamento por cidade
plt.figure()
vendas_cidade = df.groupby('cidade')['valor_total'].sum().sort_values(ascending=False)
vendas_cidade.plot(kind='bar', color='seagreen')
plt.title("Total de vendas por Cidade")
plt.ylabel('Faturamento total (R$)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()