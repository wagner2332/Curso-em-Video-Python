aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Média de {aluno['nome']} :"))
if aluno['media'] > 7:
    aluno['situação']= 'Aprovado'
    print("")
    print("Parabéns!!")
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperacao'
    print("")
    print("Você ainda terá outra oportunidade")
else:
    aluno['situação']= 'Reprovado'
    print("")
    print("Estude mais no próximo período")
print("-"*30)
for k, v in aluno.items():
    print(f' -  {k} é igual a {v}')