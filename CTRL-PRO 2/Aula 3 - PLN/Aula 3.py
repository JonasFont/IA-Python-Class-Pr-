from pandas.core.internals.construction import to_arrays
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

respostas = [

    # Saudações
    "Olá! Como posso ajudar?",

    "Olá! Como posso ajudar?",

    "Olá! Como posso ajudar?",

    "Olá! Como posso ajudar?",

    "Olá! Como posso ajudar?",

    "Olá! Como posso ajudar?",

    "Olá! Como posso ajudar?",


    # Preço
    "O preço do curso depende da modalidade escolhida.",

    "O preço do curso depende da modalidade escolhida.",

    "O preço do curso depende da modalidade escolhida.",

    "O preço do curso depende da modalidade escolhida.",

    "O preço do curso depende da modalidade escolhida.",

    "O preço do curso depende da modalidade escolhida.",


    # Horário
    "As aulas acontecem de acordo com o horário da turma.",

    "As aulas acontecem de acordo com o horário da turma.",

    "As aulas acontecem de acordo com o horário da turma.",

    "As aulas acontecem de acordo com o horário da turma.",

    "As aulas acontecem de acordo com o horário da turma.",


    # Cancelamento
    "Para cancelar, procure a secretaria da escola.",

    "Para cancelar, procure a secretaria da escola.",

    "Para cancelar, procure a secretaria da escola.",

    "Para cancelar, procure a secretaria da escola.",

    "Para cancelar, procure a secretaria da escola.",


    # Material
    "Você pode encontrar o material na plataforma da escola.",

    "Você pode encontrar o material na plataforma da escola.",

    "Você pode encontrar o material na plataforma da escola.",

    "Você pode encontrar o material na plataforma da escola.",

    "Você pode encontrar o material na plataforma da escola."
]

#2 TRANSFORMANDO TEXTO EM NUMEROS
vectorizer = TfidfVectorizer()
matriz = vectorizer.fit_transform(frases)

print("Vocabulario do chatbot")
print(vectorizer.get_feature_names_out())
print('MAtriz TF_IDF \n')
print(matriz.toarray())

def responder(pergunta):
    #Transofrmamos a pergutna do usuario em um vetor TF-IDF
    pergunta_vetor = vectorizer.transform([pergunta])

    #Calculamos a similaridade entra a pergunta e todas as frases conhecidas
    similaridade = cosine_similarity(pergunta_vetor, matriz)

    #Procuramos o indice da frase mais parecida
    indice = similaridade.argmax()

    pontuacao = similaridade[0][indice]

    #definimos um limite minimo
    #se a pergunta for muito diferente
    #das frases conhecidas, o chatbot
    #não deve tentar adivinhar

    if pontuacao < 0.25:
        return("Não consegui entender sua pergunta", pontuacao)

    return  respostas[indice], pontuacao





while True:
    pergunta = input("Voce: ")

    if pergunta.lower() == "sair":
        print("CHATBOT até mais!")
        break

    resposta, pontuacao = responder(pergunta)

    print("Chatbot: ", resposta)
    print("Confiança",
        round(pontuacao * 100, 1),
        "%"
    )