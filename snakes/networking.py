# Solution to this: https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # Construct a graph for shortestPath
        g = {}
        for i in range (1, N + 1):
            g[str(i)] = None
        for time in times:
            u, v, w = time # I'm not kidding; u, v, w are variable names given from the damn question
            if not g[str(u)]:
                g[str(u)] = []
            g[str(u)].append({"next": str(v), "dist": w})

        longestOptimalPing = 0

        dist = shortestPath(str(K), str(i), g)
        for key, item in dist.items():
            if item == float('inf'):
                return -1
            if item > longestOptimalPing:
                longestOptimalPing = item


        return longestOptimalPing


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

    return dist


