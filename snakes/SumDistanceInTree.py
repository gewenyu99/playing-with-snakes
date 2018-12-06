# Solution: https://leetcode.com/problems/sum-of-distances-in-tree/description/
# I admit I had to look at the solution a bit to figure this one  out
# This is honestly, really hard :3

class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        # My take on the given solution's algo :3
        # It took me a good while just to understand the solution
        # That's how you know it was a great question :D
        if N == 1:
            return [0]

        graph = {}  # We turn this into a graph so it is easy to traverse

        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = set()
            if edge[1] not in graph:
                graph[edge[1]] = set()
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        # We're gonna map out the child_dist and node_counts
        child_dist = {}
        node_count = {}

        def post_order(root, parent):
            node_count[root] = 1
            child_dist[root] = 0
            for node in graph[root]:
                if node != parent:
                    count, dist = post_order(node, root)
                    node_count[root] += count
                    child_dist[root] += count
                    child_dist[root] += dist
            return [node_count[root], child_dist[root]]

        def sum_dists(root, parent):
            for node in graph[root]:
                if node != parent:
                    sum_list[node] = sum_list[root] - node_count[node] * 2 + N
                    sum_dists(node, root)

        post_order(root=0, parent=None)
        sum_list = [0] * N
        sum_list[0] = child_dist[0]
        sum_dists(root=0, parent=None)

        return sum_list







