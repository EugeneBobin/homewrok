def difference(*args):
    if not args:
        return 0
    else:
        min_value = min(args)
        max_value = max(args)
        return max_value - min_value

print(difference(1,7,9.4))