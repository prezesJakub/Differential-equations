from utility import solve
from plot import show

if __name__ == "__main__":
    n = 1000
    x, y = solve(n)
    show(x, y, n)