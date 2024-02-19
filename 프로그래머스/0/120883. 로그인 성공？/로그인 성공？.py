def solution2(id_pw, db):

    id_lst = [i[0] for i in db]
    pw_lst = [i[1] for i in db]
    
    if id_pw[0] in id_lst :
        if id_pw[1] == pw_lst[id_lst.index(id_pw[0])]:
            return 'login'
        else:
            return "wrong pw"
    return "fail"

def solution(id_pw, db):
    for ID, PW in db:
        if id_pw[0]==ID and id_pw[1]==PW:
            return "login"
        elif id_pw[0]==ID and id_pw[1]!=PW:
            return "wrong pw"
    return "fail"