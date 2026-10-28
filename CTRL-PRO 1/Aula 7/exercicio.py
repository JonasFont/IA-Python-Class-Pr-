import pandas as pd
import numpy as np

# Criando dados de um E-commerce de Tecnologia
dados_tech = {
    'Produto': ['Smartphone', 'Laptop', 'Tablet', 'Fone Bluetooth', 'Monitor 4K', 'Teclado Mecânico', 'Mouse Gamer'],
    'Categoria': ['Mobile', 'Computação', 'Mobile', 'Acessórios', 'Computação', 'Acessórios', 'Acessórios'],
    'Preco_Unitario': [2500, 4500, 1800, 350, 2200, 450, 250],
    'Quantidade_Vendida': [150, 80, 120, 400, 60, 210, 310],
    'Avaliação_Clientes': [4.5, 4.8, 4.2, 4.0, 4.7, 4.9, 4.6],
    'Custo_Fabricação': [1200, 2800, 900, 100, 1400, 180, 90]
}

df_tech = pd.DataFrame(dados_tech)

df_tech['Faturamento_Total'] = df_tech["Preco_Unitario"] * df_tech["Quantidade_Vendida"]
df_tech['Lucro_Total'] = df_tech['Faturamento_Total'] - (df_tech['Custo_Fabricação'] * df_tech['Quantidade_Vendida'])
print(df_tech)

df_tech.to_csv('vendas_tech.csv', index=False)
print("Novo dataset 'vendas_tech.csv' Gerado com sucesso!")