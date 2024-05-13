def solution(citations):
    citations.sort()
    n = len(citations)
    
    if n == 0:
        return 0
    
    for i in range(n):
        if citations[i] >= n - i:
            return n - i
    
    return 0 

print(solution([3, 0, 6, 1, 5]))