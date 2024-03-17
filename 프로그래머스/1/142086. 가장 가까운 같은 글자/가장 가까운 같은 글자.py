def solution(s):
    result = []
    seen = {}

    for i, char in enumerate(s):
        if char in seen:
            result.append(i - seen[char])
        else:
            result.append(-1)
        seen[char] = i

    return result

print(solution("banana"))
print(solution("foobar"))