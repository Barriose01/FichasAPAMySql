from conexionBD import Conexion

class QueryLibros:
    cn = Conexion("fichasLibros")

    def recolectarInfoFichaLibros(self):
        salida = "q"
        while True:
            print("\nGENERADOR DE FUENTE APA PARA LIBROS:")
            print("Presiona (q) en cualquier momento para volver\n")
            nombre = input("Nombre del Autor (EJ: Miguel): ").strip()
            if nombre.lower() == salida:
                break
            apellido = input("Apellido del Autor (EJ: De Cervantes): ").strip()
            if apellido.lower() == salida:
                break
            try:
                año = input("Año de publicacion (EJ: 1605): ").strip()
                if año == salida:
                    break
                if(len(año) > 4):
                    print("Debe ingresar un año adecuado")
                    continue
            except:
                print("Debe ingresar un año adecuado")
                continue
            titulo = input("Titulo del libro (EJ: Don Quijote de La Mancha): ").strip()
            if titulo.lower() == salida:
                break
            lugar = input("Lugar de publicacion (EJ: Madrid): ").strip()
            if lugar.lower() == salida:
                break
            pais = input("Pais de publicacion (EJ: España): ").strip()
            if pais.lower() == salida:
                break
            editorial = input("Editorial (EJ: Santillana): ").strip()
            if editorial.lower() == salida:
                break
            self.generarFichaLibros(nombre,apellido,año,titulo,lugar,pais,editorial)
            break
    
    def generarFichaLibros(self,nombre,apellido, año,titulo,lugar,pais,editorial):
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
        self.crearFichaLibro(nombre,apellido,año,titulo,lugar,pais,editorial,ficha)

    def crearFichaLibro(self, nombre,apellido, año,titulo,lugar,pais,editorial,ficha):
        try:
            sql = "CALL insertarFichaLibro(%s,%s,%s,%s,%s,%s,%s,%s)"
            self.cn.cursor.execute(sql,(nombre,apellido, año,titulo,lugar,pais,editorial,ficha))
            self.cn.db.commit()
        except:
            print("Error al guardar la ficha en la base de datos")


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


