from grafo import grafo

pilhaDeAbertos = [0]
listaDeCandidatos =[]
sucesso = False

resposta = int(input("Digite onde quer chegar: "))

#Verifica se é possivel gerar um filho inédito para o nó-candidato
def filhoInedito():
    contador = 0
    contador1 = 0
    for i in grafo[noCandidato]:                                            # Para verificar se é possivel gerar um nó-candidato dos filhos desse ponto
        contador1 = contador1 + 1                                           # é comparado o ponto com a lista de candidatos, e, para cada filho que for inédito,
        if grafo[noCandidato][contador1 - 1] not in listaDeCandidatos:      # o contador soma uma vez. Se o número do contador for maior que 1 significa que
            contador = contador + 1                                         # existe pelo menos um filho inédito possivel nesse ponto.
    return contador

#Tira o nó-candidato do topo da pilha de abertos caso esse nó-candidato não seja inédito
def tiraTopo():
    pilhaDeAbertos.pop()
    pilhaDeAbertos.insert(0,grafo[noCandidato])

#Loop principal
while sucesso == False and pilhaDeAbertos != []:
    noCandidato = pilhaDeAbertos[-1]#seleciona como nó-candidato o item do topo da pilha de abertos
    listaDeCandidatos.append(noCandidato)#registra todos os pontos que são nó-candidato
    ##print(listaDeCandidatos) mostra a evolução do caminho

    if filhoInedito() > 0:#Se filho inédito for 0 significa que não é possivel gerar um nó-candidato inédito dos filhos desse ponto
        for i in grafo[noCandidato]:#Percorre os filhos do nó-candidato procurando o primeiro filho inédito para ser um nó-candidato(de acordo com as regras do labirinto)
            if i not in listaDeCandidatos:
                noCandidato = i
                break#Quando o primeiro filho inédito é encontrado o for é parado
        if noCandidato == resposta:
            sucesso = True#Caso esse filho seja a resposta a variável "sucesso" recebe verdadeiro, o que irá gerar o término do loop principal.
            listaDeCandidatos.append(noCandidato)
        else:
            pilhaDeAbertos.append(noCandidato)#Se não for a resposta o filho inédito vira um nó-candidato.
    else:
        tiraTopo()


print(listaDeCandidatos)#Mostra o caminho percorrido

