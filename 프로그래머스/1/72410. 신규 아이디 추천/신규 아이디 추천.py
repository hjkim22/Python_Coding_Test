import re

def solution(new_id):
    new_id = new_id.lower()
    
    new_id = re.sub(r"[^a-z0-9-_.]", "", new_id)
    
    new_id = re.sub(r"\.{2,}", ".", new_id)
    
    new_id = new_id.strip(".")
    
    if not new_id:
        new_id = "a"
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip(".")
    
    while len(new_id) <= 2:
        new_id += new_id[-1]
    
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))