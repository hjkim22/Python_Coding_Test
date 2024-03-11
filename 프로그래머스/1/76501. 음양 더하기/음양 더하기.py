def solution(absolutes, signs):
    result = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:
            result += absolute
        else:
            result -= absolute
    return result

print(solution([4,7,12], [True,False,True]))
print(solution([1,2,3], [False,False,True]))