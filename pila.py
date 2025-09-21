class Pila:
    _pila: list

    def __init__(self, lista=[]) -> None:
        self._pila = []
        for i in lista:
            self._pila.append(i)

    def push(self, item):
        self._pila.append(item)

    def pop(self):
        return self._pila.pop()

    def seek(self):
        return self._pila[-1]

    def __len__(self):
        return len(self._pila)

    def __repr__(self) -> str:
        return repr(self._pila)


def remover_medio(pila: Pila):
    total = len(pila)

    def rec(pila):
        if len(pila) == total // 2:
            pila.pop()
            return

        item = pila.pop()
        rec(pila)
        pila.push(item)

    rec(pila)


p1 = Pila([1, 2, 3])
p2 = Pila([1, 2, 3, 4])
p3 = Pila([1, 2, 3, 4, 5])

print(f"{p1 = }")
print(f"{p2 = }")
print(f"{p3 = }")

print("Removiendo valor medio...")
remover_medio(p1)
remover_medio(p2)
remover_medio(p3)

print(f"{p1 = }")
print(f"{p2 = }")
print(f"{p3 = }")
