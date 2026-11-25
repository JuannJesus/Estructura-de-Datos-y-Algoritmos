# Tienda Virtual Simple de Libros (BST y Lista Enlazada Simple)

**Curso:** Estructura de Datos y Algoritmos  
**Institucion:** Tecsup  
**Lenguaje:** Python 3 (sin librerias externas)  

---

## 1. Integrantes y Division del Trabajo

- **Juan Jesus Huanay Izquierdo (Bloque 1 - Catalogo BST):** Implementacion de la clase `Libro`, estructura del nodo `NodoBST`, insercion recursiva por ISBN, busqueda binaria, eliminacion (por ISBN y por titulo) y recorrido In-Order.
- **Mauricio Justo Martinez Cueva (Bloque 2 - Carrito, Compras y Reportes):** Implementacion de la Lista Enlazada Simple (`NodoCarrito`), visualizacion y eliminacion de nodos en el carrito (`mostrar_carrito`, `quitar_del_carrito`), menu interactivo en consola, validacion de stock antes de comprar, descuento de inventario y reportes estadisticos.

---

## 2. Introduccion y Problematica

En una tienda de libros en linea, almacenar el catalogo en listas simples vuelve lenta la busqueda a medida que crece el inventario, y procesar ventas sin verificar disponibilidad genera errores de stock negativo.

**Solucion implementada:**
1. **Arbol Binario de Busqueda (BST):** Organiza los libros por su codigo **ISBN** unico, permitiendo localizar productos rapidamente y listar todo el catalogo ordenado de menor a mayor mediante un recorrido **In-Order**.
2. **Lista Enlazada Simple:** Gestiona dinamicamente los articulos del carrito de compras mediante nodos conectados con punteros `next`, permitiendo agregar, visualizar, quitar items y validar el stock disponible antes de confirmar cualquier venta.

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

![Arbolito](https://github.com/user-attachments/assets/0dc16868-364a-4247-88b0-585772db2165)

Para evitar que el arbol degenere en una lista inclinada, los libros base se insertan comenzando por el codigo intermedio (`"103"` como raiz), seguido de `"101"`, `"102"`, `"104"` y `"105"`. Con el recorrido **In-Order** (`izquierda -> raiz -> derecha`), el catalogo se imprime automaticamente ordenado de menor a mayor: `101, 102, 103, 104`.

### 3.3. Carrito de Compras (`NodoCarrito`)

![carrito](https://github.com/user-attachments/assets/8d2c1db8-12f6-4d1b-a878-9891a2ebc071)

Cada libro agregado al carrito crea un NodoCarrito que se enlaza al inicio de la lista apuntando al nodo anterior mediante next (con el ultimo nodo apuntando a None). Esto permite recorrer los items para mostrar subtotales, quitar productos reacomodando punteros o validar todo el stock antes de confirmar la compra
---

## 4. Funcionalidades Implementadas

| Opcion / Modulo | Funcionalidad | Estructura utilizada |
| :--- | :--- | :--- |
| **Opcion 1** | Ver catalogo completo ordenado por ISBN | Arbol BST (Recorrido In-Order) |
| **Opcion 2** | Buscar libro por ISBN o coincidencia exacta (titulo, autor, categoria) | Busqueda binaria BST / Recorrido In-Order |
| **Opcion 3** | Agregar libro al carrito validando stock disponible | Insercion al inicio en Lista Enlazada (`NodoCarrito`) |
| **Opcion 4** | Ver carrito (muestra items acumulados, subtotales y total) | Recorrido `while` (`mostrar_carrito`) |
| **Opcion 5** | Quitar libro del carrito por ISBN | Reenlace de punteros `next` (`quitar_del_carrito`) |
| **Opcion 6** | Confirmar compra (valida stock, descuenta unidades y vacia carrito) | Recorrido `while` sobre Lista Enlazada |
| **Opcion 7** | Reportes (mas caro, mas barato, sin stock, stock por categoria y valor inventario) | Recorrido In-Order del BST |
| **Pruebas Iniciales** | Actualizacion de stock/precio por ISBN, eliminacion por titulo (`105`) y filtro por rango de precios | Operaciones directas sobre nodos BST |

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
| Ver / Quitar / Confirmar compra en carrito | O(m) | O(m) |

*(Nota: `m` representa la cantidad de items agregados al carrito de compras).*

---

## 6. Ejecucion del Programa

1. Verificar que Python 3 este instalado en el sistema ejecutando: `python --version`
2. Ejecutar el archivo principal desde la terminal en la carpeta del proyecto: `python TiendaVirtual.py`
3. Revisar las pruebas administrativas iniciales en consola y seleccionar las opciones del menu (`1` al `7`, o `0` para salir).

---

## 7. Evidencia de Ejecucion

    --- RANGO DE PRECIOS (S/.40 - S/.75) ---
      [101] Estructuras de Datos | Luis Melendez | Programacion | S/.70.0 | Stock: 4
      [102] Cien Anos de Soledad | Garcia Marquez | Literatura | S/.50.0 | Stock: 8
      [103] Python Facil | Juan Perez | Programacion | S/.45.0 | Stock: 6
    Total carrito prueba: S/.140.0

    --- TIENDA DE LIBROS ---
    1. Ver catalogo
    2. Buscar libro
    3. Agregar al carrito
    4. Ver carrito
    5. Quitar libro del carrito
    6. Confirmar compra
    7. Ver reportes
    0. Salir
    Opcion: 1
      [101] Estructuras de Datos | Luis Melendez | Programacion | S/.70.0 | Stock: 4
      [102] Cien Anos de Soledad | Garcia Marquez | Literatura | S/.50.0 | Stock: 8
      [103] Python Facil | Juan Perez | Programacion | S/.45.0 | Stock: 6
      [104] Clean Code | Robert Martin | Programacion | S/.85.0 | Stock: 3

---

## 8. Conclusiones

1. El uso de un **Arbol Binario de Busqueda (BST)** con una insercion balanceada desde la raiz `"103"` permite mantener el catalogo ordenado por ISBN y realizar busquedas eficientes en $O(\log n)$ sin recorrer toda la coleccion.
2. La **Lista Enlazada Simple** facilita la gestion dinamica del carrito de compras mediante punteros `next`, permitiendo agregar, visualizar, eliminar productos y validar el inventario en tiempo real antes de confirmar una transaccion.
