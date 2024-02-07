def solution(A, B):
    if len(A) != len(B):
        return -1
    
    for i in range(len(A)):
        if A[-i:] + A[:-i] == B:
            return i
        
    return -1

print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution("atat", "tata"))
print(solution("abc", "abc"))