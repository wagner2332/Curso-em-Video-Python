numeros = list()
while True:
    n= int(input("\nDigite um valor: "))
    if n not in numeros:
        numeros.append(n)
        print("\nValor adicionado com sucesso!")
    else:
        print("\nValor duplicado! Nao irei adicionar")
    r= str(input("\nDeseja continuar? S/N "))
    if r in 'n':
        break
print("-"*40)
numeros.sort()
print(f"\nVoce digitou os valores {numeros}")