def solution(nums):
    num_set = set(nums)
    max_pick = len(nums) // 2
    
    return min(len(num_set), max_pick)

print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))