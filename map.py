import random


class Map:
    def __init__(self, m, n, density=0.4):
        self.m = m
        self.n = n
        self.grid = [[0 for _ in range(n)] for _ in range(m)]
        self.init_rand_islands(density=density)

    def init_rand_islands(self, density):
        self.grid = [[1 if random.random() < density else 0 for _ in range(self.n)] for _ in range(self.m)]

    def display(self):
        print(f"Input:\n{self.m} {self.n}")
        for row in self.grid:
            print(" ".join(map(str, row)))

    def count_islands(self):
        visited = [[False for _ in range(self.n)] for _ in range(self.m)]

        def dfs(x, y):
            if x < 0 or y < 0 or x >= self.m or y >= self.n or self.grid[x][y] == 0 or visited[x][y]:
                return
            visited[x][y] = True
            # explore neighbors
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        island_count = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1 and not visited[i][j]:
                    island_count += 1
                    dfs(i, j)

        return island_count


if __name__ == "__main__":
    m = random.randint(1, 10)
    n = random.randint(1, 10)
    map_instance = Map(m, n)
    map_instance.display()
    print("Output:", map_instance.count_islands())