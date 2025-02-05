def min_galoes(L):
    g10 = L // 10  # Quantos galões de 10 litros usar
    L %= 10        # O que sobra após usar os de 10 litros

    g4 = L // 4    # Quantos galões de 4 litros usar
    L %= 4         # O que sobra após usar os de 4 litros

    g1 = L         # O restante será preenchido com galões de 1 litro

    return g10 + g4 + g1

# Entrada
L = int(input())
print(min_galoes(L))
