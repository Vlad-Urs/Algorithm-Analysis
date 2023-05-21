import decimal
import math
from gmpy2 import mpz
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import random


def pi_bbp(n):
    decimal.getcontext().prec = n + 1  # Set the precision to n+1 decimal places
    pi = decimal.Decimal(0)
    for k in range(n):
        pi += (decimal.Decimal(1) / 16**k) * (
            decimal.Decimal(4) / (8*k+1) -
            decimal.Decimal(2) / (8*k+4) -
            decimal.Decimal(1) / (8*k+5) -
            decimal.Decimal(1) / (8*k+6)
        )
    return pi


def pi_gauss_legendre(n):
    """Compute the first n digits of pi using the Gauss-Legendre algorithm."""
    decimal.getcontext().prec = n + 1

    # Initialize the sequences A and B
    a = decimal.Decimal(1)
    b = 1 / decimal.Decimal(2).sqrt()
    t = decimal.Decimal(1) / decimal.Decimal(4)
    p = 1

    # Iterate until the desired number of digits is obtained
    for i in range(n):
        a_new = (a + b) / 2
        b_new = (a * b).sqrt()
        t_new = t - p * (a - a_new) ** 2
        p_new = 2 * p

        a = a_new
        b = b_new
        t = t_new
        p = p_new

    # Compute the final estimate of pi
    pi = (a + b) ** 2 / (4 * t)

    # Convert to a string and return the result
    return str(pi)[:n + 1]


def pi_chudnovsky(digits):
    """
    Compute int(pi * 10**digits)

    This is done using Chudnovsky's series with binary splitting
    """
    C = 640320
    C3_OVER_24 = C**3 // 24
    def bs(a, b):
        """
        Computes the terms for binary splitting the Chudnovsky infinite series

        a(a) = +/- (13591409 + 545140134*a)
        p(a) = (6*a-5)*(2*a-1)*(6*a-1)
        b(a) = 1
        q(a) = a*a*a*C3_OVER_24

        returns P(a,b), Q(a,b) and T(a,b)
        """
        if b - a == 1:
            # Directly compute P(a,a+1), Q(a,a+1) and T(a,a+1)
            if a == 0:
                Pab = Qab = mpz(1)
            else:
                Pab = mpz((6*a-5)*(2*a-1)*(6*a-1))
                Qab = mpz(a*a*a*C3_OVER_24)
            Tab = Pab * (13591409 + 545140134*a) # a(a) * p(a)
            if a & 1:
                Tab = -Tab
        else:
            # Recursively compute P(a,b), Q(a,b) and T(a,b)
            # m is the midpoint of a and b
            m = (a + b) // 2
            # Recursively calculate P(a,m), Q(a,m) and T(a,m)
            Pam, Qam, Tam = bs(a, m)
            # Recursively calculate P(m,b), Q(m,b) and T(m,b)
            Pmb, Qmb, Tmb = bs(m, b)
            # Now combine
            Pab = Pam * Pmb
            Qab = Qam * Qmb
            Tab = Qmb * Tam + Pam * Tmb
        return Pab, Qab, Tab
    # how many terms to compute
    DIGITS_PER_TERM = math.log10(C3_OVER_24/6/2/6)
    N = int(digits/DIGITS_PER_TERM + 1)
    # Calclate P(0,N) and Q(0,N)
    P, Q, T = bs(0, N)
    one_squared = mpz(10)**(2*digits)
    sqrtC = math.sqrt(10005*one_squared)
    return (Q*426880*sqrtC) // T


bbp_times = []
gl_times = []
chdn_times = []
digits = 125

for i in range(2,digits):

    start_time1 = timer()
    pi_bbp(i)
    bbp_times.append(timer() - start_time1)

    start_time2 = timer()
    pi_gauss_legendre(i)
    gl_times.append(timer() - start_time2)

    start_time3 = timer()
    pi_chudnovsky(i)
    chdn_times.append(timer() - start_time3)

digits_list = [x for x in range(2, digits)]

plt.plot(digits_list, bbp_times)
plt.plot(digits_list, gl_times)
plt.plot(digits_list, chdn_times)
plt.xlabel('Number of digits')
plt.ylabel('Seconds elapsed')
plt.legend(['Bailey-Borwein-Plouffe', 'Gauss-Legendre', 'Chudnovsky'])
plt.show()