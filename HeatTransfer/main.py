from utility import solve
from plot import show

if __name__ == "__main__":
    n = int(input("Podaj liczbę elementów siatki: "))
    x, y = solve(n)
    show(x, y, n)