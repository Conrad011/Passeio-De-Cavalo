import time

class KnightTour:
    def __init__(self, size):
        self.N = size
        self.board = [[-1 for _ in range(self.N)] for _ in range(self.N)]
        self.h = [2, 1, -1, -2, -2, -1, 1, 2]
        self.v = [1, 2, 2, 1, -1, -2, -2, -1]

    def isValid(self, x, y):
        return 0 <= x < self.N and 0 <= y < self.N and self.board[x][y] == -1

    def printBoard(self):
        for row in self.board:
            print(' '.join(f"{cell:2}" for cell in row))
        print()

    def solve(self):
        self.board[0][0] = 0
        if self.tryMove(1, 0, 0):
            print(f"Solução encontrada para tabuleiro {self.N}x{self.N}:")
            self.printBoard()
        else:
            print(f"Não há solução para tabuleiro {self.N}x{self.N}.")

    def tryMove(self, step, x, y):
        if step == self.N * self.N:
            return True
        for i in range(8):
            nx, ny = x + self.h[i], y + self.v[i]
            if self.isValid(nx, ny):
                self.board[nx][ny] = step
                if self.tryMove(step + 1, nx, ny):
                    return True
                self.board[nx][ny] = -1
        return False

# Teste com instâncias crescentes
for size in range(5, 9):  # De 5x5 até 8x8
    print("="*40)
    print(f"Testando tabuleiro {size}x{size}")
    start = time.time()
    tour = KnightTour(size)
    tour.solve()
    end = time.time()
    print(f"Tempo: {end - start:.2f} segundos")
