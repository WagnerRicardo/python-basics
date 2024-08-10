def notas(* nota, sit=False):
    """
        Cadastra Notas em um boletim.
    :param nota: N notas de um aluno
    :param sit: Mostrar ou não situação
    :return: boletim contendo total de notas cadastradas, maior nota, menor nota e média.
    """
    boletim = dict()

    boletim['total'] = len(nota)
    boletim['maior'] = max(nota)
    boletim['menor'] = min(nota)
    boletim['média'] = round((sum(nota) / boletim["total"]), 2)

    if sit:
        if boletim['média'] >= 7:
            boletim['situação'] = 'BOA'
        if boletim['média'] <= 6:
            boletim['situação'] = 'RAZOAVÉL'
        if boletim['média'] <= 5:
            boletim['situação'] = 'RUIM'

    return boletim


resp = notas(5.7, 5.6, 7.9, sit=True)
print(resp)
