def solution(s):
    count_zero = 0 
    count_turn = 0  

    while s != "1":
        count_turn += 1 
        count_zero += s.count("0") 
        s = bin(s.count("1"))[2:] 
    return [count_turn, count_zero]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))