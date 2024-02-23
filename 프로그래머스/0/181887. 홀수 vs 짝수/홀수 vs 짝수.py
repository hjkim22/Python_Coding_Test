def solution(num_list):
    odd_sum = sum(num_list[::2])
    even_sum = sum(num_list[1::2])
    
    return max(odd_sum, even_sum)

print(solution([4, 2, 6, 1, 7, 6]))
print(solution([-1, 2, 5, 6, 3]))