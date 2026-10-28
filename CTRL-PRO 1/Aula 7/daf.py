import pandas as pd
import matplotlib.pyplot as plt
from pyparsing import alphas

#Importando o arquivo
df = pd.read_csv('vendas_cafeteria.csv')

#Configura a tela
plt.figure(figsize=(10,10))
#markersize, markerfacecolor
#Plot
plt.plot(df['Dia'], df['Clientes'],marker='o',color='lightblue',label='Cafeteria')
#plt.bar(df['Dia'], df['Clientes'], color='blue', edgecolor='red')
#plt.scatter(df['Dia'], df['Vendas_Cafe'], color='blue', edgecolor='black')
#plt.hist(df['Vendas_Cafe'], bins=10, color='purple', edgecolor='red')
#plt.boxplot(df['Vendas_Cafe'], patch_artist=True, boxprops=dict(facecolor='lightblue'))



#Titulo
plt.title('Relatorio de Vendas = Cafeteria Cafeteria', fontsize=20)
#plt.xlabel('Distribuição das vendas', fontsize=20)
plt.ylabel('Freqencia (Quantos dias)', fontsize=20)
plt.grid(True, alpha=0.3)
plt.legend()

#Mostrar a tabela
plt.show()

totais = [df['Vendas_Cafe'].sum(), df['Vendas_Comida'].sum()]
label = ['Cafe', "Comida"]
cores = ['green', 'pink']

#plt.figure(figsize=(6, 6))

#plt.pie(totais, labels=label, colors=cores, autopct="%1.1f%%", startangle=140)
#plt.title("Porporção do faturamento Total")
#plt.show()
