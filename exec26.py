def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade >= 18:
        return ("VOTO OBRIGATÓRIO")
    elif 16 <= idade < 18 or idade > 65:
        return "VOTO OPCIONAL"
    elif idade < 16:
        print("NÃO VOTA AINDA")



nasc = int(input("Em qual ano você nasceu?"))
print(voto(nasc))
