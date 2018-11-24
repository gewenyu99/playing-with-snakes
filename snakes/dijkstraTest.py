# After developing Golang for a bit, I caught on to how they unit test by literally creating a fileTest.go for file .go
from snakes.dijkstra import shortestPath
from snakes.networking import Solution

g1 = {
    "1": [{"next": "2", "dist": 12},
          {"next": "6", "dist": 6}],
    "2": [{"next": "3", "dist": 3},
          {"next": "4", "dist": 8},
          {"next": "5", "dist": 11}],
    "6": [{"next": "7", "dist": 3},
          {"next": "8", "dist": 4}],
    "8": [{"next": "9", "dist": 6}],
    "4": [{"next": "9", "dist": 6}],
    "3": [{"next": "9", "dist": 6}],
    "5": [{"next": "9", "dist": 6}],
    "7": None,
    "9": None
}

# print(shortestPath("1", "3", g1))
# print(shortestPath("1", "7", g1))
# print(shortestPath("1", "8", g1))
# print(shortestPath("1", "9", g1))
# print(shortestPath("1", "2", g1))
# print(shortestPath("1", "6", g1))
# print(shortestPath("1", "1", g1))
