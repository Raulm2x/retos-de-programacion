import math


def primo(num: int) -> bool:
    """Devuelve True si el número es primo, False en caso contrario."""
    if num < 2:
        return False

    elif num < 4:
        return True

    root = math.sqrt(num)

    c = 2

    while (c <= root):
        if num % c == 0:
            return False
        c += 1

    return True

# Mostrar los numeros primos entre 1 y 100
primos = [i for i in range(1, 101) if primo(i)]
print(primos)
