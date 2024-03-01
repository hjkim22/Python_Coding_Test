def solution(arr):
    max_length = max(len(arr), len(arr[0]))
    
    for i in range(len(arr)):
        while len(arr[i]) < max_length:
            arr[i].append(0)
    
    while len(arr) < max_length:
        arr.append([0] * max_length)
    
    return arr

print(solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]))
print(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))
print(solution([[1, 2], [3, 4]]))