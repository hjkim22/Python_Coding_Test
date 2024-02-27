def solution(arr, k):
    result = []
    seen = set()
    
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
            if len(result) == k:
                break
    
    while len(result) < k:
        result.append(-1)
    
    return result

print(solution([0, 1, 1, 2, 2, 3], 3))
print(solution([0, 1, 1, 1, 1], 4))
