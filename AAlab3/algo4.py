def algorithm4(n):
    c = [True for x in range(n)]
    c[0] = False
    c[1] = False
    i = 2

    while (i<n):
        j = 2
        while(j<i):
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1

    sieve = [i for i in range(n) if c[i]]

    return sieve

