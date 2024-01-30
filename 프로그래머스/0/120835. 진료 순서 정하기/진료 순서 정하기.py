def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    
    result = [sorted_emergency.index(x) + 1 for x in emergency]
    
    return result

emergency1 = [3, 76, 24]
emergency2 = [1, 2, 3, 4, 5, 6, 7]
emergency3 = [30, 10, 23, 6, 100]

print(solution(emergency1))
print(solution(emergency2))
print(solution(emergency3))