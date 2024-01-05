def solution(strlist):
    answer = [len(w) for w in strlist]
    return answer

word1 = ["We", "are", "the", "world!"]
word2 = ["I", "Love", "Programmers."]

print(solution(word1))
print(solution(word2))