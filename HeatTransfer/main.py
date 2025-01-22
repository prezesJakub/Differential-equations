from utility import solve
from plot import show

if __name__ == "__main__":
    n = int(input("Podaj liczbę elementów siatki: "))
    if n <= 0:
        raise ValueError("Liczba elementów siatki musi być większa od zera")
    x, y = solve(n)
    show(x, y, n)