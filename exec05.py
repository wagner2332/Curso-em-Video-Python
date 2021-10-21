print("-"*40)
print("LISTAGEM DE PREÇOS")
print("-"*40)
listagem = ('Lapis',1.75,
            'Borracha',2.00,
            'Caderno',15.90,
            'Estojo',25.00,
            'Compasso',10.00,
            'Mochila',120.00,
            'Canetas', 22.50,
            'Livros',35.00)
for pos in range (0,len(listagem)):
    if pos %2 ==0:
        print(f"{listagem[pos]:.<30}",end="")
    else:
        print(f"R${listagem[pos]:.>7}")
print("-"*40)        