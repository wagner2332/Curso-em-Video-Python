from time import sleep

def maior(*num):
    cont = maior = 0
    print("Analisando os valores passados...")
    print("-="*15)
    for valor in num:
        print(f"{valor} - ",end="", flush=True)
        sleep(0.3)
        if cont ==0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print("")
    print(f"\nForam informados {cont} valores ao todo")
    print(f"\nO maior valor informador foi {maior}")

maior(1 ,2,8,10,54,81,2000)