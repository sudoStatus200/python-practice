from collections import deque
list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [8, 9, 10, 11, 12, 13, 14]

list_a.append(2)
list_c = [2]
list_c.extend(list_a)
list_c[len(list_c):] = list_a
list_c.insert(2, 12)
print(list_c[:])

queue = deque(["Eric", "John", "Michael"])


list_c = [(x, y) for x in range(8) for y in range(0, 8) if x == y]
print(list_c)
for i, v in enumerate(list_a):
    print(i, v)
