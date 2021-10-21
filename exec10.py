galera = []
dado = []
for c in range (0,3):
    galera.append(str(input("Digite seu nome: ")))
    dado.append(int(input("Digite sua idade: ")))
    galera.append(dado[:])
    dado.clear()

print(galera)