def solution(dot):
    x ,y = dot
    if x > 0:
        if y > 0:
            return 1
        else:
            return 4
    else:
        if y > 0:
            return 2
        else:
            return 3
print(solution([2, 4]))
print(solution([-7, 9]))