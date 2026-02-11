simbolos = [0,1]
sequencias = []

for b1 in simbolos:
    for b2 in simbolos:
        for b3 in simbolos:
            for b4 in simbolos:
                for b5 in simbolos:
                    if b1 + b2 + b3 + b4 + b5 == 3:
                        sequencia = (b1, b2, b3, b4, b5)
                        sequencias.append(sequencia)

print('Sequências formadas: ', sequencias)
print('Quantidade de sequências: ', len(sequencias))
