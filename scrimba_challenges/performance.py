import timeit

print("Performance and Timeit module")
# Experiment with sieve of Eratosthenes
def test1():
    [
        x
        for x in range(1, 151)
        if not any([x % y == 0 for y in range(2, x)]) and not x == 1
    ]
    return(1)

def test2():
  [x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])]

# Initialize a list
def test3():
    primes = []
    for possiblePrime in range(2, 151):
        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime**0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)  
    return(1)

print(timeit.timeit("test1()", globals=globals(), number=10))
print(timeit.timeit("test2()", globals=globals(), number=10))
print(timeit.timeit("test3()", globals=globals(), number=10))


# this shows that the for loop without comprehension is faster --> never judge the speed of your code by how messy it is

