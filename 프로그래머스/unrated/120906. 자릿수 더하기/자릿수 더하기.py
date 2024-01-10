def solution(n):
    num = list(str(n))
    
    num_sum = sum(map(int, num))
    
    return num_sum

print(solution(1234))
print(solution(930211))