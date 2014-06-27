from math import sqrt
def is_prime_2(n):
    if n == 2:
        return True
    if (n < 2) or (n % 2 == 0):
        return False
    return all(n % i for i in xrange(3, int(sqrt(n)) + 1, 2))

n = int(raw_input())
count = 0
for i in range(0,n):
    for j in range(0,n):
        x = i + j
        if is_prime_2(x) == True:
            count = count + 1
print count
