num = [[],[]]
valor = 0
for c in range (1,8):
    valor= int(input(f"Digite o {c}o. valor:"))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print("-"*50)
num[1].sort()
num[0].sort()
print(f"Todos os valores: {num}")
print("-"*50)
print(f"Os valores pares digitados foram: {num[0]}")
print("-"*50)
print(f"Os valores impares digitados foram: {num[1]}")
print("-"*50)
