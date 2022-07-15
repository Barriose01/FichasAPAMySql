from conexionBD import Conexion

class QueryLibros:
    cn = Conexion("fichasLibros")

    def crearFichaLibro(self):
        while True:
            print("\nGENERADOR DE FUENTE APA PARA LIBROS:\n ")
            nombre = input("Nombre del Autor (EJ: Miguel): ")
            apellido = input("Apellido del Autor (EJ: De Cervantes): ")
            try:
                año = input("Año de publicacion (EJ: 1605): ")
                if(len(año) > 4):
                    print("Debe ingresar un año adecuado")
                    continue
            except:
                print("Debe ingresar un año adecuado")
                continue
            titulo = input("Titulo del libro (EJ: Don Quijote de La Mancha): ")
            lugar = input("Lugar de publicacion (EJ: Madrid): ")
            pais = input("Pais de publicacion (EJ: España): ")
            editorial = input("Editorial (EJ: Santillana): ")
            break

        print("\nFICHA BIBLIOGRAFICA:\n")
        if(nombre == "" and apellido == "" and año == ""):
            ficha = titulo.title() + ". (sf). " + lugar.title() + ", " + pais.title() + ": " 
            + editorial.title()
        elif(nombre == "" and apellido == ""):
            ficha = titulo.title() + ". (" + año + "). " + lugar.title() + ", " + pais.title() 
            + ": " + editorial.title()
        elif(año == ""):
            ficha = apellido.title() + ", " + nombre[0].title() + ". (sf). " + titulo.title() + ". " 
            + lugar.title() + ", " + pais.title() + ": " + editorial.title()
        else:
            ficha = apellido.title() + ", " + nombre[0].title() + " (" + año + "). " + titulo.title() + ". " + lugar.title() + ", " + pais.title() + ": " + editorial.title()
        print(ficha)
        sql = "CALL insertarFichaLibro(%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cn.cursor.execute(sql,(nombre,apellido, año,titulo,lugar,pais,editorial,ficha))
        self.cn.db.commit()
    
    #ESTE METODO ES PARA ACCEDER A OPCIONES ESPECIALES DE LAS FICHAS DE LIBROS
    def buscarLibro(self, opcion, ficha):
        if opcion == "5":
            seleccion = input("Ingrese el lugar de publicacion: ")
            self.cn.buscarCualquierCosa(ficha, "lugarPublicacion",seleccion.title().strip())
        elif opcion == "6":
            seleccion = input("Ingrese el pais de publicacion: ")
            self.cn.buscarCualquierCosa(ficha, "paisPublicacion",seleccion.title().strip())
        elif opcion == "7":
            seleccion = input("Ingrese la editorial del libro: ")
            self.cn.buscarCualquierCosa(ficha, "editorial",seleccion.title().strip())


