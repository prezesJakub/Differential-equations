import seaborn
import matplotlib.pyplot as plt

def show(x, y, n):
    seaborn.set(style='darkgrid')
    plt.figure()
    plt.title('Transport Ciepła MES')
    plt.xlabel(f'n = {n}')
    plt.plot(x, y, color='darkblue')
    plt.grid(True)
    plt.show()
