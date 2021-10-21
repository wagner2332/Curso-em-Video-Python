from time import sleep
n1= int(input('digite o primeiro numero: '))
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
n2= int(input('digite o segundo valor agora: '))
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
opcao=0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior valor
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    opcao= int(input('Qual opcao voce deseja?'))
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    if opcao == 1:
        soma = n1 + n2
        print('O valor somado e igual a {}'.format(soma))
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print('A multiplicacao desses numeros e igual a {}'.format(multiplicacao))
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor e {}'.format(maior))
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    elif opcao == 4:
        print('Digite novos numeros: ')
        n1= int(input('Digite outro valor: '))
        n2= int(input('digite um segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Digite uma opcao valida')
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print('FIM DO PROGRAMA!')