numeros = list()
while True:
    n= int(input("Digite um numero inteiro: "))
    if n not in numeros:
        numeros.append(n)
    r= str(input("Deseja continuar? S / N  "))
    if r in 'n':
        break
print("-"*40)
print(f"Foram digitados {len(numeros)} numeros")
numeros.sort(reverse=True)
print(f"A lista no valor decrescrente igual :{numeros}")
if n ==5:
    print("Valor 5 encontrado na lista")
else:
    print("Numero 5 nao encontrado")
