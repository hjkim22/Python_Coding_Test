def solution(sides):
    sides.sort()
    if max(sides) < sides[0] + sides[1]:
        return 1
    else:
        return 2

print(solution([1, 2, 3]))
print(solution([3, 6, 2]))
print(solution([199, 72, 222]))