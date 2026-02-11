passos = ['D','C']
caminhos = []

for p1 in passos:
    for p2 in passos:
        for p3 in passos:
            for p4 in passos:
                for p5 in passos:
                    caminho = (p1,p2,p3,p4,p5)	
                    if caminho.count('D') == 2:
                        caminhos.append(caminho)

print('Caminhos gerados: ', caminhos)
print('Número de caminhos: ', len(caminhos))
