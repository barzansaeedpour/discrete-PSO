import numpy as np

# The problem is defined in this file

def discrete_problem(x, P, M):

    # the problem is to find 10 numbers lower than M that their multiplication is equal to P and 
    # their summation is minimum
    


    temp = 1+M*x
    temp = np.floor(temp)
    temp = np.append(temp, M)
    K = np.min(temp)

    violation = np.abs((np.prod(K)/P)-1)

    beta = 10
    z = np.sum(K) * (1+beta*violation)

    return z


def problem(x, P, M):

    z = discrete_problem(x, P, M)

    return z