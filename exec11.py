temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if len(princ) ==0:
         maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input("Gostaria de continuar? [S/N]"))
    if resp in 'n':
        break
print(f"\nOs dados foram {princ}")
print(f"\nAo todo, você cadastrou {len(princ)} pessoas")
print(f"\nO maior peso foi de {maior}Kg")
print(f"\nEnquanto o menor peso foi de {menor}Kg")
