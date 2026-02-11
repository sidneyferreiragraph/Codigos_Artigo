elementos = [1,2,3,4,5]
subconjuntos = []
contador = 0

for a in elementos:
    for b in elementos:
        if a < b:
            for c in elementos:
                if b < c:
                    subconjunto = {a,b,c}
                    subconjuntos.append(subconjunto)
        
print("Subconjuntos:", subconjuntos)
print("Quantidade:", len(subconjuntos))
