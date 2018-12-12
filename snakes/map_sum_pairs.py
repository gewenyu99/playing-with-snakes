## https://leetcode.com/problems/map-sum-pairs/
class MapSum(object):
    # Basically a B Tree

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numMap = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        pointer = self.numMap
        for i in range(0, len(key)):
            if key[i] not in pointer:
                pointer[key[i]] = {}
            pointer = pointer[key[i]]
        pointer['val'] = val
        print(self.numMap)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        pointer = self.numMap
        for i in range(0, len(prefix)):
            if prefix[i] not in pointer:
                return 0
            pointer = pointer[prefix[i]]

        return dfsSum(pointer)


def dfsSum(root):
    localSum = 0
    for key, node in root.items():
        if key != 'val':
            localSum += dfsSum(node)

    if 'val' in root:
        return localSum + root['val']
    return localSum

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)