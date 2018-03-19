import math

def is_prime(n):
    import math
    for i in xrange(2,n):
        if n % i == 0:
            return False
        elif i > math.sqrt(n):
            break
        else:
            continue
    return True

def get_primes_brute():
    i=1
    primes = []
    while True:
        i+=1
        if is_prime(i):
            primes.append(i)
        elif len(primes) >= 10001:
            break
        else:
            continue
    return primes[-1]    

def get_primes_fast(n,limit=125001):
    i=0
    primes = [True]*limit
    primes[0], primes[1]= False, False
    for ind, val in enumerate(primes):
        if val is True:
            primes[ind*2::ind] = [False] * (len(primes[ind*2::ind]))
            i+=1
        if i == n: return ind
        elif ind == limit-1:
            return "Only reached %dth prime with limit = %d. Use a larger container." % (i, limit)
    return False

print get_primes_fast(10001)
