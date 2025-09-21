def suma(lista: list[int]):
    if lista == []:
        return 0

    return lista[-1] + suma(lista[:-1])


print(f"{suma([1, 2, 3, 4]) = }")
