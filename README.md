# FichasAPAMySql

ATENCION: Como este programa apunta a una base de datos local, es necesario crear la base de datos con el script de SQL que 
aparece incluido en un entorno MySql. Para poder utilizar este programa, se debe ejecutar el archivo "FichaAPABD.py", ademas de tener 
activado el servidor Xampp con MySql

Al ejecutar el programa, nos aparece el siguiente menu por la consola:

![image](https://user-images.githubusercontent.com/107152796/179368005-81cc8792-7225-421c-ad8b-f846b82243a0.png)

Dependiendo del medio el cual se quiere generar una ficha bibliografica en formato APA, elegimos una de las opciones.

Al elegir una de las dos primeras opciones, nos llevara a un menu comun para ambos, en donde tenemos a disposicion
distintas opciones:

![image](https://user-images.githubusercontent.com/107152796/179368056-acfce99e-fe0c-46d4-91ba-1f076db7a438.png)

Al elegir la primera opcion (Crear una ficha), el programa nos pedira que ingresemos la informacion del medio que 
querramos citar. En este caso, queremos generar una ficha bibliografica del libro "Harry Potter y la piedra filosofal".

![image](https://user-images.githubusercontent.com/107152796/181105207-972330e7-ce0a-4439-96d0-c6599510d814.png)


Llenamos la informacion y nos generara una ficha en formato APA:

![image](https://user-images.githubusercontent.com/107152796/179368168-da01d2d6-d28b-47cb-a9e2-eb0a99302f52.png)

Al presionar la segunda opcion, podremos ver las fichas que hemos creado. Estas fichas estan almacenadas en una base de datos:

![image](https://user-images.githubusercontent.com/107152796/179368194-3f11a488-182e-46f7-b1a9-327861780049.png)

Si queremos buscar una determinada ficha, elegiremos la tercera opcion, la cual nos dirigira a un nuevo menu en donde especificaremos
el criterio por el cual queremos buscar:

![image](https://user-images.githubusercontent.com/107152796/179368219-9d8094ab-f4a1-4343-a470-f92a164875b8.png)

En este ejemplo, veremos aquellas fichas las cuales sus libros fueron publicadas en la ciudad de Madrid. Para esto, escogemos la opcion
de "Buscar por lugar de publicacion":

![image](https://user-images.githubusercontent.com/107152796/179368257-f01223ea-9d5a-4270-a993-3db259517f6e.png)

Estando en el menu de busqueda, presionamos el numero 8 para volver al menu anterior.

Una vez en este menu, podemos eliminar una ficha. En este caso, eliminaremos la ultima ficha que creamos como ejemplo, la del libro de JK Rowling.
Para esto, se ingresa el id de la ficha que se quiere eliminar:

![image](https://user-images.githubusercontent.com/107152796/179368316-7420f850-6a9b-4cd8-9079-45dba446f275.png)

Al ver todas las fichas que tenemos, notaremos que la ficha ha sido eliminada del sistema:

![image](https://user-images.githubusercontent.com/107152796/179368343-8e8d7433-dd7f-40b1-92ac-2f2fdb1b3298.png)






