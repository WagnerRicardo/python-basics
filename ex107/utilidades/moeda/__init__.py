def aumentar(n, p, formatado=False):
    n = n + (n * (p / 100))
    return n if not formatado else moeda(n)


def diminuir(n, p, formatado=False):
    n = n - (n * (p/100))
    return n if not formatado else moeda(n)


def dobro(n, formatado=False):
    n = n * 2
    return n if not formatado else moeda(n)


def metade(n, formatado=False):
    n = n / 2
    return n if not formatado else moeda(n)


def moeda(n, currency='R$'):
    n = f'{n:.2f}'
    inteiro = n.split('.')[0]
    decimal = n.split('.')[1]

    return f'{currency} {inteiro},{decimal}'


def resumo(p, a, r):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço analisado:":<20}{moeda(p)}')
    print(f'{"Dobro do preço:":<20}{dobro(p, True)}')
    print(f'{"Metade do preço:":<20}{metade(p, True)}')
    print(f'{f"{a}% de aumento:":<20}{aumentar(p, a, True)}')
    print(f'{f"{r}% de redução: ":<20}{diminuir(p, r, True)}')
    print('-'*30)

