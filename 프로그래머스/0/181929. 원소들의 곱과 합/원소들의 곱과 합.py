def solution(num_list):
    answer = 1
    total = sum(num_list)
    for num in num_list:
        answer *= num
    if answer < total ** 2:
        return 1
    else:
        return 0
    
print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))