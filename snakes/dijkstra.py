# I wrote this to play around with graphs
# This is not the optimal fibinacci heap implementation
# In face I don't think this is optimal in any sense
import copy

# A dijkstra's shortest weighted directed path I wrote
def shortestPath(start, end, graph, returnPath = False):
    '''

    :param start: str |as key|
    :param end: str |as key|
    :param graph_const: dict[list[{"next": str, "dist": int} ...]]
    :param returnPath: bool
    :return:
    '''

    def findMin(dict, Q):
        retkey = None
        for key, item in dict.items():
            if key in Q:
                if not retkey:
                    retkey = key
                if item < dict[retkey]:
                    retkey = key
        return retkey

    dist = {}
    Q = []

    for key, node in graph.items():
        dist[key] = float('inf')
        Q.append(key)

    dist[start] = 0

    while Q:
        imminent = findMin(dist, Q)
        Q.remove(imminent)
        if graph[imminent]:
            for node in graph[imminent]:
                if dist[imminent] + node['dist'] < dist[node['next']]:
                    dist[node['next']] = dist[imminent] + node['dist']

    return dist[end]