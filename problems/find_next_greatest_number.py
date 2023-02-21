"""
number: 1342
result: 1423
"""


def find_next(number):
    n = len(number)

    for i in range(n-1, 0, -1):
        if number[i] > number[i-1]:
            break

    if i == 0 and number[i] <= number[i-1]:
        return "Not possible"

    x = number[i-1]
    smallest_idx = i

    for j in range(i+1, n):
        if number[j] > x and number[j] < number[smallest_idx]:
            smallest_idx = j

    number[smallest_idx], number[i-1] = number[i-1], number[smallest_idx]

    result = 0

    for j in range(i):
        result = result * 10 + number[j]

    number = sorted(number[i:])

    for j in range(n-i):
        result = result * 10 + number[j]

    print("Next number with set of digits is", result)
    return result


digits = "1342"


number = list(map(int, digits))

print(find_next(number))
