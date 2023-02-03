import sys
input = sys.stdin.readline

test_cases = int(input())

inputs  = []

def inlt():
    return(list(map(int,input().split())))


def actual_cost(arr):
    res = []
    for i in range(len(arr)):
        res.append(i+1+arr[i])
    return res


for i in range(test_cases):
    line1 = inlt()

    a_length =  line1[0]
    coins = line1[1]
    arr = inlt()
    
    inputs.append({ 
        "arr":arr,
        "coins": coins 
    })

for val in inputs:

    cost_arr = actual_cost(val["arr"])
    coins = val["coins"]
    cost_arr.sort()
    ans = 0

    for cost in cost_arr:
        coins = coins - cost
        if coins < 0:
            break
        else:
            ans +=1
    
    print(ans)


