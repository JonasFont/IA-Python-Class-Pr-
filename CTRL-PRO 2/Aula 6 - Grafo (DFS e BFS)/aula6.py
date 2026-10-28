import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import json
#Criando o Grafo
G = nx.Graph()


amizades = [
    ("Ana", "Bruno"),
    ("Ana", "Carla"),
    ("Bruno", "Diego"),
    ("Bruno", "Eva"),
    ("Carla", "Eva"),
    ("Carla", "Felipe"),
    ("Diego", "Eva"),
    ("Diego", "Gabriel"),
    ("Felipe", "Gabriel"),
    ("Eva", "Gabriel")
]
#Adiciona todas as conexões ao grafo
G.add_edges_from(amizades)

#Informações do grafo
print(f'Numero de pessoas: {G.number_of_nodes()}')
print(f'Numero de conexões: {G.number_of_edges()}')
print("\nPessoa da rede:")
print(list(G.nodes()))
print("\nConexões:")
print(list(G.edges()))

# ============================================
# 1. DFS =  BUSCA EM PROFUNDIDADE
#Explora primeiro todos os nós mais proximos do nó inicial, nivel por nivel
# ============================================
inicio = "Ana"
print("DFS")
#Gera a árvore de busca DFS
resultado_dfs = list(nx.dfs_preorder_nodes(G, source=inicio))
print(resultado_dfs)

# ============================================
# 2. BFS =  BUSCA EM LARGURA
#Visita primeiros todos os nós que estao proximos do nó incial
# ============================================
print("BFS")
resultado_bfs = list(nx.bfs_tree(G, source=inicio).nodes())
print(f"\nBusca iniciando em {inicio}")
print(resultado_bfs)


def recomendar_amigos(grafo, usuario):
    #Amigos diretos
    amigos_diretos = set(grafo.neighbors(usuario))

    #Dicionario de recomendações
    recomendacoes  = {}

    #Percorre os amigos do usuario
    for amigo in amigos_diretos:
        for sugestao in grafo.neighbors(amigo):
            if(sugestao != usuario and sugestao not in amigos_diretos):
                amigos_comun = list(nx.common_neighbors(
                    grafo,
                    usuario,
                    sugestao
                ))
                recomendacoes[sugestao] = len(amigos_comun)

    ranking = sorted(
        recomendacoes.items(),
        key=lambda item: item[1],
        reverse=True
    )
    return ranking
filme = input("Digite um filme: ")
ranking = recomendar_amigos(G, filme)
print(f"\nPessoas recomendadas para {inicio}")

for pessoa, conexao in ranking:
    print(
        f"{pessoa} -> "
        f"{conexao} filme(s) em comun"
    )
plt.figure(figsize=(10, 7))
nx.draw(G, with_labels=True, node_size=2500,
        font_size=12, font_weight='bold')
plt.title("Rede Social - Grafo")
plt.show()


dados_json = json.dumps(resultado_bfs, ensure_ascii=False, indent=4)

print(dados_json)