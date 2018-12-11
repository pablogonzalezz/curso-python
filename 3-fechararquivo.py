arquivo = open("carros.txt", "w")

texto = """
Lista de Carros
____________________
Gol
Celta
Fiat Uno
Gurgel
Classic
Opala
Hilux
"""

arquivo.write(texto)

arquivo.close()
