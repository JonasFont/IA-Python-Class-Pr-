import pandas as pd

dados = {
    'Produto': ['Arroz', 'Feijão', 'Macarrão'],
    'Preço': [25.50, 9.80, 5.20],
    'Estoque': [100, 50, 200]
}
df = pd.DataFrame(dados)
print(df.head(2))
print(df.tail(1))
print(df.info())