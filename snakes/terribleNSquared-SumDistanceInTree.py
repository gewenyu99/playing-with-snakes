# Solution: https://leetcode.com/problems/sum-of-distances-in-tree/description/
# Can you tell the later into the night it gets, the worse my file and var naming?

import copy

class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        rList = []
        graph = {}
        OG_Q = set()
        for i in range(0, N):
            OG_Q.add(str(i))
            graph[str(i)] = []

        for edge in edges:
            graph[str(edge[0])].append(str(edge[1]))
            graph[str(edge[1])].append(str(edge[0]))

        def crawl(start):
            Q = copy.deepcopy(OG_Q)
            curNode = str(start)
            dist = {}
            dist[curNode] = 0

            while Q:
                Q.discard(curNode)
                for node in graph[curNode]:
                    if node not in dist:
                        dist[node] = dist[curNode] + 1
                for node, _ in dist.items():
                    if node in Q:
                        curNode = node
                        break;
            return dist

        def sumDistance(dict):
            sum = 0
            for key, num in dict.items():
                sum += num
            return sum

        for i in range(0, N):
            dist = crawl(i)
            rList.append(sumDistance(dist))

        return rList


