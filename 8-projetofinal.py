def inserirDados(arquivo):
	f = open(arquivo, 'r')
	lista = f.readlines()
	if len(lista) != 0:
		print("Os dados ja foram inseridos, limpe a nota para inserir novamente\n")
		return
	f.close()
	
	empresa = raw_input("Qual o nome da empresa?\n")
	cnpj = raw_input("Insira o cnpj da empresa:\n")
	endereco = raw_input("Insira o endereco:\n")
	email = raw_input("Insira o email:\n")
	telefone = input("Insira um telefone:\n")
	
	lista.append(empresa + "\n")
	lista.append("CNPJ: " + str(cnpj) + "\n")
	lista.append("Endereco: " + endereco + "\n")
	lista.append("Email: " + email + "\n")
	lista.append("Telefone: " + str(telefone) + "\n")
	lista.append("\n------------Produtos------------\n")

	
	f = open(arquivo, 'w')
	f.writelines(lista)
	f.close()
	
def inserirItens(arquivo):
	f = open(arquivo, 'r')
	lista = f.readlines()
	
	produto = raw_input("Insira um produto: \n")
	preco = input("Insira o preco: \n")
	lista.append(produto + "-------" + " Valor:" + "R$: " + str(preco) + "\n")
	
	f = open(arquivo, 'w')
	f.writelines(lista)
	f.close()
	
def limparNota(arquivo):
	f = open(arquivo, 'w')
	lista = []
	f.writelines(lista)
	f.close()
	
def imprimirNota(arquivo):
	f = open(arquivo, 'r')
	nota = f.read()
	print(nota)
	f.close()
	
def limparProdutos(arquivo):
	f = open(arquivo, 'r')
	lista = f.readlines()
	remove = lista[7:]
	
	b = filter(lambda x: x not in remove, lista)
	f.close()
	
	f = open(arquivo, 'w')
	f.writelines(b)
	f.close()
	
	
def main():
	print('----------Gerador de Nota Fiscal----------')
	
	opcao = 0
	while opcao != 6:
		print("Opcoes: \n")
		print("1- Inserir Dados \n")
		print("2- Inserir Produto \n")
		print("3- Imprimir a nota \n")
		print("4- Limpar Nota \n")
		print("5- Limpar Produtos \n")
		print("6- Sair \n")
		
		opcao = input("O que deseja fazer?")
		
		if opcao == 1:
			inserirDados('notafiscal.txt')
		if opcao == 2:
			inserirItens('notafiscal.txt')
		if opcao == 3:
			imprimirNota('notafiscal.txt')
		if opcao == 4:
			limparNota('notafiscal.txt')
		if opcao == 5:
			limparProdutos('notafiscal.txt')
			
if(__name__=="__main__"):
	main()
