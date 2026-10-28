import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/1XPng6Xxq_eNkfW4ASEgaXdHoZml6UxVmTkjygXeGfFk/edit?usp=sharing'
df = pd.read_csv('url')

df_estados = df[df['state'] != 'TOTAL']
print(df_estados)
print(df.columns.tolist())
estado_maior_mortes = df_estados.loc[df_estados['deaths'].idxmax()]
print(estado_maior_mortes)

estado_porporcional = df_estados.loc[df_estados['deaths_per_100k_inhabitants'].idxmax()]
print(estado_porporcional)

print(df.info())