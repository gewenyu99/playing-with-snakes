class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        unvisitedRooms = set()
        unlockedRooms = set([0])
        for i in range(0, len(rooms)):
            unvisitedRooms.add(i)

        while unvisitedRooms:
            if not unlockedRooms:
                return False
            newKeys = set()
            for room in unlockedRooms:
                unvisitedRooms.discard(room)
                for key in rooms[room]:
                    newKeys.add(key)
            unlockedRooms |= newKeys
            unlockedRooms &= unvisitedRooms
        return True


print(Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))