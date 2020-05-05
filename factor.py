from math import exp
from math import sqrt
from random import seed
from random import random
from random import randint

seed(1)

n = 7 * 11
a = randint(1, round(sqrt(n)))
b = randint(1, round(sqrt(n)))

def energy(m, n):
    e = 0
    i = 0
    while n != 0:
        if (m & 1) == (n & 1):
            e += i
        m = m >> 1
        n = n >> 1
        i += 1
    return e
print(n, energy(n, n))
print(a, b, energy(a*b, n))

t = 1000
for c in range(1000):
    aprime = a
    bprime = b
    mutation = randint(0, 2)
    if mutation == 0:
        aprime = aprime ^ (1 << randint(0, 16))
    elif mutation == 1:
        bprime = bprime ^ (1 << randint(0, 16))
    else:
        aprime = aprime ^ (1 << randint(0, 16))
        bprime = bprime ^ (1 << randint(0, 16))
    nprime = aprime * bprime
    if nprime == n:
        break
    elif nprime > n or nprime == 0 or aprime == 1 or bprime == 1:
        continue
    e = energy(a * b, n)
    eprime = energy(nprime, n)
    if eprime > e:
        a = aprime
        b = bprime
    elif exp((eprime - e)/t) > random():
        a = aprime
        b = bprime
    t = t * .9
print(energy(a*b, n))
print(a, b, n - (a*b))
