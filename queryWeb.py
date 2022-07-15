from conexionBD import Conexion

class QueryWeb:
    cn = Conexion("fichasWeb")

    def crearFichaWeb(self):
        while True:
            print("\nGENERADOR DE FUENTE APA PARA WEB:\n ")
            nombre = input("Nombre del Autor (EJ: Arturo): ")
            apellido = input("Apellido del Autor (EJ: Uslar): ")
            try:
                año = input("Año de publicacion (EJ: 2021 ): ")
                if(len(año) > 4):
                    print("Debe ingresar un año adecuado")
                    continue
            except:
                print("Debe ingresar un año adecuado")
                continue
            titulo = input("Titulo del articulo (EJ: Historia de Chile): ")
            fecha = input("Fecha de recuperacion (EJ: mayo 1, 2021): ")
            url = input("Enlace del articulo (EJ: wikipedia.org): ")
            break

        print("\nFICHA BIBLIOGRAFICA:\n")
        if(nombre == "" and apellido == "" and año == ""):
            ficha = titulo.title() + ". (sf). Recuperado en " + fecha + ", de " + url
        elif(nombre == "" and apellido == ""):
            ficha = titulo.title() + ". (" + año + "). Recuperado en " + fecha + ", de " + url
        elif(año == ""):
            ficha = apellido.title() + ", " + nombre[0].title() + "(sf). " + titulo.title() + ". Recuperado en " + fecha + ", de " + url
        else:
            ficha = apellido.title() + ", " + nombre[0].title() +  " (" + año + "). " + titulo.title() + ". Recuperado en " + fecha + ", de " + url
        print(ficha)
        sql = "CALL insertarFichaWeb(%s,%s,%s,%s,%s,%s,%s)"
        self.cn.cursor.execute(sql,(nombre,apellido, año,titulo,fecha,url,ficha))
        self.cn.db.commit()

    #ESTE METODO ES PARA ACCEDER A OPCIONES ESPECIALES DE LAS FICHAS WEB
    def buscarFichaWeb(self,opcion,ficha):
        if opcion == "5":
            seleccion = input("Ingrese la fecha de recuperacion (EJ: julio 12, 2022): ")
            self.cn.buscarCualquierCosa(ficha, "fechaRecuperacion", seleccion.title().strip())
        elif opcion == "6":
            seleccion = input("Ingrese el enlace de recuperacion: ")
            self.cn.buscarCualquierCosa(ficha, "enlaceRecuperacion", seleccion.title().strip())

    