test_cases = int(input())

main_string   = "codeforces"
directions = []


for i in range(test_cases):
    s_length = int(input())
    direction = input()
    directions.append(direction)


results = []
for steps in directions:
    r_pos = 0
    u_pos = 0 
    ans = 'NO'
    for step in steps:
        if step  == "U":
            u_pos += 1
        if step  == "D":
            u_pos -= 1
        if step  == "R":
            r_pos += 1
        if step  == "L":
            r_pos -= 1
        if r_pos ==  1 and u_pos == 1:
            ans = "YES"
            break
        
    results.append(ans)



for res in results:
    print(res)
    

        


