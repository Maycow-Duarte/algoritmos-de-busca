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

def AEstrela(inicio, resposta):
    noAtual = inicio
    caminho = [inicio.upper()]
    while noAtual != resposta:#faz isso até o "noAtual" ser a resposta
        tamanho = len(grafo[noAtual])#armazena a quantidade de filhos do "noAtual". Esse número é usado para que o while percorra os filhos do "noAtual"
        listaDeFilhos = []#após o término do while abaixo as variáveis: "listaDeFilhos", "listaDePesosFilhos", "i" e "acumulaHeuristica" são zeradas 
        listaDePesosFilhos = []
        i = 0
        acumulaHeuristica = 0

        while tamanho > i:
            listaDeFilhos.insert(0,grafo[noAtual][i])#preenche a lista de filhos do "noAtual" 
            acumulaHeuristica = pesos[noAtual][i] + heuristica[grafo[noAtual][i]][0]#soma o valor da heuristica com o peso de cada nó. Essa conta é o que define esse metodo, pois a partir dele o algoritmo escolhe o proximo nó
            listaDePesosFilhos.insert(0, acumulaHeuristica)#preenche uma lista com o peso mais a heuristica de cada nó 
            i = i + 1#i++. 

        menor = min(listaDePesosFilhos)#Escolhe o nó com o menor valor de heuristica + peso da lista
        indexMenor = listaDePesosFilhos.index(menor)#armazena o index(o numero da posição) do menor valor
        noAtual = listaDeFilhos[indexMenor]#escolhe como "noAtual" o nó com o menor valor de heuristica + peso
        caminho.append(noAtual.upper())# adiciona na lista de caminhos o próximo "noAtual"
    return caminho

print(AEstrela('a', 'g'))#chama a função principal, onde o primeiro argumento indica onde começa o caminho, e o segundo mostra o objetivo
    