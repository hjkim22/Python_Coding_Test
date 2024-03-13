def solution(d, budget):
    d.sort()
    count = 0
    for cost in d:
        budget -= cost
        if budget < 0:
            break
        count += 1
    return count

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))