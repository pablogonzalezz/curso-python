arquivo = open('carros.txt', 'r')

linha = arquivo.readline()
print(linha)

print(arquivo.readline())
print(arquivo.readline())

arquivo.close()

arquivo = open('carros.txt', 'r')

texto = arquivo.readlines() # no plural!!!

print(texto)
print(texto[7]) 	# imprimindo a lista pelo indice
