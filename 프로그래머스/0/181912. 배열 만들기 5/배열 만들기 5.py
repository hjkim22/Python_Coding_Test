def solution(intStrs, k, s, l):
    result = []
    for string in intStrs:
        substring = string[s:s+l]
        integer = int(substring)
        if integer > k:
            result.append(integer)
    return result

intStrs = ["0123456789", "9876543210", "9999999999999"]
k = 50000
s = 5
l = 5
print(solution(intStrs, k, s, l))