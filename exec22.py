from time import sleep

def contador(i,f,p):
    print(f"Contagem de {i} até {f} em {p} em {p}")
    print("-="*15)

    if i < f:
        cont = i
        while cont <= f:
            print(cont , end=" ", flush=True)
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(cont ,end=" ", flush=True)
            sleep(0.5)
            cont -= p
contador(1,10,1)
print("\n")
contador(10,0,2)
print("\n")
print("Agora é sua vez de personalizar a contagem!")
print("-="*15)
ini = int(input("Início: "))
fim = int(input("Fim: "))
pas = int(input("Passo: "))
contador(ini,fim,pas)
sleep(0.5)
print("")
print("\n FIM DO PROGRAMA!")
