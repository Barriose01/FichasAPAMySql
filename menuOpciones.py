from conexionBD import Conexion
from queryLibros import QueryLibros
from queryWeb import QueryWeb
class Menu:
    def __init__(self, ficha):
        self.ficha = ficha
        self.bd = Conexion(self.ficha)
        self.ql = QueryLibros()
        self.qw = QueryWeb()

    def opciones(self):
        while True:
            print("\nUSTED ELIGIO: " + self.ficha)
            print("(1): Crear ficha")
            print("(2): Mostrar fichas")
            print("(3): Buscar fichas")
            print("(4): Eliminar fichas")
            print("(5): Volver")

            try:
                opcion = int(input())
                if opcion < 1 or opcion > 5:
                    print("Debe elegir una opcion valida")
            except:
                print("Debe elegir una opcion valida")
            if str(opcion).lower().strip()  == "1":
                crearFicha = self.bd.crearFicha()
                if crearFicha == "libro":
                    self.ql.crearFichaLibro()
                else:
                    self.qw.crearFichaWeb()

            elif str(opcion).lower().strip()   == "2":
                self.bd.mostrarFicha()
            elif str(opcion).lower().strip()   == "3":
                self.buscar(self.ficha)
            elif str(opcion).lower().strip()  == "4":
                self.bd.eliminarFicha()
            elif str(opcion).lower().strip()   == "5":
                break
    
    def buscar(self, ficha):
        if ficha == "fichasLibros":
            self.buscarLibro(ficha)
        else:
            self.buscarWeb(ficha)

    def buscarLibro(self,ficha):
        while True:
            print("BUSQUEDA DE FICHA")
            print("(1): Buscar por nombre del autor")
            print("(2): Buscar por apellido del autor")
            print("(3): Buscar por año de publicacion")
            print("(4): Buscar por titulo del libro")
            print("(5): Buscar por lugar de publicacion")
            print("(6): Buscar por pais de publicacion")
            print("(7): Buscar por editorial")
            print("(8): Volver")

            try:
                opcion = int(input())
                if opcion < 1 or opcion > 8:
                    print("Debe elegir una opcion valida\n")  
                    continue
            except:
                print("Debe elegir una opcion valida\n")
                continue
            if str(opcion).lower().strip()  == "8":
                break
            elif opcion < 5:
                self.bd.buscarGeneral(str(opcion).lower().strip(), ficha)
            else:
                self.ql.buscarLibro(str(opcion).lower().strip(),ficha)
    
    def buscarWeb(self, ficha):
        while True:
            print("BUSQUEDA DE FICHA")
            print("(1): Buscar por nombre del autor")
            print("(2): Buscar por apellido del autor")
            print("(3): Buscar por año de publicacion")
            print("(4): Buscar por titulo de la publicacion")
            print("(5): Buscar por fecha de recuperacion")
            print("(6): Buscar por enlace de recuperacion")
            print("(7): Volver")

            try:
                opcion = int(input())
                if opcion < 1 or opcion > 7:
                    print("Debe elegir una opcion valida\n")  
                    continue
            except:
                print("Debe elegir una opcion valida\n")
                continue
            if str(opcion).lower().strip()  == "7":
                break
            elif opcion < 5:
                self.bd.buscarGeneral(str(opcion).lower().strip(), ficha)
            else:
                self.qw.buscarFichaWeb(str(opcion).lower().strip(),ficha)
                   
