# I wrote this to play around with graphs
# This is not the optimal fibinacci heap implementation
# In face I don't think this is optimal in any sense
# A dijkstra's shortest weighted directed path I wrote
# If we do our implementation with a min heap, we could get faster run time

def shortestPath(start, end, graph, returnPath=False):
    '''

    :param start: str |as key|
    :param end: str |as key|
    :param graph_const: dict[list[{"next": str, "dist": int} ...]]
    :param returnPath: bool
    :return:
    '''

    # finds the minimum in the intersection of dict and Q
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
    Q = []  # Should really be a min heap
    path = []

    for key, node in graph.items():
        dist[key] = float('inf')
        Q.append(key)

    dist[start] = 0

    while Q:
        imminent = findMin(dist, Q)  # imminent is a key!
        Q.remove(imminent)
        path.append(imminent)

        if graph[imminent]:  # if the imminent node has descendents
            for node in graph[imminent]:
                new_path_len = dist[imminent] + node['dist']
                if new_path_len < dist[node['next']]:  # if the new path to said node is shorter
                    dist[node['next']] = new_path_len
    path.append(end)

    return dist[end]


# btree
def postorder(root, callback):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    callback(root.val)


def preorder(root, callback):
    if not root:
        return
    callback(root.val)
    postorder(root.left)
    postorder(root.right)


def inorder(root, callback):
    if not root:
        return
    postorder(root.left)
    callback(root.val)
    postorder(root.right)