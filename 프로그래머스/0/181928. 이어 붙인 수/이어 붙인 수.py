def solution(num_list):
    odd_str = ''.join(str(num) for num in num_list if num % 2 != 0)
    even_str = ''.join(str(num) for num in num_list if num % 2 == 0)
    return int(odd_str) + int(even_str)

print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))