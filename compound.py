def lchain_decorator(func):
    def wrapper(*iterables):
        result = []
        for item in iterables:
            for i in item:
                result.append(i)
        return result
    return wrapper

@lchain_decorator
def lchain(*iterables):
    pass

result = lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10))
print(result)
