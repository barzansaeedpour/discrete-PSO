import numpy as np

# The problem is defined in this file

def discrete_problem(x, P, M):

    # the problem is to find 10 numbers lower than M that their multiplication is equal to P and 
    # their summation is minimum
    
    # x is a list of continuous values between 0 and 1 generated by PSO
    
    # we need to convert it to discrete values:
    # first we transform these values to the desired interval  

    K = 1 + (M * x)         # transform 0-1 to 1-N
    K = np.floor(K)
   
    for t in K:
        t = min(t, M)

    
    violation = np.abs((np.prod(K)/P)-1)

    beta = 10
    z = np.sum(K) * (1+beta*violation)

    return z , K


def problem(x, P, M):

    z, K = discrete_problem(x, P, M)

    return z, K