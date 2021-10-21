total = list()
par = list()
impar = list()
while True:
    total.append( int(input("Digite um valor qualquer: ")))
    r = str(input("Deseja continuar? [S / N]"))
    if r in 'n':
        break
for i, v in enumerate(total):


    if v % 2 ==0:
     par.append(v)

    elif v % 2==1:
        impar.append(v)

print(f"Os valores digitados foram {total}")
print(f"Os numeros impares {impar}")
print(f"Os numeros pares{par}")