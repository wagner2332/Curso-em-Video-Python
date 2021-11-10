def area(larg,compri):
    a = larg * compri
    print(f"A área de um terreno {larg} x {compri} é de {a} m2")


print("Controle de terrenos")
print("-="*15)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
area(l,c)
