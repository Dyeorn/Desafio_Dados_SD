"""Exercício I

Escreva uma função que, dado um número inteiro n, retorne uma lista
de n strings de tal forma que a string i contém i asteriscos. Por exemplo,
para n=5, a lista retornada seria ["*", "**", "***", "****", "*****"]."""

def gerar_asteriscos(n): # Criação da função passando como parametro a variavel "n".
    lista_asterisco = [] # Criação de uma lista vazia.

    for i in range(1, 1+n): # Loop começando do 1 até a variavel "n" + 1.
        asterisco = "*" * i # Multiplicação da string pela quantidade digitada.
        lista_asterisco.append(asterisco) # Implementação da string ja multiplicada na lista vazia.

    return lista_asterisco # Retornar a lista, dessa vez, sem estar vazia.


n = int(input("Digite a um número para N: ")) # Input para o usuário digitar o número desejado para a variável.

resultado = gerar_asteriscos(n) # Puxando a função passando o input como parametro.
print(resultado) # Exibindo a lista com as string já multiplicadas.


