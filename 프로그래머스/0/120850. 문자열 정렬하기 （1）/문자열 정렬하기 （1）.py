def solution(my_string):
    numbers = [int(char) for char in my_string if char.isdigit()]
    sorted_numbers = sorted(numbers)
    return sorted_numbers

print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))