# Problema del camino mínimo: Algoritmo de Dijkstra

Proyecto académico desarrollado para el curso de **Matemática Computacional** de la Universidad Peruana de Ciencias Aplicadas (UPC), sección 5829.

El proyecto fue realizado de manera grupal. Por motivos de privacidad, esta versión pública del informe muestra únicamente mi nombre.



## Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación en Python con interfaz gráfica para resolver el **problema del camino mínimo en grafos dirigidos y ponderados**, mediante la implementación del **algoritmo de Dijkstra**.

La aplicación permite construir grafos de manera aleatoria o manual, visualizar su representación mediante un diagrama y consultar su matriz de adyacencia. Asimismo, permite seleccionar un nodo de origen y uno de destino para calcular la ruta de menor costo, mostrando el procedimiento seguido por el algoritmo.

## Funcionalidades

- **Generación de grafos aleatorios:** crea grafos de 8 a 16 nodos, etiquetados desde `A`, con una probabilidad del 40 % de conexión entre cada par de nodos y pesos aleatorios entre 1 y 9.
- **Creación manual de grafos:** permite definir entre 3 y 10 nodos e ingresar las conexiones mediante el formato `origen,destino,peso` (por ejemplo, `A,B,3`). La entrada finaliza al escribir `fin`.
- **Matriz de adyacencia:** representa las conexiones del grafo mediante una matriz que contiene los pesos correspondientes a cada arista.
- **Visualización del grafo:** muestra gráficamente los nodos, las aristas dirigidas y sus respectivos pesos.
- **Ejecución detallada de Dijkstra:** presenta las iteraciones del algoritmo, incluyendo los nodos visitados y las actualizaciones de las distancias provisionales.
- **Reconstrucción de caminos mínimos:** identifica la distancia mínima entre el origen y el destino y muestra todos los caminos posibles que alcanzan dicho costo.
- **Validaciones:** verifica los rangos permitidos, el formato de las conexiones y la existencia de los nodos ingresados, mostrando mensajes de aviso cuando corresponde.

## Ejemplo de resultado

En una ejecución con un grafo aleatorio de 8 nodos, al buscar el camino mínimo desde el nodo `G` hasta el nodo `E`, se obtuvo el siguiente resultado:

```text
Distancia mínima hasta E = 8

Caminos mínimos posibles:
G => B => E
```

El resultado representa una ruta cuyo costo total es de 8 unidades, correspondiente a la suma de los pesos de las aristas recorridas.

## Funcionamiento del algoritmo de Dijkstra

El algoritmo calcula las distancias mínimas desde un nodo de origen hacia los demás nodos del grafo mediante un proceso iterativo:

1. **Inicialización:** se asigna una distancia de `0` al nodo de origen y un valor infinito a los demás nodos.
2. **Selección del nodo:** se elige el nodo no visitado que presenta la menor distancia provisional.
3. **Actualización de distancias:** se evalúan sus nodos vecinos y se actualizan las distancias cuando se encuentra una ruta de menor costo. También se registran los predecesores para reconstruir los caminos mínimos.
4. **Repetición del proceso:** se continúa hasta completar las iteraciones del algoritmo.
5. **Reconstrucción de rutas:** se utilizan los predecesores registrados para obtener los caminos mínimos entre el origen y el destino.

**Restricción del algoritmo:** Dijkstra requiere que los pesos de las aristas sean no negativos. En esta implementación, los pesos utilizados son positivos.

## Contenido del repositorio

| Archivo | Descripción |
|---|---|
| `CaminoMinimo_Dijkstra.py` | Aplicación desarrollada en Python con interfaz gráfica mediante Tkinter. |
| `nombre_del_informe.pdf` | Informe académico que contiene el fundamento teórico, el diagrama de flujo y los resultados de la implementación. |
| `nombre_de_la_imagen.png` | Captura de pantalla de la aplicación en funcionamiento. |

## Tecnologías utilizadas

- **Python 3:** lenguaje de programación utilizado para implementar la lógica del algoritmo.
- **Tkinter:** biblioteca empleada para desarrollar la interfaz gráfica y las ventanas de diálogo.
- **NetworkX:** biblioteca utilizada para la creación y manipulación de grafos.
- **Matplotlib:** herramienta utilizada para representar gráficamente los grafos y sus conexiones.

## Requisitos

- Python 3 instalado.
- Tkinter, generalmente incluido en la instalación estándar de Python.
- Las bibliotecas NetworkX y Matplotlib.

Para instalar las dependencias necesarias, ejecutar:

```bash
pip install networkx matplotlib
```

## Cómo ejecutar el proyecto

1. Clonar o descargar este repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Instalar las dependencias indicadas anteriormente.
4. Ejecutar el siguiente comando:

```bash
python CaminoMinimo_Dijkstra.py
```

Al iniciar la aplicación, se mostrará el menú principal, desde el cual será posible crear un grafo, consultar su matriz de adyacencia, visualizar su estructura y ejecutar el algoritmo de Dijkstra indicando los nodos de origen y destino.

## Propósito académico

El objetivo del proyecto es aplicar los conceptos de **teoría de grafos, grafos dirigidos, ponderaciones y algoritmos de búsqueda de caminos mínimos** mediante una implementación práctica de Dijkstra.

Asimismo, permite comprender cómo se representan las conexiones entre nodos, cómo se determinan las rutas de menor costo y cómo se puede visualizar el procedimiento de resolución de un problema computacional.
