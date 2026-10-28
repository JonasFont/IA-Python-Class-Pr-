#NLTK Natural language Toolkit LPN
import pandas as pd
import matplotlib.pyplot as plt
import string
import nltk
nltk.download('punkt_tab')
#Transforma uma frase em varias partes
nltk.download('punkt')

#É uma lista de palavras muito comuns em determinados idiomas
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

df = pd.read_csv('Pesquisa_de_Satisfacao_Sapataria.csv')
print(df.info())

print(df.describe())

stop_words = set(stopwords.words('portuguese'))

def preprocessar(texto):
    #word_tokenize é ele que vai dividir os textos em tokens
    #exemplo: "Produto muito bom"
    #Vira: ["produto", "muito", "bom"]
    token = word_tokenize(
        texto.lower(),
        language='portuguese'
    )
    token = [
        palavra
        for palavra in token
        if palavra not in string.punctuation
    ]
    token = [
        palavra
        for palavra in token
        if palavra not in stop_words
    ]
    return token

texto_exemplo = df["Texto da Avaliação"].iloc[0]
print(texto_exemplo)

token_exemplo = preprocessar(texto_exemplo)
print("\n============== TEXTO PROCESSADO=============")
print(token_exemplo)
df["token"] = df["Texto da Avaliação"].apply(preprocessar)
print(df["token"])

palavras_positivas = {

    "ótimo",
    "ótima",
    "excelente",
    "excelentes",

    "bom",
    "boa",
    "bons",
    "boas",

    "perfeito",
    "perfeita",

    "satisfeito",
    "satisfeita",

    "confortável",
    "confortáveis",

    "recomendo",
    "recomendo",

    "qualidade",

    "rápido",
    "rápida",

    "rápidos",
    "rápidas",

    "feliz",
    "impressionante",

    "agradável",
    "agradáveis"
}


# ------------------------------------------------------------
# 12. PALAVRAS NEGATIVAS
# ------------------------------------------------------------

palavras_negativas = {

    "ruim",
    "ruins",

    "péssimo",
    "péssima",
    "péssimos",
    "péssimas",

    "horrível",
    "horríveis",

    "decepcionado",
    "decepcionada",

    "insatisfeito",
    "insatisfeita",

    "desconfortável",
    "desconfortáveis",

    "problema",
    "problemas",

    "defeito",
    "defeitos",

    "caro",
    "cara",
    "caros",
    "caras",

    "demorou",
    "demorado",
    "demorada",

    "lento",
    "lenta",
    "lentos",
    "lentas"
}

def analisar_sentimento(tokens):
    positivas = 0
    negativas = 0

    #Percorrer todas as palavras da avaliação
    for palavra in tokens:
        if palavra in palavras_positivas:
            positivas += 1
        elif palavra in palavras_negativas:
            negativas += 1

    pontuacao = positivas - negativas
    if pontuacao > 0:
        sentimento = "Positivo"
    elif pontuacao < 0:
        sentimento = 'Negativo'
    else:
        sentimento = "Neutro"

    return  sentimento

print(analisar_sentimento(token_exemplo))

df["Sentimento"] = df['token'].apply(analisar_sentimento)

print("\nResultado das avaliações")

print(df[
    [
    "Nota da Avaliação",
    "Texto da Avaliação",
    "Sentimento",
    ]].head(20)
)

media_sentimento = (
    df
    .groupby("Sentimento")["Nota da Avaliação"]
    .mean()
    .sort_values(ascending=False)
)
print((media_sentimento.round(2)))

print('--------------')
relacao = pd.crosstab(
    df['Nota da Avaliação'],
    df['Sentimento'],
)
print(relacao)

plt.figure(figsize=(8, 5))

(df["Nota da Avaliação"].value_counts().sort_index()).plot(
    kind="bar",
)

plt.title("Distribuição das Notas")
plt.xlabel("notas")
plt.ylabel("Quantidade de avaliações")
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
pd.crosstab(
    df["Nota da Avaliação"],
    df['Sentimento']
).plot(
    kind="bar",
    ax=plt.gca()
)
plt.title("Relação entre nota e sentimento")
plt.xlabel("Nota da Avaliação")
plt.ylabel("Quantidade de avaliações")
plt.legend(title="Sentimento")
plt.tight_layout()
plt.show()


plt.figure(figsize=(9, 5))

media_sentimento.plot(
    kind="bar"
)
plt.title("Nota média por sentimento")
plt.xlabel("Sentimento")
plt.ylabel("Nota Média")
plt.tight_layout()
plt.show()
