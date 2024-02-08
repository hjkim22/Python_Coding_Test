def solution(numlist, n):
    distances = []
    
    for num in numlist:
        distances.append((abs(num - n), -num))
    
    distances.sort()
    
    answer = [-pair[1] for pair in distances]
    
    return answer

print(solution([1, 2, 3, 4, 5, 6], 4))
print(solution([10000, 20, 36, 47, 40, 6, 10, 7000], 30))