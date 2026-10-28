import pandas as pd   #Analise de dados
import numpy as np  #Calculos
import matplotlib.pyplot as plt   #Criação de graficos
from scipy import stats #Calculos probabilisticos e Estatisticos
from scipy.stats import norm

np.random.seed(42)    #reprodutibilidade

#Servidor A (Servidor Estavel)
latencia_a = np.random.normal(loc=55, scale=8, size=1000)

#Servidor B (mais instavel + alguns picos a mais)
latencia_b = np.random.normal(loc=60, scale=12, size=1000)

outilers = np.random.choice(range(1000), size=20)
latencia_a[outilers] = np.random.randint(30, 80, size=20)


df = pd.DataFrame({
    'latencia_a': latencia_a,
    'latencia_b': latencia_b,
})
#print(df)
print('Visão Geral dos dados')
print(df.head())
print("\nresumo estatistico:")
print(df.describe())


media_a  = df['latencia_a'].mean() #tirar a media
desvio_a = df['latencia_a'].std() #Tirar o desvio padrão

print("\nServidor A")
print(f"Media: {media_a:.2f} ms")
print(f"Desvio: {desvio_a:.2f} ms")

#Probabilidade Real (Empirica)
prob_real = (df['latencia_a'] > 70).mean()
print(f'Probabilidade: {prob_real*100:.2f} %')

prob_realb = (df['latencia_b'] > 70).mean()
print(f'Probabilidade: {prob_realb*100:.2f} %')

#Probabilidade teoria (Gauss)
#Qual a chance do A passar de 70ms?

prob_teorica = 1 - norm.cdf(70, loc=media_a, scale=desvio_a)
print(f"Probabilidade teorica do Servidor A > 70: {prob_teorica:.2f} %")


#Visualização dos dados
x = np.linspace(df['latencia_a'].min(), df['latencia_a'].max(), 1000)
y = norm.pdf(x, media_a, desvio_a)

plt.figure(figsize=(10, 5))

plt.hist(df['latencia_a'], bins=30,density=True,
         alpha=0.8, color='blue', edgecolor='black', label='Dados reais A')

plt.plot(x,y, label='Curva normal', color='black')

#Area de risco (>70)
x_fill = np.linspace(50, x.max(), 1000)
plt.fill_between(x_fill, norm.pdf(x_fill, media_a, desvio_a),alpha=0.7)

plt.title("Risco de Latência Alta (Servidor A)")
plt.xlabel("Latencia (ms)")
plt.ylabel("Densidade (%)")
plt.legend()
plt.show()