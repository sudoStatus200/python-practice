test_cases = int(input())

main_string   = "codeforces"
results = []

for i in range(test_cases):
    letter = input()
    if letter in main_string:
        results.append("YES")
    else:
        results.append("NO")


for res in results:
    print(res)