def prime_generator(limit):
    primes = []
    num = 2
    while True:
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            if num <= limit:
                yield num
            else:
                return
        num += 1

print(list(prime_generator(int(input("enter number :")))))
