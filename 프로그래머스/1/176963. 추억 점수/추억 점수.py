def solution(name, yearning, photo):
    answer = []
    name_to_yearning = dict(zip(name, yearning))
    
    for people_in_photo in photo:
        total_yearning = 0
        for person in people_in_photo:
            total_yearning += name_to_yearning.get(person, 0)
        answer.append(total_yearning)
    
    return answer

name1 = ["may", "kein", "kain", "radi"]
yearning1 = [5, 10, 1, 3]
photo1 = [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
print(solution(name1, yearning1, photo1))

name2 = ["kali", "mari", "don"]
yearning2 = [11, 1, 55]
photo2 = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
print(solution(name2, yearning2, photo2))

name3 = ["may", "kein", "kain", "radi"]
yearning3 = [5, 10, 1, 3]
photo3 = [["may"], ["kein", "deny", "may"], ["kon", "coni"]]
print(solution(name3, yearning3, photo3))