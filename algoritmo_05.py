simbolos = ['x','y']
termos = []

for f1 in simbolos:
    for f2 in simbolos:
        for f3 in simbolos:
            for f4 in simbolos:
                for f5 in simbolos:
                    termo = (f1,f2,f3,f4,f5)	
                    if termo.count('y') == 3:
                        termos.append(termo)

print('Termos gerados: ', termos)
print('Número de termos: ', len(termos))


