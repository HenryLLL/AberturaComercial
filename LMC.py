"""
Calculating new wages using the labor market clearing condition
"""

import numpy as np


def lmc(Xp, Dinp, J, N, B, VAL):
    PQ_vec = Xp.T.reshape(J * N, 1, order='F').copy()

    # Check if DDinpt gives a different value
    DDinpt = np.zeros((J * N, N))
    for n in range(N):
        DDinpt[:, n] = Dinp[:, n] * PQ_vec.reshape(1, J * N)

    DDDinpt = np.zeros((J, N))
    for n in range(J):
        DDDinpt[n, :] = sum(DDinpt[n * N: (n + 1) * N, :])

    aux4 = B * DDDinpt
    aux5 = sum(aux4)
    aux5 = aux5.T.reshape(N, 1)
    wf0 = (1 / VAL) * aux5
    
    return wf0
