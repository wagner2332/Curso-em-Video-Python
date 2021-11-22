def notas(*n, sit = False):
    """
   ->Função para analisar notas e situações de vários alunos.
   :param n: Uma ou mais notas dos alunos.
   :param sit: Valor opcional indicando se deve ou não adicionar a situação.
   :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/ len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(5.5,2.5,9,8,sit=True)
print(resp)
help(notas)