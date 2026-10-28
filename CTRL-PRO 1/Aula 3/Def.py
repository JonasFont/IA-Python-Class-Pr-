#Crie duas funções uma para pedir o valor das notas
#E a outra para calcular a media das notas

#def para_int(texto):
    #return int(texto)


#numeros_textos = ["10", "5", "2"]
#print(numeros_textos)
#numeros = list(map(para_int, numeros_textos))
#print(numeros)

def saudar(nome):
    return "Ola, "+ nome

usuarios = ["Ana", "João", "Maria"]
mensagem = list(map(saudar, usuarios))
print(mensagem)


def contar_letras(palavras):
    return len(palavras)

frutas = ["Maça", "Banana", "Abacaxi"]
a = list(map(contar_letras, frutas))
print(a)

def dobrar(n):
    return n * 2

t = [10, 15, 20]
p = list(map(dobrar, t))
print(p)

def eh_par(z):
    return z % 2 == 0

numeross = [1, 3, 4, 10, 101, 1000]
pares = list(filter(eh_par, numeross))
print(pares)

def senha_longas(senha):
    return  len(senha) > 8

senhaas = ["asdzxcqwe1", 'asdae', 'aopifpsag23', '1234']
senha = list(filter(senha_longas, senhaas))
print(senha)