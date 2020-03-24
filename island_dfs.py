import numpy as np

class findIsland:
    def __init__(self, arr):
        self.arr = arr 
        self.n_row, self.n_col = np.shape(self.arr)
        self.visited = np.zeros([self.n_row, self.n_col], dtype=int)
    
    def findSquareIsland(self):
        counter = 0
        for i in range(self.n_row):
            for j in range(self.n_col):
                if self.arr[i][j] == 1:
                    if i == 0 & j == 0:
                        counter += 1
                    elif i == 0 & j > 0 & self.arr[i][j-1] != 1:
                        counter += 1
                    elif j == 0 & i > 0 & self.arr[i-1][j] != 1:
                        counter += 1
                    elif self.arr[i-1][j] != 1 & self.arr[i][j-1] != 1:
                        counter += 1
        return counter
   
    def exploreGraph(self, i, j):
        explore_coor = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
        for (a,b) in explore_coor:
            new_i = i+a
            new_j = j+b
            if (0<=new_i<self.n_row) & (0<=new_j<self.n_col):
                if self.arr[new_i][new_j] == 0:
                    continue
                elif self.visited[new_i][new_j] != 1:
                    self.visited[new_i][new_j] = 1
                    self.exploreGraph(new_i, new_j)      
    
    def findIsland(self):
        num_islands = 0
        for i in range(self.n_row):
            for j in range(self.n_col):
                if (self.arr[i][j] == 1) & (self.visited[i][j] != 1):
                     self.visited[i][j] = 1
                     self.exploreGraph(i, j)
                     num_islands += 1
        print(self.visited)
        return num_islands


if __name__ == '__main__':

    test_1 = np.ones([4,4], dtype=int)
    print(test_1)
    f1 = findIsland(test_1) 
    f1.findIsland()

    test_2 = np.random.randint(0, 2, size=[5,5])
    print(test_2)
    f2 = findIsland(test_2) 
    f2.findIsland()
    
    test_3 = [[0,1,1,0], [0,1,1,0], [0,0,0,1], [1,1,0,0]]
    print(test_3)
    f3 = findIsland(test_3) 
    print('#Square Islands {}'.format(f3.findSquareIsland()))