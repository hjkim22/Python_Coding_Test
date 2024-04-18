def solution(strArr):
    return [s for s in strArr if "ad" not in s]

print(solution(["and", "notad", "abcd"]))
print(solution(["there", "are", "no", "a", "ds"]))