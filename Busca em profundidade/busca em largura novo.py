grafo = [ [4, 1],       #0    
          [0, 5, 2],  #1
          [1], #2
          [7],  #3
          [0, 8], #4
          [1, 6],  #5
          [5, 10, 7], #6 
          [6, 3],   #7       
          [4, 12, 9], #8
          [8, 13], #9
          [6, 11], #10
          [10, 15], #11
          [8],#12
          [9,16 ,14],#13
          [13, 15, 17],#14
          [14, 11],#15
          [13],#16
          [14]#17           
        ]

resposta = None
pilhaDeAbertos = [[0]]#Armazena os caminhos em vez de apenas os nós
listaDeFechados = []
sucesso = False
while sucesso == False and pilhaDeAbertos != []:
    caminhoAtual = pilhaDeAbertos.pop(0)#Remover o primeiro caminho da lista
    noCandidato = caminhoAtual[-1]#Pegar o último nó do caminho atual
    listaDeFechados.append(noCandidato)
    for i in grafo[noCandidato]:
        if i == 17:
            sucesso = True
            caminhoAtual.append(17)#Adicionar o nó de destino ao caminho atual
            resposta = caminhoAtual#Armazenar o caminho encontrado
            break
        else:
            if i not in listaDeFechados:
                novoCaminho = caminhoAtual.copy()#Criar uma cópia do caminho atual
                novoCaminho.append(i)#Adicionar o novo nó ao caminho
                pilhaDeAbertos.append(novoCaminho)
                print(pilhaDeAbertos)
if sucesso == False:
    print("Não achou")
else:
    print("Caminho encontrado:", resposta)

