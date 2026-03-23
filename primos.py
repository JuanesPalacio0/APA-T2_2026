"""

Autor: Juan Esteban Palacio 


Este módulo proporciona funciones para trabajar con números primos, incluyendo:
- Determinación de primalidad.
- Generación de primos menores que un número dado.
- Descomposición en factores primos.
- Cálculo del mínimo común múltiplo (mcm) y el máximo común divisor (mcd).

Tests unitarios:
>>> [numero for numero in range(2, 50) if es_primo(numero)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)
>>> mcm(90, 14)
630
>>> mcd(924, 780)
12
>>> mcmN(42, 60, 70, 63)
1260
>>> mcdN(840, 630, 1050, 1470)
210
"""
from functools import reduce

def es_primo(numero):
    """Devuelve True si el número es primo, False en caso contrario."""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos(numero):
    """Devuelve una tupla con todos los números primos menores que el argumento."""
    return tuple(n for n in range(2, numero) if es_primo(n))

def descompon(numero):
    """Devuelve una tupla con la descomposición en factores primos del argumento."""
    factores = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    return tuple(factores)

def mcm(numero1, numero2):
    """Devuelve el mínimo común múltiplo de dos números."""
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores_comunes = set(factores1) | set(factores2)
    resultado = 1
    for factor in factores_comunes:
        resultado *= factor ** max(factores1.count(factor), factores2.count(factor))
    return resultado

def mcd(numero1, numero2):
    """Devuelve el máximo común divisor de dos números."""
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores_comunes = set(factores1) & set(factores2)
    resultado = 1
    for factor in factores_comunes:
        resultado *= factor ** min(factores1.count(factor), factores2.count(factor))
    return resultado

def mcmN(*numeros):
    """Devuelve el mínimo común múltiplo de varios números."""
    return reduce(mcm, numeros)

def mcdN(*numeros):
    """Devuelve el máximo común divisor de varios números."""
    return reduce(mcd, numeros)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
