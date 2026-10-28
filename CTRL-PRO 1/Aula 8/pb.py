import pandas as pd
import numpy as np

#definimos uma semente para que os numeros aleatorios
#sejam iguas para todos
np.random.seed(42)

n = 1500 #Numeros de registro

dados = {
    'id': range(1, n + 1),
    #'Servidor A': Estável
    'latencia_a': np.random.normal(50, 5, n),
    #Servidor B' Instável
    'latecia_b': np.random.normal(55, 15, n),
    #Uso de CPU em % (0 a 100)
    'uso_cpu': np.random.uniform(20, 95, n),
    #Erros: 0 = sucesso, 1 = Falha (Probabilidade de 5% de falha)
    'status_erro': np.random.choice([0,1], size=n, p=[0.95, 0.05])
}
df_gerador = pd.DataFrame(dados)
df_gerador.to_csv('dados_ti.csv', index=False)
print("Dataset 'dados_ti.csv' criado com sucesso!")