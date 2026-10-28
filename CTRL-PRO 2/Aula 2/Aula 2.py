
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import  MultinomialNB
#Gostei
#[00111] [01111] [10011] 10100 00101 01001 = gostei
dados = {
    "Comentarios": [
        "Gostei muito da aula",
        "Professor explica muito bem",
        "Excelente conteúdo",
        "Aprendi bastante",
        "Muito bom",
        "Achei incrível",
        "Gostei do exercício",
        "Foi excelente",
        "Muito interessante",
        "Parabéns pelo curso",

        "Não gostei",
        "Muito ruim",
        "Pessima aula",
        "Muito difícil",
        "Horrível",
        "Não aprendi",
        "Achei chato",
        "Muito confuso",
        "Pessimo conteúdo",
        "Não recomendo",


    ],
    "Sentimentos": [

        "Positivos","Positivos","Positivos","Positivos","Positivos",
        "Positivos","Positivos","Positivos","Positivos","Positivos",

        "Negativo","Negativo","Negativo","Negativo","Negativo",
        "Negativo","Negativo","Negativo","Negativo","Negativo"
    ]
}
df = pd.DataFrame(dados)

print("\nQuantidade por Sentimento")
print(df["Sentimentos"].value_counts())

print("\nPorcentagem")
print(df["Sentimentos"].value_counts(normalize=True)*100)



#Estou retirando o espaços entre as palavras
texto = " ".join(df['Comentarios'])
#Estou transformando tudo em letra minuscula
texto = texto.lower()
#Separa a string exemplo: Gostei da aula
palavra = texto.split()
#Conta quantas vezes cada palavra apareceu
contador = Counter(palavra)

print(contador.most_common(10))

top10 = contador.most_common(10)

nomes = [i[0] for i in top10]
quantidade = [i[1] for i in top10]
print(nomes)
print(quantidade)

plt.bar(nomes, quantidade)
plt.title("Palavras mais Frequentes")
plt.xticks(rotation=45)
plt.show()

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Comentarios'])
modelo = MultinomialNB()

modelo.fit(X, df["Sentimentos"])

print("IA Treinada com sucesso")

while True:
    frase = input("\nDigite um comentario: ('sair' para encerrar): ")

    if frase.lower() == "sair":
        break

    frase_vetor = vectorizer.transform([frase])

    resultado = modelo.predict(frase_vetor)

    print("\nSentimento identificado:")
    print(resultado[0])


#PLN  = Processamento de Linguagem Natural (PLN)
#IA Generativa = Criar ideias a partir prompts (Texto)
#LLMs Large Language Models, ou Grandes Modelos de Linguagem
#O Machine Learning (aprendizado de máquina)
#O deep learning (aprendizado profundo)
#Visão Computacional, Computador extrair informações e compreender
#conteudo de imagens e videos