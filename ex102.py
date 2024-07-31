def factorial(n, show=False):
    """
    -> Calcula o fatorial de N
    :param n: Número a calcular o fatorial
    :param show: (Opcional) Mostrar ou não o calculo.
    :return: O valor do fatorial de N.
    """
    for i in range(n, 1, -1):
        n *= i-1
        if show:
            print(f'{i} x', end=' ')
    if show:
        print(1, end=' = ')
    return n


print('-'*25)
print(factorial(5, True))
help(factorial)
