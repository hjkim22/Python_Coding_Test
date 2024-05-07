import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def lcm_of_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        l = lcm(arr[0], arr[1])
        for i in range(2, len(arr)):
            l = lcm(l, arr[i])
        return l

def solution(arr):
    return lcm_of_array(arr)

print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))