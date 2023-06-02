def find_unique_value(nums):
    counts = {}

    for i in nums:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    unique_values = [i for i, count in counts.items() if count == 1]
    if len(unique_values) > 0:
        return unique_values
    else:
        return None

print(find_unique_value(list(map(int, input("Enter numbers :").split(" ")))))
