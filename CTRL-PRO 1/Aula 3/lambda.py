def loja1(valor):
    return valor * 1.10

lista = [100.0, 250.50, 30.99, 2200.15]
precos_novoss = list(map(loja1, lista))
print(precos_novoss)

precos_novos = list(map(lambda lojas: lojas * 1.10, lista))
print(precos_novos)

notas_turma = [5.5, 9.0, 7.2, 4.0, 6.8, 8.5, 10.0]
aprovados = list(filter(lambda n: n >= 7, notas_turma))
print(aprovados)

fruta = ["uva", "banana", "maça", 'abacaxi']
longas = list(filter(lambda p: len(p) >= 7 , fruta))
print(longas)

