def pow(x):
    return x ** 2
def some_gen(begin, n, func):
    yield begin
    count = 1
    current = begin
    while count < n:
        current = func(current)
        yield current
        count += 1

print(list(some_gen(2, 4, pow)))
