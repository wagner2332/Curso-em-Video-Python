from time import sleep
print('Mercado o Baratao')
print('-------------------------------------------------')
total = totmil = 0
while True:
    produto = str(input('Digite o nome do produto:'))
    print('-------------------------------------------------')
    preco = float(input('Digite o valor desse produto: R$'))
    print('-------------------------------------------------')
    total += preco
    if preco > 1000:
        totmil += 1
    resposta = str(input('Gostaria de continuar? [S/N]'))
    print('-------------------------------------------------')
    if resposta == 'n':
        break
print('CALCULANDO...')
sleep(2)
print('-------------------------------------------------')
print(f'O valor total da compra foi igual a {total}')
print('-------------------------------------------------')
if (preco >= 1000):
    print(f'Temos {totmil} produto custando acima de R$ 1000,00')
print('-------------------------------------------------')