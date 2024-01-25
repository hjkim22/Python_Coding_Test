def solution(s):
    numbers = list(map(str, s.split()))
    result = 0
    stack = []

    for element in numbers:
        if element == "Z":
            popped = stack.pop()
            result -= popped
        else:
            current_number = int(element)
            result += current_number
            stack.append(current_number)

    return result

result1 = solution("1 2 Z 3")
print(result1)

result2 = solution("10 20 30 40")
print(result2)

result3 = solution("10 Z 20 Z 1")
print(result3)

result4 = solution("10 Z 20 Z")
print(result4)

result5 = solution("-1 -2 -3 Z")
print(result5)