import osmnx as ox

local = "São José dos Campos, São Paulo, Brazil"
G = ox.graph_from_place(local, network_type='drive')
# Endereço de origem


origem = input("Digite o endereço: ")
origem_endereco = origem + ",São José dos Campos, São Paulo, Brazil"
# Endereço de destino
destino = input("Digite o Destino: ")
destino_endereco = destino +", São José dos Campos, São Paulo, Brazil"


# ============================================
# 1. TRANSFORMAR ENDEREÇOS EM COORDENADAS
# ============================================

# Retorna:
# latitude e longitude

origem_lat, origem_lon = ox.geocode(origem_endereco)

destino_lat, destino_lon = ox.geocode(destino_endereco)

no_origem = ox.nearest_nodes(G, origem_lon, origem_lat)
no_destino = ox.nearest_nodes(G, destino_lon, destino_lat)

rota = ox.shortest_path(G, no_origem, no_destino, weight="length")

ox.plot_graph_route(G, rota)