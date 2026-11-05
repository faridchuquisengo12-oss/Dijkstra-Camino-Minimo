import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
import matplotlib.pyplot as plt
import networkx as nx

def crear_grafoAleatorio(n):
    lista_nodos = [chr(ord('A') + i) for i in range(n)]
    grafo = [[] for x in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < 0.4:
                peso = random.randint(1, 9)
                grafo[i].append((j, peso))
    return lista_nodos, grafo

def crear_grafoManual(n, text_widget):
    lista_nodos = [chr(ord('A') + i) for i in range(n)]
    grafo = [[] for x in range(n)]
    text_widget.insert(tk.END, "Ingrese conexiones entre nodos en formato: origen,destino,peso. (escriba 'fin' para terminar)\n")
    while True:
        entrada = simpledialog.askstring("Grafo Manual", "Conexión: ")
        if entrada is None or entrada.lower() == 'fin':
            break
        try:
            origen, destino, peso = entrada.split(',')
            origen = origen.strip().upper()
            destino = destino.strip().upper()
            peso = int(peso.strip())
            if origen in lista_nodos and destino in lista_nodos:
                i = lista_nodos.index(origen)
                j = lista_nodos.index(destino)
                grafo[i].append((j, peso))
            else:
                text_widget.insert(tk.END, "Nodos inválidos.\n")
        except:
            text_widget.insert(tk.END, "Formato incorrecto. Use: A,B,3\n")
        text_widget.update()
    return lista_nodos, grafo

def mostrar_matriz(lista_nodos, grafo):
    n = len(lista_nodos)
    matriz = [[0] * n for x in range(n)]
    for i, vecinos in enumerate(grafo):
        for j, peso in vecinos:
            matriz[i][j] = peso
    texto = "     " + "  ".join(f"{nodo:>3}" for nodo in lista_nodos) + "\n"
    for i in range(n):
        fila = "  ".join(f"{matriz[i][j]:>3}" for j in range(n))
        texto += f"{lista_nodos[i]:>3}  {fila}\n"
    return texto

def dibujar_grafo(lista_nodos, grafo, tipo):
    G = nx.DiGraph()
    for i, vecinos in enumerate(grafo):
        for j, peso in vecinos:
            G.add_edge(lista_nodos[i], lista_nodos[j], weight=peso)
    pos = nx.circular_layout(G) if tipo == "manual" else nx.spring_layout(G, seed=42)
    nx.draw_networkx_nodes(G, pos, node_size=800,
    node_color="skyblue" if tipo == "manual" else "lightgreen")
    nx.draw_networkx_labels(G, pos, font_weight="bold")
    for u, v in G.edges():
        if G.has_edge(v, u) and u < v:
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v)],
            connectionstyle='arc3,rad=0.25',
            arrows=True, arrowsize=20, edge_color='gray')
            nx.draw_networkx_edges(G, pos, edgelist=[(v, u)],
                connectionstyle='arc3,rad=-0.25',
                arrows=True, arrowsize=20, edge_color='gray')
        elif not G.has_edge(v, u):
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v)],
                connectionstyle='arc3,rad=0.0',
                arrows=True, arrowsize=20, edge_color='gray')
    seen_pairs = set()
    for u, v, data in G.edges(data=True):
        peso = data['weight']
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
        if G.has_edge(v, u):
            if (v, u) not in seen_pairs:
                plt.text(xm, ym + 0.1, str(peso), fontsize=9, color='black',
                        bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.2'))
            else:
                plt.text(xm, ym - 0.1, str(peso), fontsize=9, color='black',
                        bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.2'))
            seen_pairs.add((u, v))
            seen_pairs.add((v, u))
        else:
            plt.text(xm, ym, str(peso), fontsize=9, color='black',
                    bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.2'))
    plt.axis('off')
    plt.show()


def dijkstra_detallado(lista_nodos, grafo, origen, destino, text_widget):
    n = len(lista_nodos)
    dist = {v: float('inf') for v in lista_nodos}
    previo = {v: [] for v in lista_nodos}
    visitado = {v: False for v in lista_nodos}
    dist[origen] = 0
    for _ in range(n):
        no_visitados = {v: dist[v] for v in lista_nodos if not visitado[v]}
        if not no_visitados:
            break
        actual = min(no_visitados, key=no_visitados.get)
        visitado[actual] = True
        text_widget.insert(tk.END, f"\nVisitando nodo: {actual}")
        i = lista_nodos.index(actual)
        for j, peso in grafo[i]:
            vecino = lista_nodos[j]
            if dist[actual] + peso < dist[vecino]:
                dist[vecino] = dist[actual] + peso
                previo[vecino] = [actual]
            elif dist[actual] + peso == dist[vecino]:
                previo[vecino].append(actual)
        text_widget.insert(tk.END, f"\nDistancias actuales:\n")
        for v in lista_nodos:
            d = dist[v] if dist[v] != float('inf') else " "
            text_widget.insert(tk.END, f" {v}: {d} |")
        text_widget.insert(tk.END, "\n")
        text_widget.update()
    caminos = []
    def construir_caminos(nodo, camino):
        if nodo == origen:
            caminos.append([origen] + camino)
        else:
            for ant in previo[nodo]:
                construir_caminos(ant, [nodo] + camino)
    construir_caminos(destino, [])
    text_widget.insert(tk.END, f"\nDistancia mínima hasta {destino} = {dist[destino]}\n")
    text_widget.insert(tk.END, "Caminos mínimos posibles:\n")
    for c in caminos:
        text_widget.insert(tk.END, " => ".join(c) + "\n")
    text_widget.update()
    return dist[destino], caminos

class Proyecto:
    def __init__(self, root):
        self.root = root
        self.root.title("Problema del camino minimo - Dijkstra")
        self.lista_nodos = []
        self.grafo = []
        frame = ttk.Frame(root, padding=20)
        frame.grid(row=0, column=0, padx=10, pady=10)

        btn_config = {"font": ("Times New Roman", 11, "bold"), "width": 20, "height": 2}
        tk.Button(frame, text="Crear Grafo Aleatorio", command=self.crear_aleatorio, bg="#D0A798", **btn_config).grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        tk.Button(frame, text="Crear Grafo Manual", command=self.crear_manual, bg="#D0A798", **btn_config).grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        tk.Button(frame, text="Mostrar Matriz de Adyacencia", command=self.ver_matriz, bg="#D0A798", **btn_config).grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        tk.Button(frame, text="Dibujar Grafo Manual", command=self.dibujar_manual, bg="#D0A798", **btn_config).grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        tk.Button(frame, text="Dibujar Grafo Aleatorio", command=self.dibujar_aleatorio, bg="#D0A798", **btn_config).grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        tk.Button(frame, text="Ejecutar Dijkstra", command=self.ejecutar_dijkstra, bg="#D0A798", **btn_config).grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        tk.Button(frame, text="Salir del programa", command=self.root.quit, bg="#D0A798", **btn_config).grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        for i in range(4):
            frame.rowconfigure(i, weight=1)
        for j in range(2):
            frame.columnconfigure(j, weight=1)
        frame_text = tk.Frame(root)
        frame_text.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        self.text = tk.Text(frame_text, width=80, height=20)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(frame_text, command=self.text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.config(yscrollcommand=scrollbar.set)

    def crear_aleatorio(self):
        try:
            n = simpledialog.askinteger("Grafo Aleatorio", "Ingrese el número de nodos (8-16):")
            if n is None:
                return
            if n < 8 or n > 16:
                raise ValueError
            self.lista_nodos, self.grafo = crear_grafoAleatorio(n)
            messagebox.showinfo("Éxito", "Grafo aleatorio generado correctamente.")
        except:
            messagebox.showerror("Error", "Ingrese un número válido entre 8 y 16.")

    def crear_manual(self):
        try:
            n = simpledialog.askinteger("Grafo Manual", "Ingrese el número de nodos (3-10):")
            if n is None:
                return
            if n < 3 or n > 10:
                raise ValueError
            self.text.delete("1.0", tk.END) 
            self.lista_nodos, self.grafo = crear_grafoManual(n, self.text)
            messagebox.showinfo("Éxito", "Grafo manual creado correctamente.")
        except:
            messagebox.showerror("Error", "Ingrese un número válido entre 3 y 10.")

    def ver_matriz(self):
        if not self.grafo:
            messagebox.showwarning("Aviso", "Primero cree un grafo.")
            return
        texto = mostrar_matriz(self.lista_nodos, self.grafo)
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, texto)

    def dibujar_manual(self):
        if not self.grafo:
            messagebox.showwarning("Aviso", "Primero cree un grafo.")
            return
        dibujar_grafo(self.lista_nodos, self.grafo, "manual")

    def dibujar_aleatorio(self):
        if not self.grafo:
            messagebox.showwarning("Aviso", "Primero cree un grafo.")
            return
        dibujar_grafo(self.lista_nodos, self.grafo, "aleatorio")

    def ejecutar_dijkstra(self):
        if not self.grafo:
            messagebox.showwarning("Aviso", "Primero cree un grafo.")
            return
        origen = simpledialog.askstring("Dijkstra", "Ingrese nodo origen:").upper()
        destino = simpledialog.askstring("Dijkstra", "Ingrese nodo destino:").upper()
        if origen is None or destino is None:
            return
        if origen not in self.lista_nodos or destino not in self.lista_nodos:
            messagebox.showerror("Error", "Nodos inválidos.")
            return
        self.text.delete("1.0", tk.END)
        dist, caminos = dijkstra_detallado(self.lista_nodos, self.grafo, origen, destino, self.text)

if __name__ == "__main__":
    root = tk.Tk()
    proyecto = Proyecto(root)
    root.mainloop()