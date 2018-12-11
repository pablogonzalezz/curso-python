def popItem(arquivo):
	f = open(arquivo, 'r')
	lista = f.readlines()
	print(lista)
	index = input("qual item deseja remover?\n")
	print("Voce removeu o " + lista.pop(index))
	f.close()
	
	f = open(arquivo, 'w')
	f.writelines(lista)
	
	
def addItem(arquivo):
	f = open(arquivo, 'r')
	lista = f.readlines()
	print(lista)
	nome = raw_input("Digite o novo item:\n") # se a versao do python for menor q 3, usar o raw_input
	lista.append('\n' + nome)
	
	f.close()
	
	f = open(arquivo, 'w')
	f.writelines(lista)
	
def imprimirLista(arquivo):
	f = open(arquivo, 'r')
	lista = f.read()
	print("Lista: \n")
	print(lista)
	print("\n")
	f.close()
def main():
	opcao = 0
	while opcao != 4:
		print("Opcoes\n")
		print("1- Remover item\n")
		print("2- Adicionar item\n")
		print("3- Imprimir a lista\n")
		print("4- Sair\n")
		opcao = input("O que deseja fazer?")
	
		if opcao == 1:
			popItem('carros.txt')
		if opcao == 2:
			addItem('carros.txt')
		if opcao == 3:
			imprimirLista('carros.txt')
	
	
if(__name__=="__main__"):
	main()
