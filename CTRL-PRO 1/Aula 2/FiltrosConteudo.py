senha = input("Digite sua senha: ")

#Criamos uma lista de verificações (Booleanas)
#Verifica se algum dos caracteres e Maiusculas ele retorna True
contem_maiusculo = any(chat.isupper() for chat in senha)
print(contem_maiusculo)
#
contem_numero = any(char.isdigit() for char in senha)
print(contem_numero)
tamanho_minimo = len(senha) >= 8
print(tamanho_minimo)

requesitos = [contem_maiusculo, contem_numero, tamanho_minimo]

if all(requesitos):
    print("Senha Segura")
else:
    print("Senha fraca. Verigique os requesitos.")
#Exercicio
#Senha deve possuir 1 Letra maiuscula, 1 minuscula, 1 Numero
#1 Caracter Especial, > 12 Digitos

palavras_proibidas = ["spam", "bot", "palmeiras", 'palavrão']
comentario = input("Digite uma frase: ")

bloqueado = any(proibida in comentario.lower() for proibida in palavras_proibidas)
if bloqueado:
    print("Comentario retido para moderação.")
else:
    print("Bom comentario")