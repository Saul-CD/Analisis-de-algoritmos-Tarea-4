def es_palindromo(cadena: str):
    cadena = cadena.strip().replace(" ", "").lower()
    if len(cadena) <= 1:
        return True

    return cadena[0] == cadena[-1] and es_palindromo(cadena[1: -1])


print(f"{es_palindromo('Anita lava la tina') = }")
