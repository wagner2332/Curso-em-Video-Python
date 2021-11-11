from random import randint
from time import sleep

def sorteio(lista):
    print("Sorteando 5 valores da lista: ", end="")
    for cont in range (0,5):
        n = randint(1,10)
        lista.append(n)
        print(f"{n} - ",end="",flush=True)
        sleep(0.3)
    print("")
    print("\nPronto!")

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 ==0:
            soma += valor
    print(f"\nSomando os valores pares de {lista}, temos {soma}")


numeros = list()
sorteio(numeros)
somapar(numeros)

print("\nFINALIZANDO O PROGRAMA...")
sleep(3)
print("\nVOLTE SEMPRE")

