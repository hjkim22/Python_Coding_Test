import re
from collections import Counter

def make_multiset(s):
    s = s.lower()
    return [s[i:i+2] for i in range(len(s) - 1) if re.match('[a-z]{2}', s[i:i+2])]

def solution(str1, str2):
    set1 = make_multiset(str1)
    set2 = make_multiset(str2)
    
    counter1 = Counter(set1)
    counter2 = Counter(set2)
    
    intersection = counter1 & counter2
    union = counter1 | counter2
    
    inter_size = sum(intersection.values())
    union_size = sum(union.values())
    
    if union_size == 0:
        return 65536
    
    jaccard_similarity = inter_size / union_size
    return int(jaccard_similarity * 65536)

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))