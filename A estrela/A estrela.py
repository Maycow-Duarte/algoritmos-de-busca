grafo = { 
('f1'):         [('f2','f3')],
('f2,f3'):      [('f1','f4') ],
('f4'):         [('f5','f6'),('f2','f3')],
('f5','f6'):    [('f4'),('f7')],
('f7'):         [('f5','f6'),('d7','e7'),('g7','h7')],
('d7','e7'):    [('f7'),('d6','e6')],
('g7','h7'):    [('f7'),('g6','h6'),('i7')],
('d6','e6'):    [('d7','e7'),('f6')],
('g6','h6'):    [('g7','h7'),('f6'),('i6')],
('i7'):         [('g7','h7'),('i8','i9')],
('f6'):         [('d6','e6'),('g6','h6'),('f4','f5')],
('i6'):         [('g6','h6'),('i7','i8')],
('i8','i9'):    [('i7'),('h8','h9'),('i10')],
('f4','f5'):    [('f6'),('f3')],
('i7','i8'):    [('i6'),('h7','h8'),('i9')],
('h8','h9'):    [('i8','i9'),('h7')],
('i10'):        [('i8','i9'),('i11','i12')],
('f3'):         [('f4','f5'),('f1','f2')],
('h7','h8'):    [('i7','i8'),('h6'),('h9')],
('i9'):         [('i7','i8'),('i10','i11')],
('h7'):         [('h8','h9'),('f7','g7')],
('i11','i12'):  [('i10')],
('f1','f2'):    [('f3')],
('h6'):         [('h7','h8'),('f6','g6')],
('h9'):         [('h7','h8'),('i9','j9')],
('i10','i11'):  [('i9'),('j10','j11'),('l12')],
('f7','g7'):    [('h7'),('f6','g6'),('e7')],
('f6','g6'):    [('h6'),('f7','g7'),('e6')],
('i9','j9'):    [('h9'),('i10','j10')],
('j10','j11'):  [('i10','i11'),('j9')],
('l12'):        [('i10','i11'),('g12','h12')],
('e7'):         [('f7','g7')],
('e6'):         [('f6','g6')],
('i10','j10'):  [('i9','j9'),('i11','j11')],
('j9'):         [('j10','j11'),('h9','i9')],
('g12','h12'):  [('l12'),('f12')],
('i11','j11'):  [('i10','j10')],
('h9','i9'):    [('j9'),('h8','i8')],
('f12'):        [('g12','h12'),('f10','f11')],
('h8','i8'):    [('h9','i9'),('h7','i7')],
('f10','f11'):  [('f12'),('e10','e11')],
('h7','i7'):    [('h8','i8'),('h6','i6'),('g7')],
('e10','e11'):  [('f10','f11'),('d10','d11')],
('h6','i6'):    [('h7','i7'),('g6')],
('g7'):         [('h7','i7'),('e7','f7')],
('d10','d11'):  [('e10','e11'),('d9')],
('g6'):         [('h6','i6'),('e6','f6')],
('e7','f7'):    [('g7'),('e6','f6'),('d7')],
('d9'):         [('d10','d11'),('d7','d8')],
('e6','f6'):    [('e7','f7'),('d6'),('g6')],
('d7'):         [('e7','f7'),('d8','d9')],
('d7','d8'):    [('d9'),('d6')],
('d6'):         [('d7','d8'),('e6','f6')],
('d8','d9'):    [('d7'),('d10')],
('d10'):        [('d8','d9'),('e10','f10')],
('e10','f10'):  [('d10'),('e11','f11')],
('e11','f11'):  [('e10','f10'),('d11')],
('d11'):        [('e11','f11'),('d9','d10')],
('d9','d10'):   [('d11'),('d8')],
('d8'):         [('d9','d10'),('d6','d7')],
('d6','d7'):    [('d8'),('e6','e7')],
('e6','e7'):    [('d6','d7'),('f6','f7')],
('f6','f7'):    [('e6','e7'),('g6','g7'),('f5')],
('g6','g7'):    [('f6','f7'),('h6','h7')],
('f5'):         [('f6','f7'),('f3','f4')],
('h6','h7'):    [('g6','g7'),('h8'),('i6','i7')],
('f3','f4'):    [('f5'),('f2')],
('h8'):         [('h6','h7')],
('i6','i7'):    [('h6','h7'),('i8')],
('f2'):         [('f3','f4'),('d2','e2')],
('i8'):         [('i6','i7'),('i9','i10')],
('d2','e2'):    [('f2'),('c2')],
('i9','i10'):   [('i8'),('j9','j10'),('i11')],
('c2'):         [('a2','b2'),('c3','c4')],
('j9','j10'):   [('i9','i10'),('j11')],
('i11'):        [('i9','i10')],
('a2','b2'):    [('c2'),('a2','b2')],
('c3','c4'):    [('c2'),('b3','b4')],
('j11'):        [('j9','j10')],
('b3','b4'):    [('c3','c4'),('b2'),('a3','a4'),('b5')],
('b2'):         [('b3','b4'),('c2','d2')],
('a3','a4'):    [('b3','b4'),('a2'),('a5')],
('b5'):         [('b3','b4')],
('c2','d2'):    [('b2'),('e2')],
('a2'):         [('a3','a4'),('b2','c2')],
('a5'):         [('a3','a4')],
('e2'):         [('c2','d2')],
('b2','c2'):    [('a2'),('b3','c3'),('d2')],
('b3','c3'):    [('b2','c2'),('a3'),('b4','c4')],
('d2'):         [('b2','c2'),('e2','f2')],
('a3'):         [('b3','c3'),('a4','a5')],
('b4','c4'):    [('b3','c3'),('a4')],
('e2','f2'):    [('d2')],
('a4','a5'):    [('a3'),('b4','b5')],
('a4'):         [('b4','c4'),('a2','a3')],
('b4','b5'):    [('a4','a5'),('b3')],
('a2','a3'):    [('a4'),('b2','b3')],
('b3'):         [('b4','b5')],
('b2','b3'):    [('a2','a3'),('b4'),('c2','c3')],
('b4'):         [('b2','b3')],
('c2','c3'):    [('b2','b3'),('c4')],
('c4'):         [('c2','c3'),('a4','b4')],
('a4','b4'):    [('c4'),('a3','b3'),('a5','b5')],
('a3','b3'):    [('a4','b4'),('c3'),('a2','b2')],
('a5','b5'):    [('a4','b4')],
('c3'):         [('a3','b3')]             
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
    