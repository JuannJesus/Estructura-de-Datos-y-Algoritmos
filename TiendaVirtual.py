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
