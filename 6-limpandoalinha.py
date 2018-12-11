arquivo = open('carros.txt', 'r')

texto = arquivo.readlines()

print(texto)

print("voce removeu o " + texto.pop(3))

arquivo.close()

texto.append("Maverick\n")
print(texto)

arquivo = open('carros.txt', 'w')	#abrindo de novo

arquivo.writelines(texto)

