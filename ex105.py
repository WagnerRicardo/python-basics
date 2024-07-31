def notas(* nota, sit=False):
    """
        Cadastra Notas em um boletim.
    :param nota: N notas de um aluno
    :param sit: Mostrar ou não situação
    :return: boletim contendo total de notas cadastradas, maior nota, menor nota e média.
    """
    boletim = dict()
    maior = menor = nota[0]
    tot = 0

    for i in nota:
        if maior <= i:
            maior = i
        if menor >= i:
            menor = i
        tot += i

    boletim['total'] = len(nota)
    boletim['maior'] = maior
    boletim['menor'] = menor
    boletim['média'] = round((tot / boletim["total"]), 2)

    if sit:
        if boletim['média'] >= 8:
            boletim['situação'] = 'BOA'
        if boletim['média'] <= 7:
            boletim['situação'] = 'RAZOAVÉL'
        if boletim['média'] <= 5:
            boletim['situação'] = 'RUIM'

    return boletim


resp = notas(5.7, 5.6, 7.9, sit=True)
print(resp)
