def solution(s):
    import re
    from collections import defaultdict
    
    s = s[2:-2]
    s = s.split("},{")
    
    sets = []
    for subset in s:
        sets.append(set(map(int, subset.split(','))))
    
    sets.sort(key=len)
  
    answer = []
    seen = set()
    
    for subset in sets:
        for number in subset:
            if number not in seen:
                answer.append(number)
                seen.add(number)
    
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))