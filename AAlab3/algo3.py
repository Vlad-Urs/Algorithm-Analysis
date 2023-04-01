def algorithm3(n):
    c = [True for x in range(n)]
    c[0] = False
    c[1] = False
    i = 2

    while (i<n):
        if c[i]:
            j = i + 1
            while(j<n):
                if j % i == 0:
                    c[j] = False
                j += 1
        i += 1

    sieve = [i for i in range(n) if c[i]]

    return sieve



