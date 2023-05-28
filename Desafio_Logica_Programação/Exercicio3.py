"""Exercício III
Escreva uma função que retorne todos os subconjuntos de um conjunto
de números. Por exemplo, se a entrada for [1, 2], a saída deve ser [[], [1],
[2], [1, 2]]."""

def encontrar_subconjuntos(conjunto): # Criação da função com parametro 'conjunto'.
    if len(conjunto) == 0: # Caso base: conjunto vazio.
        return[[]]
    
    primeiro = conjunto[0] # Variavel para obter o primeiro elemento do conjunto.

    subconjuntos_restantes = encontrar_subconjuntos(conjunto[1:]) # Encontrar subconjuntos do restante do conjunto.

    subconjuntos = [] # Criação de uma lista vazia para receber os subconjuntos.

    for sub in subconjuntos_restantes: # Para juntar o primeiro elemento com o restante do conjunto.

        subconjuntos.append(sub) # Adiciona os subconjuntos a lista.
        subconjuntos.append([primeiro] + sub) # Adiciona o primeiro elemento mais os subconjuntos a lista

    return subconjuntos # Retorna a lista, dessa vez, com os elementos.


conjunto = [1, 2] # Variável com o conjunto desejado.
subconjuntos = encontrar_subconjuntos(conjunto) # Puxando a função com os valores da variável.
print(subconjuntos) # Exibindo a lista com o resultado desejado.