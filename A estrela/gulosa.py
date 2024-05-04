grafo = { 
    'a': ['b', 'c', 'd'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'f'],
    'd': ['a', 'b','e','g'],
    'e': ['b','d', 'g'],
    'f': ['c', 'g'],
    'g': ['e','d','f']               
}
pesos = { 
    'a': [9, 5, 13],
    'b': [9, 3, 10],
    'c': [5, 12],
    'd': [13, 3, 6, 14],
    'e': [10, 6, 7],
    'f': [12, 10],
    'g': [7, 14, 10]               
}
heuristica = {
    'a': [24],
    'b': [15],
    'c': [22],
    'd': [12],
    'e': [7],
    'f': [7],
    'g': [0]   
}


def busca_gulosa(inicio, resposta):
    noAtual = inicio
    caminho = [inicio.upper()]
    while noAtual != resposta:
        tamanho = len(grafo[noAtual])
        listaDeFilhos = []
        listaDeHeuristicas = []  # Lista para armazenar apenas os valores heurísticos

        for i in range(tamanho):
            filho = grafo[noAtual][i]
            heuristica_filho = heuristica[filho][0]  # Apenas a heurística do filho
            listaDeFilhos.append(filho)
            listaDeHeuristicas.append(heuristica_filho)

        # Escolher o filho com a menor heurística (busca gulosa)
        menor_heuristica = min(listaDeHeuristicas)
        index_menor_heuristica = listaDeHeuristicas.index(menor_heuristica)
        noAtual = listaDeFilhos[index_menor_heuristica]
        caminho.append(noAtual.upper())
    return caminho

print(busca_gulosa('a', 'g'))
