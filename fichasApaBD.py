from menuOpciones import Menu

while True:
	print("\nElegir el medio que se quiere citar: ")
	print("(1): Web")
	print("(2): Libro")
	print("(3): Salir")
	opcion = input()
	if opcion.lower().strip() == "3":
		break
	elif opcion.lower().strip() == "1":
		menu = Menu("fichasWeb")
		menu.opciones()
	elif opcion.lower().strip() == "2":
		menu = Menu("fichasLibros")
		menu.opciones()
	
