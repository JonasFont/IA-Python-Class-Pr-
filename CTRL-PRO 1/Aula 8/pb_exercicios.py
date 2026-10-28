#Importanção das bibliotecas essenciais
import pandas as pd             #Manipulação de tabelas
import numpy as np              #Calculos matemáticos e vetorias
import matplotlib.pyplot as plt #Criação de graficas
from scipy import stats         #Funções estatisticas avançadas

#Carregar os dados do arquivo csv

df = pd.read_csv('dados_ti.csv')

#Explorando medidas de tendencia central para o serviço
media_a = df['latencia_a'].mean() #Calcula a media aritmetica
mediana_a = df['latencia_a'].median() #Calcula o valor central (mediana
desvio_a = df['latencia_a'].std() #Calcula o desvio padrao
#Devio padrao e para saber o quantos os dados variam entre si
print(f"----Servidor A----")
print(f"Media: {media_a:.2f}ms | Mediana: {mediana_a:.2f}ms "
      f"| Desvio: {desvio_a:.2f}ms")

media_b = df['latecia_b'].mean() #Calcula a media aritmetica
mediana_b = df['latecia_b'].median() #Calcula o valor central (mediana
desvio_b = df['latecia_b'].std() #Calcula o desvio padrao

print(f"----Servidor B----")
print(f"Media: {media_b:.2f}ms | Mediana: {mediana_b:.2f}ms "
      f"| Desvio: {desvio_b:.2f}ms")

#Pergunta: Qual a chance de uma requisição no Servidor B
#demorar mais de 80ms?
total_casos = len(df)  #Total de registros
casos_acima_80 = len(df[df['latencia_a'] > 60]) #Conta quantos registro foram > 80
prob_b_80 = (casos_acima_80/total_casos)*100 #Calculo simples de probabilidade


print(f"\nProbabilidade observada de Latência A > 60ms: {prob_b_80:.2f}%")

#Probabilidade Teórica (Distribuição Normal)
#Pergunta: Segundo a estatistica, qual a chance do latencia A passar de 60ms?
#sf (Survival Function) calcula a area a direita do ponto na curva normal
prob_teorica_60 = stats.norm.sf(60, loc=media_a, scale=desvio_a) * 100

print(f"Probabilidade teórica (Gauss) de Latencia A > 60ms : {prob_teorica_60:.2f}%")

#Visualização de Dados (Histograma)
plt.figure(figsize=(10,10))

#Plotando histogrma do Servidor A (em Azul) e B (Laranja)
#'density=true' transforma o eixo Y em probabilidade em vez de contagem bruta
plt.hist(df['latencia_a'], bins=40, alpha=0.6, label="Servidor A", color='blue', density=True)
plt.hist(df['latecia_b'], bins=40, alpha=0.4, label="Servidor B", color='orange', density=True)

#Adicionando a linha da curva noraml teorica para o servidor A
eixo_x = np.linspace(30, 75, 100) #Cria 100 pontos entre 30 e 75
pdf_a = stats.norm.pdf(eixo_x, media_a, desvio_a) #Calcula a densidade de probabilidade
plt.plot(eixo_x, pdf_a, color='red', label="Curva Normal Teorica (A)")

plt.title("Distribuição de Latência entre Servidores")
plt.xlabel("Tempo de Resposta (ms)")
plt.ylabel("Densidade Probabilidade")
plt.legend()
plt.show()