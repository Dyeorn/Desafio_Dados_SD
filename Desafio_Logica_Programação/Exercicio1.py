"""Exercício I

Escreva uma função que, dado um número inteiro n, retorne uma lista
de n strings de tal forma que a string i contém i asteriscos. Por exemplo,
para n=5, a lista retornada seria ["*", "**", "***", "****", "*****"]."""

def gerar_asteriscos(n): 
    lista_asterisco = [] 

    for i in range(1, 1+n): # Loop começando do 1 até a variavel "n" + 1.
        asterisco = "*" * i # Multiplicação da string pela quantidade digitada.
        lista_asterisco.append(asterisco) # Implementação da string ja multiplicada na lista vazia.

    return lista_asterisco 


n = int(input("Digite a um número para N: ")) 

resultado = gerar_asteriscos(n)
print(resultado) 

