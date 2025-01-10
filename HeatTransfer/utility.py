import numpy
from scipy import integrate

def e(i, x, h):
    if x<(i-1)*h or x>(i+1)*h:
        return 0
    elif x<i*h:
        return x/h - i + 1
    else:
        return -x/h + i - 1

def e_prim(i, x, h):
    if x<(i-1)*h or x>(i+1)*h:
        return 0
    elif x<i*h:
        return 1/h
    else:
        return -1/h

def k(x):
    if 0<=x<=1:
        return 1
    elif 1<x<=2:
        return 2*x
    else:
        return 0

def B(i, j, l, r, h):
    return integrate.quad(lambda x: e_prim(i, x, h) * e_prim(j, x, h) * k(x), l, r)[0]

def L(i, l, r, h):
    return integrate.quad(lambda x: 100 * x**2 * e(i, x, h), l, r)[0] - e(i, 0, h) * 20

def matrixA(n, h):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if abs(i-j) > 1:
                row.append(0)
                continue
            if abs(i-j) == 1:
                l = max(0, min(i,j)*h)
                r = min(2, max(i,j)*h)
            else:
                l = max(0, (i-1) * h)
                r = min(2, (i+1) * h)
            row.append(B(j, i, l, r, h))
        matrix.append(row)
    return matrix

def matrixB(n, h):
    matrix = []
    for i in range(n):
        l = max(0, (i-1) * h)
        r = min(2, (i+1) * h)
        matrix.append(L(i, l, r, h))
    return matrix

def solve(n):
    h = 2/n
    a = numpy.array(matrixA(n, h))
    b = numpy.array(matrixB(n, h))
    u = numpy.linalg.solve(a, b)
    x = [h*i for i in range(n+1)]
    y = numpy.append(u, -20)
    return x, y

