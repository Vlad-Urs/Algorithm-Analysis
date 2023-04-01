def algorithm1(n):
    c = [True for x in range(n)]
    c[0] = False
    c[1] = False
    i = 2

    while (i<n):
        if c[i]:
            j = 2*i
            while(j<n):
                c[j] = False
                j += i
        i += 1

    sieve = [i for i in range(n) if c[i]]

    return sieve

