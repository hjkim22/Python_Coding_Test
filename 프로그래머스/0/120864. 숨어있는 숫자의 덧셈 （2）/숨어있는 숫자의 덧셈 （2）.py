def solution(my_string):
    numbers = []
    current_number = ""
    
    for char in my_string:
        if char.isdigit():
            current_number += char
        elif current_number:
            numbers.append(int(current_number))
            current_number = ""

    if current_number:
        numbers.append(int(current_number))

    return sum(numbers)

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123Z"))