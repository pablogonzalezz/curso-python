arquivo = open('carros.txt', 'r')
string = arquivo.read()
print(string)

string2 = arquivo.read()
print(string2)  	# a variavel 'arquivo' ja foi consumida
arquivo.close()

arquivo = open('carros.txt', 'r')
string3 = arquivo.read()
print(string3)
