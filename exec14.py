from random import randint
from time import sleep
lista = list()
jogos = list()

print("-"*40)
print("         JOGO DA MEGA SENA")
print("-"*40)
quant = int(input("Informe quantos jogos gostaria de sortear: "))
print("")
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 100)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print("-="*3,f"SORTEANDO {quant} JOGOS","-="*3)
print("")
for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")
    sleep(1)
print("")
print("        BOA SORTE!!")


