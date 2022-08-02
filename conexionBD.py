import mysql.connector

class Conexion:
    try:
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            database = "APAFichas"
        )
        cursor = db.cursor(buffered=True)
    except:
        print("Error de conexion a la base de datos")

    def __init__(self, ficha):
        self.ficha = ficha
     
    def crearFicha(self):
        print(self.ficha)
        if self.ficha == "fichasLibros":
            return "libro"
        elif self.ficha == "fichasWeb":
            return "web"

    def mostrarFicha(self):
        try:
            fichas = self.obtenerFicha()
            if len(fichas) > 0:
                for x in fichas:
                    print("-" + str(x))
            else:
                print("No hay fichas para mostrar")
        except:
            print("Error al mostrar las fichas")

    def eliminarFicha(self):
        try:
            while True:
                fichas = self.obtenerFicha()
                if len(fichas) > 0:
                    print()
                    for a in fichas:
                        print(a)
                    print("(q): Volver \n")
                    try:
                        opcion = input("Ingrese el id de la ficha a eliminar: ")
                        if opcion.lower().strip()  == "q":
                            break
                        else:
                            self.eliminarFichaConId(opcion)
                    except:
                        print("Debe ingresar una opcion valida")
                        continue
                else:
                    print("No hay fichas para eliminar")
                    break
        except:
            print("Error al eliminar las fichas")
            
    def eliminarFichaConId(self,id):
        elId = self.obtenerID()
        listaId = []
        #POR CADA ELEMENTO t EN LA TUPLA elId, GENERADA POR LOS ID RECUPERADOS
        for t in elId:
            #CADA ELEMENTO QUE SE INGRESE SERA UNA TUPLA DE UN SOLO VALOR
            listaId.append(t)
        #CONVERTIR EL id INGRESADO EN LA FUNCION A TUPLA (LO SAQUE DE INTERNET)
        idTupla = tuple(map(int, id.split(', ')))
        if idTupla in listaId:
            self.cursor.execute("DELETE FROM " + self.ficha + " WHERE id = " + id)
            self.db.commit()
            print("La ficha ha sido eliminada con exito")
        else:
            print("Ingrese una opcion valida")

    #ESTE METODO SE USA TANTO PARA ENCONTRAR FICHAS PARA LIBROS O WEB
    def buscarGeneral(self, opcion, ficha):
        if opcion == "1":
            seleccion = input("Ingrese el nombre del autor: ")
            self.buscarCualquierCosa(ficha, "nombre",seleccion.title().strip())
        elif opcion == "2":
            seleccion = input("Ingrese el apellido del autor: ")
            self.buscarCualquierCosa(ficha, "apellido",seleccion.title().strip())
        elif opcion == "3":
            while True:
                try:
                    seleccion = int(input("Ingrese el año de publicacion: "))
                except:
                    print("Ingrese un año valido")
                    continue
                break
            self.buscarCualquierCosa(ficha, "ano",str(seleccion).title().strip())
        elif opcion == "4":
            seleccion = input("Ingrese el titulo de la publicacion: ")
            self.buscarCualquierCosa(ficha, "titulo",seleccion.title().strip())

    def buscarCualquierCosa(self, ficha, opcion, seleccion):
        fichas = []
        try:
            self.cursor.execute("SELECT ficha FROM " + ficha + " WHERE " + opcion + " LIKE '%" + seleccion + "%'")
            for x in self.cursor:
                fichas.append(x)
            print("Resultados para '" + seleccion + "': ")
            if len(fichas) > 0:
                for ficha in fichas:
                    print(ficha)
            else:
                print("No hay fichas para mostrar")
        except:
            print("Error al buscar ficha")
    
    def obtenerID(self):
        try:
            self.cursor.execute("SELECT id FROM " + self.ficha)
            return self.cursor
        except:
            print("Error al obtener id de la ficha")

    def obtenerFicha(self):
        fichas = []
        self.cursor.execute("SELECT id, ficha FROM " + self.ficha)
        for ficha in self.cursor:
            fichas.append(ficha)
        return fichas
        
