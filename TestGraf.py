import Graf
import Graf_func
import Graf_Cruscal
import math

def deikstra():
    nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]

    init_graph = {}
    for node in nodes:
        init_graph[node] = {}

    init_graph["Reykjavik"]["Oslo"] = 5
    init_graph["Reykjavik"]["London"] = 4
    init_graph["Oslo"]["Berlin"] = 1
    init_graph["Oslo"]["Moscow"] = 3
    init_graph["Moscow"]["Belgrade"] = 5
    init_graph["Moscow"]["Athens"] = 4
    init_graph["Athens"]["Belgrade"] = 1
    init_graph["Rome"]["Berlin"] = 2
    init_graph["Rome"]["Athens"] = 2

    graph = Graf_func.Graph_func(nodes, init_graph)

    previous_nodes, shortest_path = Graf.Graph.dijkstra_algorithm(graph=graph, start_node="Reykjavik")

    Graf.Graph.print_result(previous_nodes, shortest_path, start_node="Reykjavik", target_node="Belgrade")


def prima():
    matr = [
             [0, -1, 15, 20, 15],
             [-1, 0, 60, 50, 80],
            [15, 60, 0, 50, 10],
            [20, 50, 50, 0, 30],
            [15, 80, 10, 30, 0]
        ]

    Graf.Graph.prima(matr)


def kruskal():          # алгоритм Крускала
    example_graf = Graf_Cruscal.Grap_cruscal(9)

    example_graf.add_edge(0, 1, 4)
    example_graf.add_edge(0, 2, 7)
    example_graf.add_edge(1, 2, 11)
    example_graf.add_edge(1, 3, 9)
    example_graf.add_edge(1, 5, 20)
    example_graf.add_edge(2, 5, 1)
    example_graf.add_edge(3, 6, 6)
    example_graf.add_edge(3, 4, 2)
    example_graf.add_edge(4, 6, 10)
    example_graf.add_edge(4, 8, 15)
    example_graf.add_edge(4, 7, 5)
    example_graf.add_edge(4, 5, 1)
    example_graf.add_edge(5, 7, 3)
    example_graf.add_edge(6, 8, 5)
    example_graf.add_edge(7, 8, 12)

    example_graf.kruskals_mst()


def floid():
    W = [[0, 2, math.inf, 3, 1, math.inf, math.inf, 10],
         [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
         [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
         [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
         [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
         [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
         [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
         [10, math.inf, 3, 8, math.inf, math.inf, 1, 0],
         ]

    Graf.Graph.floid(W)

def dfs_start():        #обход в глубину
    graph = {'0': set(['1', '2']),
             '1': set(['0', '3', '4']),
             '2': set(['0']),
             '3': set(['1']),
             '4': set(['2', '3'])}

    Graf.Graph.dfs(graph, '0')

def bfs_start():    # обход в ширину
    graph = {0: [1, 2],
             1: [2],
             2: [3],
             3: [1, 2]
             }

    Graf.Graph.bfs(graph, 0)

if __name__ == '__main__':
    deikstra(), print("\n")
    prima(), print("\n")
    kruskal(), print("\n")
    floid(), print("\n")
    dfs_start(), print("\n")
    bfs_start()