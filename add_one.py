def add_one(digits):
    carry = 1
    result = []

    for i in range(len(digits)-1,-1,-1):
        sum = digits[i] + carry
        result.append(sum % 10)
        carry = sum // 10

    if carry > 0:
        result.append(carry)

    result.reverse()

    return result
print(add_one(list(map(int, input("enter numbers off list :").split(" ")))))

