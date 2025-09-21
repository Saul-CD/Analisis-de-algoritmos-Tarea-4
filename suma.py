def suma(lista: list[int]):
    if lista == []:
        return 0

    return lista[-1] + suma(lista[:-1])


print(f"{suma([1, 2, 3, 4]) = }")
print(f"{suma([1, 2, 3, 4, 5]) = }")
print(f"{suma([0, 0, 3, 6, 9]) = }")
print(f"{suma([-4, -2, 0, 1, 3, 5]) = }")
