import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Criando os dados
data = {
    'Dia': ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom'],
    'Vendas_Cafe': [120, 150, 140, 165, 210, 250, 300],
    'Vendas_Comida': [80, 95, 85, 110, 130, 190, 180],
    'Clientes': [45, 52, 48, 60, 75, 100, 95],
    'Categoria_Mais_Vendida': ["Grão", "Moido", "Grão", "Bebida", "Bebida", "Grão", "Grão"]
}
#Transforma os dados em um dataframe
df = pd.DataFrame(data)
print(df)

df.to_csv('vendas_cafeteria.csv', index=False)
print("Arquivo 'vendas_cafeteria.csv' criado com sucesso!")

