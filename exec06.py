palavras = ('aprender','programacao','python','curso','estudar','praticar','trabalhar')
for p in palavras:
    print(f"\nNa palavra {p} temos ", end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra,"-",end='')