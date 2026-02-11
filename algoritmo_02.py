elementos = [1, 2, 3 ,4, 5]
subconjuntos = []

for i in range(len(elementos)):
    for j in range(i + 1, len(elementos)):
        for k in range(j + 1, len(elementos)):
            subconjunto = (elementos[i],elementos[j],elementos[k])
            subconjuntos.append(subconjunto)

print("Subconjuntos:", subconjuntos)
print("Quantidade:", len(subconjuntos))
