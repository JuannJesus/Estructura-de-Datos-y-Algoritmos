# Tienda Virtual Simple de Libros (BST y Lista Enlazada Simple)

**Curso:** Estructura de Datos y Algoritmos  
**Institucion:** Tecsup  
**Lenguaje:** Python 3 (sin librerias externas)  

---

## 1. Integrantes y Division del Trabajo

* **Juan Jesus Huanay Izquierdo (Bloque 1 - Catalogo BST):** Implementacion de la clase `Libro`, estructura del nodo `NodoBST`, insercion recursiva por ISBN, busqueda binaria, eliminacion (por ISBN y por titulo) y recorrido In-Order.
* **Mauricio Justo Martinez Cueva (Bloque 2 - Carrito, Compras y Reportes):** Implementacion de la Lista Enlazada Simple (`NodoCarrito`), menu interactivo en consola, validacion de stock antes de comprar, descuento de inventario y reportes estadisticos.

---

## 2. Introduccion y Problematica

En una tienda de libros en linea, almacenar el catalogo en listas simples vuelve lenta la busqueda a medida que crece el inventario, y procesar ventas sin verificar disponibilidad genera errores de stock negativo.

**Solucion implementada:**
1. **Arbol Binario de Busqueda (BST):** Organiza los libros por su codigo **ISBN** unico, permitiendo localizar productos rapidamente y listar todo el catalogo ordenado de menor a mayor mediante un recorrido **In-Order**.
2. **Lista Enlazada Simple:** Gestiona dinamicamente los articulos del carrito de compras mediante nodos conectados con punteros `next`, validando el stock disponible antes de confirmar cualquier venta.

---

## 3. Modelo y Funcionamiento de las Estructuras

### 3.1. Campos del Nodo del Catalogo (`Libro` y `NodoBST`)

| Campo | Tipo | Proposito | Ejemplo |
| :--- | :--- | :--- | :--- |
| `isbn` | `str` | Clave unica de ordenamiento en el BST | `"101"` |
| `titulo` | `str` | Nombre del libro | `"Estructuras de Datos"` |
| `autor` | `str` | Autor de la obra | `"Luis Melendez"` |
| `precio` | `float` | Precio unitario en soles | `70.0` |
| `stock` | `int` | Unidades disponibles en inventario | `4` |
| `categoria` | `str` | Clasificacion tematica | `"Programacion"` |
| `left` | `NodoBST` | Enlace al subarbol con ISBN menores | `None` o nodo |
| `right` | `NodoBST` | Enlace al subarbol con ISBN mayores | `None` o nodo |

### 3.2. Regla de Organizacion del BST

    [103] Python Facil -> Raiz
    Izquierda (left): [101] Estructuras -> Derecha de 101: [102] Cien Anos
    Derecha (right): [104] Clean Code

Con el recorrido **In-Order** (`izquierda -> raiz -> derecha`), el catalogo se imprime automaticamente ordenado por codigo: `101, 102, 103, 104`.

### 3.3. Carrito de Compras (`NodoCarrito`)

    [carrito] ---> [Libro 101 | Cant: 2 | next] ---> [Libro 103 | Cant: 1 | next] ---> None

---

## 4. Funcionalidades Implementadas

| Opcion / Modulo | Funcionalidad | Estructura utilizada |
| :--- | :--- | :--- |
| **Opcion 1** | Ver catalogo completo ordenado por ISBN | Arbol BST (Recorrido In-Order) |
| **Opcion 2** | Buscar libro por ISBN, titulo, autor o categoria | Busqueda binaria BST / Recorrido |
| **Opcion 3** | Agregar libro al carrito validando stock disponible | Lista Enlazada Simple (`NodoCarrito`) |
| **Opcion 4** | Confirmar compra (valida stock, descuenta y calcula total) | Recorrido `while` sobre Lista Enlazada |
| **Opcion 5** | Reportes (mas caro, mas barato, sin stock, total por categoria y valor inventario) | Recorrido In-Order del BST |
| **Funciones Admin** | Actualizar stock/precio por ISBN, eliminar por titulo y filtro por rango de precios | Operaciones sobre nodos BST |

---

## 5. Complejidad Temporal (Big O)

Siendo `n` la cantidad de libros en el catalogo y `h` la altura del arbol:

| Operacion | BST Equilibrado | Peor Caso |
| :--- | :---: | :---: |
| Insertar libro (`insertar`) | O(log n) | O(n) |
| Buscar por ISBN (`buscar_isbn`) | O(log n) | O(n) |
| Eliminar libro (`eliminar`) | O(log n) | O(n) |
| Listar catalogo ordenado (`listar_inorder`) | O(n) | O(n) |
| Insertar en carrito (`NodoCarrito`) | O(1) | O(1) |
| Confirmar compra (recorrer carrito) | O(m) | O(m) |

*(Nota: `m` representa la cantidad de items agregados al carrito de compras).*

---

## 6. Ejecucion del Programa

1. Verificar que Python 3 este instalado en el sistema ejecutando: `python --version`
2. Ejecutar el archivo principal desde la terminal en la carpeta del proyecto: `python TiendaVirtual.py`
3. Seleccionar las opciones del menu para consultar el catalogo, buscar libros, gestionar el carrito, confirmar compras y revisar los reportes.

---

## 7. Evidencia de Ejecucion

    --- TIENDA DE LIBROS ---
    1. Ver catalogo
    2. Buscar libro
    3. Agregar al carrito
    4. Confirmar compra
    5. Ver reportes
    0. Salir
    Opcion: 1
      [101] Estructuras de Datos | Luis Melendez | Programacion | S/.70.0 | Stock: 4
      [102] Cien Anos de Soledad | Garcia Marquez | Literatura | S/.50.0 | Stock: 8
      [103] Python Facil | Juan Perez | Programacion | S/.45.0 | Stock: 6
      [104] Clean Code | Robert Martin | Programacion | S/.85.0 | Stock: 3

---

## 8. Conclusiones

1. El uso de un **Arbol Binario de Busqueda (BST)** permite mantener el catalogo ordenado por ISBN desde el momento de la insercion y realizar busquedas eficientes sin recorrer toda la coleccion.
2. La **Lista Enlazada Simple** facilita la gestion dinamica del carrito de compras mediante punteros `next`, permitiendo agregar productos y validar el inventario en tiempo real antes de confirmar una transaccion.
