entrada_usuario = "   joão_silva@gmail.com   "
print(len(entrada_usuario))
print(entrada_usuario)
#remove espaços inuteis strip()
#conta a quantidade de caracteres dentro de uma arrazy ou variavel .le()
email_limpo = entrada_usuario.strip()
print(len(email_limpo))
print(email_limpo)
#Troca o valor escolhido por um novo
email_final = email_limpo.replace(" ", ".")
print(email_final)

nome_cracha = "joão silva".upper() #.lower()
print(nome_cracha)
#pip install validate-docbr

#Sistema base de login pede nome, email e cpf
#No CPF validem se o CPF e valido
input()