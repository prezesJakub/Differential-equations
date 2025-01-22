import numpy
from scipy import integrate


def k(x):
    if 0 <= x <= 1:
        return 1
    elif 1 < x <= 2:
        return 2 * x
    else:
        return 0


def element_integrals(l, r, h):
    B = numpy.zeros((2, 2))
    L = numpy.zeros(2)

    quadrature_points = numpy.array([-1, 1]) / numpy.sqrt(3)

    midpoint = (l + r) / 2

    e_prim = numpy.array([-1, 1]) / h

    for xi in quadrature_points:
        x = midpoint + h * xi / 2
        e = numpy.array([1 - xi, 1 + xi]) / 2

        for i in range(2):
            L[i] += 100 * x ** 2 * e[i] * h / 2
            for j in range(2):
                B[i, j] += k(x) * e_prim[i] * e_prim[j] * h / 2
    return B, L


def assemble_global_matrices(N):
    nodes = numpy.linspace(0, 2, N + 1)

    B_global = numpy.zeros((N + 1, N + 1))
    L_global = numpy.zeros(N + 1)

    for element in range(N):
        l, r = nodes[element], nodes[element + 1]
        h = r - l

        B, L = element_integrals(l, r, h)

        for i in range(2):
            L_global[element + i] += L[i]
            for j in range(2):
                B_global[element + i, element + j] += B[i, j]
    return B_global, L_global, nodes


def apply_boundary_conditions(B, L):
    B[-1, :] = 0
    B[-1, -1] = 1
    L[-1] = -20

    B[0, 0] += 1
    L[0] += -20

    return B, L


def solve(n):
    B, L, nodes = assemble_global_matrices(n)

    B, L = apply_boundary_conditions(B, L)

    u = numpy.linalg.solve(B, L)

    return nodes, u
