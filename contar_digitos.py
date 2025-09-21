def contar_digitos(num: int):
    if num == 0:
        return 0
    return 1 + contar_digitos(num // 10)


print(f"{contar_digitos(12345) = }")
