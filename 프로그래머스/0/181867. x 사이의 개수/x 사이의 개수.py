def solution(myString):
    lengths = []
    substrings = myString.split('x')
    
    for substring in substrings:
        lengths.append(len(substring))
    
    return lengths

myString1 = "oxooxoxxox"
myString2 = "xabcxdefxghi"
print(solution(myString1))
print(solution(myString2))