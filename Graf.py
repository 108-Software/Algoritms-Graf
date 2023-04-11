import sys
import random
from string import ascii_uppercase
import Graf_func
import collections

class Graph:

    @staticmethod
    def dijkstra_algorithm(graph, start_node):
        unvisited_nodes = list(graph.get_nodes())

        # Мы будем использовать этот словарь, чтобы сэкономить на посещении каждого узла и обновлять его по мере продвижения по графику
        shortest_path = {}

        # Мы будем использовать этот dict, чтобы сохранить кратчайший известный путь к найденному узлу
        previous_nodes = {}

        # Мы будем использовать max_value для инициализации значения "бесконечности" непосещенных узлов
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        # Однако мы инициализируем значение начального узла 0
        shortest_path[start_node] = 0

        # Алгоритм выполняется до тех пор, пока мы не посетим все узлы
        while unvisited_nodes:
            # Приведенный ниже блок кода находит узел с наименьшей оценкой
            current_min_node = None
            for node in unvisited_nodes:  # Iterate over the nodes
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            # Приведенный ниже блок кода извлекает соседей текущего узла и обновляет их расстояния
            neighbors = graph.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    # We also update the best path to the current node
                    previous_nodes[neighbor] = current_min_node

            # После посещения его соседей мы отмечаем узел как "посещенный"
            unvisited_nodes.remove(current_min_node)

        return previous_nodes, shortest_path

    @staticmethod
    def print_result(previous_nodes, shortest_path, start_node, target_node):
        path = []
        node = target_node

        while node != start_node:
            path.append(node)
            node = previous_nodes[node]

        # Добавить начальный узел вручную
        path.append(start_node)

        print("Найден следующий лучший маршрут с ценностью {}.".format(shortest_path[target_node]))
        print(" -> ".join(reversed(path)))


    @staticmethod
    def prima(W, city_labels=None):
        """
        Алгоритм Прима для нахождения сети дорог минимальной длины
        Дискретная алгебра, приложение 1
        """

        _ = float('inf')
        cities_count = len(W)

        # проверка на размерость таблицы связей
        for weights in W:
            assert len(weights) == cities_count

        # генерация имен городов
        if not city_labels:
            city_labels = [ascii_uppercase[x] for x in range(cities_count)]

        assert cities_count <= len(city_labels)

        # выбор начального города
        free_vertexes = list(range(0, len(city_labels)))

        starting_vertex = random.choice(free_vertexes)
        tied = [starting_vertex]
        free_vertexes.remove(starting_vertex)

        print('Started with %s' % city_labels[starting_vertex])

        road_length = 0

        # пока есть свободные вершины
        while free_vertexes:
            min_link = None  # соединение, образующее минимальный путь
            overall_min_path = _  # минимальный путь среди всех возможных

            # проход по всем уже связанным дорогой вершинам
            for current_vertex in tied:
                weights = W[current_vertex]  # связи текущей вершины с другими

                min_path = _
                free_vertex_min = current_vertex

                # проход по связанным городам
                for vertex in range(cities_count):
                    vertex_path = weights[vertex]
                    if vertex_path == 0:
                        continue

                    if vertex in free_vertexes and vertex_path < min_path:
                        free_vertex_min = vertex
                        min_path = vertex_path

                if free_vertex_min != current_vertex:
                    if overall_min_path > min_path:
                        min_link = (current_vertex, free_vertex_min)
                        overall_min_path = min_path
            try:
                path_length = W[min_link[0]][min_link[1]]
            except TypeError:
                print('Unable to find path')
                return

            print('Connecting %s to %s [%s]' % (city_labels[min_link[0]], city_labels[min_link[1]], path_length))

            road_length += path_length
            free_vertexes.remove(min_link[1])
            tied.append(min_link[1])

        print('Road length: %s' % road_length)
        # TODO: return graph

    @staticmethod
    def floid(W):
        N = len(W)
        F = [[[None for j in range(N)] for i in range(N)] for k in range(N + 1)]
        Parent = [[None for j in range(N)] for i in range(N)]
        for k in range(N + 1):
            for i in range(N):
                for j in range(N):
                    if k == 0:
                        F[0][i][j] = W[i][j]
                    else:
                        F[k][i][j] = min(F[k - 1][i][j], F[k - 1][i][k - 1] + F[k - 1][k - 1][j])
                        Parent[i][j] = Parent[k - 1][j]
        print(F[i][j], end=" ")

    @staticmethod
    def dfs(graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start)
        for next in graph[start] - visited:
            Graph.dfs(graph, next, visited)
        return visited


    @staticmethod
    def bfs(graph, root):
        visited, queue = set(), collections.deque([root])
        visited.add(root)
        while queue:
            vertex = queue.popleft()
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
