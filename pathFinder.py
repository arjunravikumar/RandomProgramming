"""
Problem: https://www.geeksforgeeks.org/shortest-distance-two-cells-matrix-grid/
Author: Arjun Ravikumar
"""
import copy
class Point:
	def __init__(self, row = 0, col = 0, dist = 0):
		self.row = row
		self.col = col
		self.dist = dist

def shortestPath(grid):
    queue = []
    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    start = None
    for i in range(len(grid)):
    	for j in range(len(grid[i])):
    		if (grid[i][j] == "s"):
    			start = Point(i,j,0)
    queue.append([start])
    while(len(queue)>0):
        path = queue.pop(0)
        loc = path[-1]
        for i in range(-1,2):
            for j in range(-1,2):
                if((i == 0 or j == 0) and (loc.row + i) >= 0 and (loc.col + j) >= 0 and \
                	(loc.row + i) < len(grid) and (loc.col + j) < len(grid[0]) \
                	and visited[loc.row + i][loc.col + j] == False):
                    visited[loc.row + i][loc.col + j] = True
                    if(grid[loc.row + i][loc.col + j] == "d"):
                        return path
                    if(grid[loc.row + i][loc.col + j] == "*"):
                        newPath = list(path)
                        newNode = Point(loc.row + i,loc.col + j,loc.dist+1)
                        newPath.append(newNode)
                        queue.append(newPath)
    return None

def modifyOriginalPath(grid,finalPath):
	node = finalPath
	for i in range(len(finalPath)):
		if(grid[finalPath[i].row][finalPath[i].col] == "*"):
			grid[finalPath[i].row][finalPath[i].col] = "."
	return grid

print("Original Maze:")
grid = [['*', '*', '0', 's', '*'],
        ['*', '0', '*', '0', '*'],
        ['*', '*', '0', '*', '*'],
        ['*', '*', '*', '*', '*'],
        ['d', '0', '*', '*', '0']]

for i in range(len(grid)):
	print(grid[i])

finalPath = shortestPath(grid)
if(finalPath == None):
	print("No Path")
else:
	endPath = modifyOriginalPath(grid,finalPath)
	print("\nCorrect Path:")
	for i in range(len(endPath)):
		print(endPath[i])
