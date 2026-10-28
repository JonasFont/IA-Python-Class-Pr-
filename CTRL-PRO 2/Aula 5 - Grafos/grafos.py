import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


G = nx.Graph()

rua = [
    "Rua 10 de Julho",
    "Av. Eduardo Ribeiro",
    "R. José Clemente",
    "R. Dona Libania",
    "R. 24 de Maio",
    "R. Barroso",
    "R. Costa Azevedo",
    "Av. Gertio Vargas",
    "R. Saldanha Marinho"
]

G.add_nodes_from(rua)

ligacoes = [
    ("Rua 10 de Julho", "Av. Eduardo Ribeiro"),
    ("Rua 10 de Julho", "R. Costa de Azevedo"),
    ("Rua 10 de Julho", "Av. Gertio Vargas"),
    ("Av. Eduardo Ribeiro", "R. Saldanha Marino"),
    ("Av. Eduardo Ribeiro", "R. 24 de Maio"),
    ("Av. Eduardo Ribeiro", "R. José Clemente"),
    ("R. José Clemente", "Av. Gertio Vargas"),
    ("R. José Clemente", "R. Dona Libania"),
    ("R. José Clemente", "R. Costa de Azevedo"),
    ("R. José Clemente", "R. Barros"),
    ("R. José Clemente", "Av. Eduardo Ribeiro"),
    ("R. 24 de Maio", "Av. Gertio Vargas"),
    ("R. 24 de Maio", "Av. Gertio Vargas"),
    ("R. 24 de Maio", "R. Barros"),
    ("R. 24 de Maio", "Av. Eduardo Ribeiro"),
    ("R. Saldanha Marinho", "Av. Gertio Vargas"),
    ("R. Saldanha Marinho", "Av. Gertio Vargas"),
    ("R. Saldanha Marinho", "R. Costa de Azevedo"),
    ("R. Saldanha Marinho", "R. Barros"),
    ("R. R. Saldanha Marinho", "Av. Eduardo Ribeiro"),
    ("R. Barroso", "José Clemente"),
    ("R. Barroso", "R. 24 Maio"),
    ("R. Barroso", "R. Saldanha Marinho"),
    ("R. Costa Azevedo", "R. Sadanha Marinho"),
    ("R. Costa Azevedo", "R. 24 de Maio"),
    ("R. Costa Azevedo", "R. José Clemente"),
    ("R. Dona Libania", "Rua 10 de Julho"),
    ("R. Dona Libania", "R. José Clemente"),
    ("R. Dona Libania", "R. 24 de Maio"),

]

G.add_edges_from(ligacoes)


print("NOS DE GRAFOS")
print(list(G.nodes()))

print("LIGACOES DOS GRAFOS")
for rua1, rua2 in G.edges():
    print(f"{rua1} está ligada a {rua2}")

print(f"Quntidade de ligações {G.number_of_edges()}")



rua = "Rua 10 de Julho"

for letra in G.neighbors(rua):
    print(f"{rua} -> {letra}")

orig = "Rua 10 de Julho"
dest = "R. 24 de Maio"
print("-"*50)
caminho = nx.shortest_path(G, orig, dest)
print("->".join(caminho))

plt.figure(figsize=(10, 7))
posicoes = nx.spring_layout(
    G,
    seed=42
)
nx.draw(
    G,
    posicoes,
    with_labels=True,
    font_size=8,
    node_size=3500,
    font_weight="bold",
)

plt.title("Grafos de Ligações entre ruas de Manaus", fontsize=24)
plt.show()