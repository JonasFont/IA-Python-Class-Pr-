import pandas as pd
import sqlite3
#codeshare.io/ctrlplay
conn = sqlite3.connect('sistema_comecial.db')

vendas_data = {
    'ID_Venda': [101, 102, 103, 104, 105, 106, 107],
    'Produto': ['Notebook', 'Mouse', 'Notebook', 'Teclado', 'Mouse', 'Monitor', 'Teclado'],
    'Categoria': ['Eletrônicos', 'Acessórios', 'Eletrônicos', 'Acessórios', 'Acessórios', 'Eletrônicos', 'Acessórios'],
    'Quantidade': [1, 5, 2, 10, 2, 1, 3],
    'Preco_Unitario': [4500, 50, 4500, 150, 50, 1200, 150]
}

estoque_data = {
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor'],
    'Qtd_Minima': [5, 20, 15, 10],
    'Qtd_Atual': [3, 50, 12, 15]
}
df_vendas = pd.DataFrame(vendas_data)
df_estoque = pd.DataFrame(estoque_data)
a = df_vendas[df_vendas['Produto']  == 'Notebook']
print(a)
#Salvar as tabelas inicias no banco
df_vendas.to_sql('Vendas', conn, if_exists='replace', index=False)
df_estoque.to_sql('Estoque', conn, if_exists='replace', index=False)

df_db_vendas = pd.read_sql('SELECT * FROM vendas', conn)
df_db_vendas['Total_Item'] = df_db_vendas['Quantidade'] * df_db_vendas['Preco_Unitario']


relatorio_categoria = df_db_vendas.groupby('Categoria').agg(
    Faturamento_total=("Total_Item", 'sum'),
    Ticket_media=('Total_Item', 'mean'),
    Qts_itens_vendidos=('Quantidade', 'sum'),
)

