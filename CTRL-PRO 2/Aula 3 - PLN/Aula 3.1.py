from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.naive_bayes import MultinomialNB

frases = [
    #SAUDAÇÔES
    'oi',
    'ola',
    'bom dia',
    'boa noite',
    'eai',
    'tudo bem',
    'boa tarde',
    #PREÇO
    'qual o preço do curso',
    'quanto custa o curso',
    'qual o valor da mensalidade',
    'quanto tenho que pagar',
    'qual é o preço',
    'quanto custa',
    #HORARIO
    'qual o horário das aulas',
    'que horas começa a aula',
    'quando começa a aula',
    'qual o horario do curso',
    'que horas é a aula',
    #CANCELAMENTO
    'quero cancelar minha matricula',
    'como cancelar o curso',
    'quero sair do curso',
    'quero cancelar minha inscrição',
    'como faço para cancelar',
    #MATERIAL
    'onde encontro o material',
    'onde estão as atividade',
    'onde vejo minhas atividades',
    'quero acessar o material',
    'onde estão os exercicios'
]

rotulos = [
    "oi",
    "oi",
    "oi",
    "oi",
    "oi",
    "oi",
    "oi",

    # PREÇO
    "preco",
    "preco",
    "preco",
    "preco",
    "preco",
    "preco",

    # HORÁRIO
    "horario",
    "horario",
    "horario",
    "horario",
    "horario",

    # CANCELAMENTO
    "cancelamento",
    "cancelamento",
    "cancelamento",
    "cancelamento",
    "cancelamento",

    # MATERIAL
    "material",
    "material",
    "material",
    "material",
    "material"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(frases)

#CRia o modelo
modelo = MultinomialNB()

#Treinar a IA
modelo.fit(X, rotulos)

print("Modelo Treinado")

respostas = {

    "preco":
        "O valor do curso pode ser consultado na secretaria.",

    "horario":
        "O horário da sua aula pode ser consultado na plataforma.",

    "cancelamento":
        "Para realizar o cancelamento, procure a secretaria.",

    "material":
        "O material e as atividades estão disponíveis na plataforma."
}

def responder(pergunta):
    pergunta_transformada = vectorizer.transform([pergunta])

    #Modelo prevêr a intenção
    intencao = modelo.predict(pergunta_transformada)[0]

    #Descobrir a probabilidade
    probabilidade = modelo.predict_proba(
        pergunta_transformada
    )[0]

    confianca = max(probabilidade)

    if confianca < 0.30:
        return(
            "Escreve direito HUMANO.",
            intencao,
            confianca
        )
    return (
        respostas[intencao],
        intencao,
        confianca
    )


perguntas = [
    "Quanto vou pagar por mes?",
    'Que horas vou ter aula?',
    "não quero mais fazer o curso",
    "onde encontro minha atividade?"
]

for pergunta in perguntas:
    resposta, intencao, confianca = responder(pergunta)
    print("\nPergunta:", pergunta)
    print("Intenção:", intencao)
    print("Confiança: ", round(confianca * 100, 2), "%")
    print("Resposta:", resposta)