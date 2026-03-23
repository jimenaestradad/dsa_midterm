# dsa_midterm

Estructura del Proyecto

dsa_midterm/
├── ll.py # Implementación de la lista doblemente linkeada
├── songs.py # Dataset de 100 canciones
├── profiling.py # Carga de datos + memoryprofiling and time profiling
└── player.py # Interfaz de usuario y funcionalidades (play, next, shuffle, etc.)


---

## Profiling del método de carga

Descripción

El método de carga consiste en recorrer una lista de 100 canciones y agregar cada una a la estructura `LinkedList` mediante `insert_at_end`.

```python
for title, artist, album in song_tuples:
    node = Node(title, artist, album)
    playlist.insert_at_end(node)


## Profiling de tiempo y de memoria 
![Captura profiling](<Captura de pantalla 2026-03-23 a la(s) 10.49.48 a. m..png>)

## Mecanismo de shuffle y complejidad teoórica

La funcionalidad de shuffle se implementa directamente sobre la estructura de datos, es decir, sobre la lista doblemente linkeada, modificando los enlaces entre nodos (next y prev) para cambiar el orden de reproducción. A diferencia de un enfoque tradicional que usa listas externas, aquí se reordena la misma estructura, lo que permite que la navegación con next y previous siga funcionando correctamente sin necesidad de lógica adicional.

El proceso de shuffle consiste en recorrer todos los nodos de la playlist y guardarlos en una lista auxiliar, además de almacenar una copia del orden original para poder restaurarlo después. Luego se mezcla el orden de los nodos utilizando random.shuffle y se reconstruyen los enlaces (next y prev) de cada nodo según este nuevo orden. Finalmente, se actualiza el nodo inicial (start) de la playlist. Por ejemplo, si el orden original es A → B → C → D, después del shuffle podría quedar como C → A → D → B.

En cuanto a la complejidad, el algoritmo tiene un costo temporal de O(n), ya que se recorren los nodos, se mezclan y se re-enlazan, todo en tiempo lineal. A nivel espacial, también es O(n) porque se utiliza una lista auxiliar para almacenar los nodos. Entre sus principales características, destaca que el shuffle modifica directamente la lista enlazada, mantiene la navegación funcional mediante next y prev, y permite activarse o desactivarse restaurando el orden original.

## Ejecución 
Para ejecutar el proyecto primero se debe clonar el repositorio. Esto se hace desde la terminal utilizando git clone con la URL del repositorio, en este caso https://github.com/jimenaestradad/dsa_midterm.git, y luego se entra a la carpeta del proyecto con cd dsa_midterm.

Una vez instalado todo, se puede ejecutar el reproductor de la playlist con python3 player.py. Al correr este archivo se abre un menú interactivo en la terminal que permite reproducir canciones (Play), avanzar (Next), retroceder (Previous), activar o desactivar el shuffle, ver un preview de la lista (List preview) o salir del programa (Quit).

Después se deben instalar las dependencias necesarias. El proyecto utiliza memory_profiler para analizar el uso de memoria, por lo que se instala con pip install memory_profiler. Si el sistema no reconoce pip, entonces se puede usar pip3 install memory_profiler.

También se puede ejecutar el profiling del programa. Para medir el tiempo de carga se usa python3 profiling.py, y para medir el uso de memoria se ejecuta python3 -m memory_profiler profiling.py.