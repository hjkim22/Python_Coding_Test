def solution(skill, skill_trees):
    skillset = set(skill)
    answer = 0
    
    for skill_tree in skill_trees:
        i, j = 0, 0
        valid = True
        while i < len(skill) and j < len(skill_tree):
            if skill_tree[j] in skillset:
                if skill_tree[j] != skill[i]:
                    valid = False
                    break
                else:
                    i += 1
                    j += 1
            else:
                j += 1
                
        if valid:
            answer += 1

    return answer