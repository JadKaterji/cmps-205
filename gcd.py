# Assignment 6 part 1


def gcd(p,q):
    x = q
    if (q == 0):
        return p
    else:
        return gcd(q,p%q)

print(gcd(102,68))