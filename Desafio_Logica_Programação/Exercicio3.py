"""Exercício III
Escreva uma função que retorne todos os subconjuntos de um conjunto
de números. Por exemplo, se a entrada for [1, 2], a saída deve ser [[], [1],
[2], [1, 2]]."""

def encontrar_subconjuntos(conjunto):
    if len(conjunto) == 0: # Caso base: conjunto vazio.
        return[[]]
    
    primeiro = conjunto[0] 

    subconjuntos_restantes = encontrar_subconjuntos(conjunto[1:]) # Encontrar subconjuntos do restante do conjunto.

    subconjuntos = [] 

    for sub in subconjuntos_restantes: # Para juntar o primeiro elemento com o restante do conjunto.

        subconjuntos.append(sub) # Adiciona os subconjuntos a lista.
        subconjuntos.append([primeiro] + sub) # Adiciona o primeiro elemento mais os subconjuntos a lista

    return subconjuntos 


conjunto = [1, 2] 
subconjuntos = encontrar_subconjuntos(conjunto) 
print(subconjuntos) 