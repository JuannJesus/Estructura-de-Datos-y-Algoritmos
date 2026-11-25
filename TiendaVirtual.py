# BLOQUE 1 - MODELOS Y ARBOL BST (CATALOGO)

# 1. Molde del Libro con los 6 datos obligatorios
class Libro:
    def __init__(self, isbn, titulo, autor, precio, stock, categoria):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def __str__(self):
        return "[" + self.isbn + "] " + self.titulo + " | " + self.autor + " | " + self.categoria + " | S/." + str(self.precio) + " | Stock: " + str(self.stock)


# 2. Nodo del Arbol Binario de Busqueda (BST)
class NodoBST:
    def __init__(self, libro):
        self.libro = libro
        self.left = None   # Aqui van los ISBN menores
        self.right = None  # Aqui van los ISBN mayores


# 3. Insertar libro respetando el orden del BST
def insertar(raiz, libro):
    if raiz is None:
        return NodoBST(libro)
    if libro.isbn < raiz.libro.isbn:
        raiz.left = insertar(raiz.left, libro)
    elif libro.isbn > raiz.libro.isbn:
        raiz.right = insertar(raiz.right, libro)
    return raiz


# 4. Busqueda rapida por codigo ISBN
def buscar_isbn(raiz, isbn):
    if raiz is None:
        return None
    if raiz.libro.isbn == isbn:
        return raiz.libro
    if isbn < raiz.libro.isbn:
        return buscar_isbn(raiz.left, isbn)
    return buscar_isbn(raiz.right, isbn)


# 5. Funciones para eliminar un libro del arbol
def minimo(nodo):
    while nodo.left is not None:
        nodo = nodo.left
    return nodo

def eliminar(raiz, isbn):
    if raiz is None:
        return None
    if isbn < raiz.libro.isbn:
        raiz.left = eliminar(raiz.left, isbn)
    elif isbn > raiz.libro.isbn:
        raiz.right = eliminar(raiz.right, isbn)
    else:
        if raiz.left is None:
            return raiz.right
        if raiz.right is None:
            return raiz.left
        temp = minimo(raiz.right)
        raiz.libro = temp.libro
        raiz.right = eliminar(raiz.right, temp.libro.isbn)
    return raiz

# Eliminar libro por titulo
def eliminar_titulo(raiz, titulo):
    lista = []
    listar_inorder(raiz, lista)
    for l in lista:
        if l.titulo == titulo:
            return eliminar(raiz, l.isbn)
    return raiz


# 6. Recorrido In-Order (izquierda -> raiz -> derecha) para sacar lista ordenada
def listar_inorder(raiz, lista):
    if raiz is not None:
        listar_inorder(raiz.left, lista)
        lista.append(raiz.libro)
        listar_inorder(raiz.right, lista)



# BLOQUE 2 - CARRITO, MENU, COMPRAS Y REPORTES

# 1. Nodo de la Lista Enlazada Simple para el Carrito
class NodoCarrito:
    def __init__(self, libro, cantidad):
        self.libro = libro
        self.cantidad = cantidad
        self.next = None   # Puntero al siguiente libro del carrito


def mostrar_carrito(carrito):
    if carrito is None:
        print("Carrito vacio.")
        return
    print("\n--- CARRITO ACTUAL ---")
    actual = carrito
    total = 0
    while actual is not None:
        subtotal = actual.libro.precio * actual.cantidad
        total = total + subtotal
        print("* " + actual.libro.titulo + " x" + str(actual.cantidad) + " -> S/." + str(subtotal))
        actual = actual.next
    print("Subtotal carrito: S/." + str(total))


def quitar_del_carrito(carrito, isbn):
    actual = carrito
    anterior = None
    while actual is not None:
        if actual.libro.isbn == isbn:
            if anterior is None:
                return actual.next, True
            anterior.next = actual.next
            return carrito, True
        anterior = actual
        actual = actual.next
    return carrito, False


# 2. Inicializamos la raiz del arbol y la cabeza del carrito
raiz = None
carrito = None

# Cargamos los libros base en orden balanceado (103 como raiz)
raiz = insertar(raiz, Libro("103", "Python Facil", "Juan Perez", 40.0, 6, "Programacion"))
raiz = insertar(raiz, Libro("101", "Estructuras de Datos", "Luis Melendez", 70.0, 4, "Programacion"))
raiz = insertar(raiz, Libro("102", "Cien Anos de Soledad", "Garcia Marquez", 50.0, 5, "Literatura"))
raiz = insertar(raiz, Libro("104", "Clean Code", "Robert Martin", 85.0, 3, "Programacion"))
raiz = insertar(raiz, Libro("105", "El Principito", "Saint-Exupery", 25.0, 0, "Literatura"))

# Pruebas administrativas estaticas (Actualizar stock, precio y eliminar por titulo)
libro_102 = buscar_isbn(raiz, "102")
if libro_102 is not None:
    libro_102.stock = 8

libro_103 = buscar_isbn(raiz, "103")
if libro_103 is not None:
    libro_103.precio = 45.0

raiz = eliminar_titulo(raiz, "El Principito")

# Prueba estatica de busqueda por rango de precios (S/.40 a S/.75)
print("--- RANGO DE PRECIOS (S/.40 - S/.75) ---")
lista_rango = []
listar_inorder(raiz, lista_rango)
for l in lista_rango:
    if l.precio >= 40 and l.precio <= 75:
        print(" ", l)

# Prueba estatica del carrito (modificar cantidad, calcular total y vaciar)
libro_101 = buscar_isbn(raiz, "101")
if libro_101 is not None:
    carrito_prueba = NodoCarrito(libro_101, 1)
    carrito_prueba.cantidad = 2
    print("Total carrito prueba: S/." + str(carrito_prueba.libro.precio * carrito_prueba.cantidad))
    carrito_prueba = None


# 3. Menu
while True:
    print("\n--- TIENDA DE LIBROS ---")
    print("1. Ver catalogo")
    print("2. Buscar libro")
    print("3. Agregar al carrito")
    print("4. Ver carrito")
    print("5. Quitar libro del carrito")
    print("6. Confirmar compra")
    print("7. Ver reportes")
    print("0. Salir")
    op = input("Opcion: ").strip()

    # Opcion 1: Mostrar todos los libros ordenados por ISBN
    if op == "1":
        lista = []
        listar_inorder(raiz, lista)
        if not lista:
            print("No hay libros en el catalogo.")
        else:
            for l in lista:
                print(" ", l)

    # Opcion 2: Buscar por ISBN o por texto exacto
    elif op == "2":
        dato = input("Escribe ISBN (ej: 101) o texto exacto (titulo/autor/categoria): ").strip()
        libro = buscar_isbn(raiz, dato)
        if libro is not None:
            print(" ", libro)
        else:
            lista = []
            listar_inorder(raiz, lista)
            encontrados = [
                l for l in lista
                if dato == l.titulo or dato == l.autor or dato == l.categoria
            ]
            if encontrados:
                for l in encontrados:
                    print(" ", l)
            else:
                print("No se encontraron coincidencias.")

    # Opcion 3: Insertar nodo al inicio de la lista enlazada del carrito
    elif op == "3":
        isbn = input("Codigo ISBN (101, 102, 103 o 104): ").strip()
        libro = buscar_isbn(raiz, isbn)
        if libro is None:
            print("Codigo no existe.")
            continue
        try:
            cant = int(input("Cantidad (Stock disponible " + str(libro.stock) + "): "))
        except ValueError:
            print("Error: ingrese un numero entero.")
            continue

        if cant > 0 and cant <= libro.stock:
            nuevo = NodoCarrito(libro, cant)
            nuevo.next = carrito
            carrito = nuevo
            print("Agregado al carrito.")
        else:
            print("Stock insuficiente.")

    # Opcion 4: Ver carrito
    elif op == "4":
        mostrar_carrito(carrito)

    # Opcion 5: Quitar libro del carrito
    elif op == "5":
        if carrito is None:
            print("Carrito vacio.")
            continue
        isbn = input("Codigo ISBN a quitar del carrito: ").strip()
        carrito, quitado = quitar_del_carrito(carrito, isbn)
        if quitado:
            print("Libro eliminado del carrito.")
        else:
            print("Codigo no encontrado en el carrito.")

    # Opcion 6: Recorrer lista enlazada, validar stock y descontar
    elif op == "6":
        if carrito is None:
            print("Carrito vacio.")
            continue

        actual = carrito
        ok = True
        while actual is not None:
            if actual.cantidad > actual.libro.stock:
                ok = False
            actual = actual.next

        if ok:
            actual = carrito
            total = 0
            while actual is not None:
                actual.libro.stock = actual.libro.stock - actual.cantidad
                total = total + (actual.libro.precio * actual.cantidad)
                print("* " + actual.libro.titulo + " x" + str(actual.cantidad))
                actual = actual.next
            carrito = None
            print("Compra lista. Total: S/." + str(total))
        else:
            print("Error: sin stock suficiente.")

    # Opcion 7: Reportes recorriendo la lista ordenada
    elif op == "7":
        lista = []
        listar_inorder(raiz, lista)
        if not lista:
            print("No hay libros para generar reportes.")
            continue

        caro = lista[0]
        barato = lista[0]
        valor_total = 0
        prog = 0
        lit = 0

        for l in lista:
            if l.precio > caro.precio:
                caro = l
            if l.precio < barato.precio:
                barato = l
            if l.stock == 0:
                print("Sin stock: " + l.titulo)
            if l.categoria == "Programacion":
                prog = prog + l.stock
            if l.categoria == "Literatura":
                lit = lit + l.stock
            valor_total = valor_total + (l.precio * l.stock)

        print("Mas caro: " + caro.titulo + " (S/." + str(caro.precio) + ")")
        print("Mas barato: " + barato.titulo + " (S/." + str(barato.precio) + ")")
        print("Total libros Programacion: " + str(prog))
        print("Total libros Literatura: " + str(lit))
        print("Valor total inventario: S/." + str(valor_total))

    elif op == "0":
        print("Saliendo...")
        break
    else:
        print("Opcion invalida.")
