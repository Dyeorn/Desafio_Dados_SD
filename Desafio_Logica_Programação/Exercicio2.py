"""Exercício II
Dado um array de números inteiros, escreva uma função que retorne o
par de números com a menor diferença absoluta. Se houver mais de um
par com a mesma diferença, retorne todos eles em uma lista. Por
exemplo, para o array [3, 8, 50, 5, 1, 18, 12], a função deve retornar
[(3, 1), (8, 5)]."""

def encontrar_diferenca(array): 
    array.sort()

    menor_diferenca = float('inf')
    pares_menor_diferenca = []

    # Itera pelo array para encontrar a menor diferença.
    for i in range(len(array) - 1):
        # Calcula a diferença absoluta entre elementos adjacentes.
        diferenca = abs(array[i] - array[i + 1])

        # Verifica se a diferença é menor que a menor diferença atual.
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            pares_menor_diferenca = [(array[i], array[i + 1])]

        # Se a diferença for igual à menor diferença atual, adiciona o par à lista.
        elif diferenca == menor_diferenca:
            pares_menor_diferenca.append((array[i], array[i + 1]))


    return pares_menor_diferenca


array = [3, 8, 50, 5, 1, 18, 12] 
resultado = encontrar_diferenca(array)  
print(resultado) 