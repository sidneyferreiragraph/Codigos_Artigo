elementos = [1, 2, 3, 4, 5]
triplas = []
contador = 0

for a in elementos:
    for b in elementos:
        if b != a:
            for c in elementos:
                if c != a and c != b:
                    triplas.append((a, b, c))
                    contador += 1

print("Triplas geradas:")
for tripla in triplas:
    print(tripla)

print("\nQuantidade de triplas:", contador)
