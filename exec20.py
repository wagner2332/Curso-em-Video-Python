jogador = dict()
partidas = list()
jogador['nome'] = str(input("Nome do jogador:"))
tot = int(input(f"Quantas partidas {jogador['nome']} jogou?"))
for c in range (0, tot):
    partidas.append(int(input(f'Quantos gols foram marcados na partida {c}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print("-"*40)
print(jogador)
print("-"*40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print("-"*40)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")
for i, v in enumerate(jogador['gols']):
    print(f" => Na partida {i}, fez {v} gols")
print(f" => Foi um total de {jogador['total']} gols")