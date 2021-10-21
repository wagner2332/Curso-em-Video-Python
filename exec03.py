from time import sleep
soma = cont = 0
while True:
    num = int(input('digite um valor (999 para poder parar):'))
    if num == 999:
        break
    soma += num
    cont += 1
print('Calculando...')
sleep(2)
print('A soma dos {} valores foi igual a: {}'.format(cont,soma))
print('Fim do programa')