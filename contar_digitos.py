def contar_digitos(num: int):
    if num == 0:
        return 0
    return 1 + contar_digitos(num // 10)


print(f"{contar_digitos(12345) = }")
print(f"{contar_digitos(333) = }")
print(f"{contar_digitos(1000) = }")
print(f"{contar_digitos(987654) = }")
