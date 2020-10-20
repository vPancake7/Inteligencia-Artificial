# Laboratorio N1
# Tema: Algoritmo de Dijkstra
# Alumno: Maykol Chang Song
# Cedula: 8-958-855
# Eleji el 1er Problema

graph = {
    'a':{'b':5, 'c':9},
    'b':{'e':10, 'f':7},
    'c':{'e':5, 'd':3},
    'f':{'h':8},
    'e':{'d':1,'g':4, 'h':2},
    'd':{'e':1,'g':4},
    'h':{'i':6},
    'g':{'i':12},
    'i':{'h':6,'g':12}
}

def dijkstra(graph,start,goal):
    shortest_distance = {} # Guarda el costo que requiere para llegar al nodo. Se actualiza a medida que se mueve en la grafica
    track_predecessor = {} # Keep track of the path that has led us to this code
    unseenNodes = graph    # Iterate through the entire graph
    infinity = 999999      # Un numero infinito puede ser considerado un numero muy largo
    track_path = []        # Trace our journey back to the source code / Ruta optima

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:

        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        path_options = graph[min_distance_node].items()

        for child_node, weight in path_options:

            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)

    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]

        except KeyError:
            print("El camino no se puede alcanzar")
            break

    track_path.insert(0,start)



    if shortest_distance[goal] != infinity:
        print("La distancia mas corta es de " + str(shortest_distance[goal]))
        print("El camino optimo es " + str(track_path))

dijkstra(graph, 'a', 'i')
