def solution(s):
    def split_string(s):
        count_x = 0
        count_other = 0
        for char in s:
            if char == s[0]:
                count_x += 1
            else:
                count_other += 1
        return count_x == count_other

    result = []
    while s:
        for i in range(len(s)):
            if split_string(s[:i+1]):
                result.append(s[:i+1])
                s = s[i+1:]
                break
            elif i == len(s) - 1:
                result.append(s)
                s = ""
    return len(result)

s1 = "banana"
print(solution(s1))
s2 = "abracadabra"
print(solution(s2))
s3 = "aaabbaccccabba"
print(solution(s3))