def solution(id_pw, db):

    id_lst = [i[0] for i in db]
    pw_lst = [i[1] for i in db]
    
    if id_pw[0] in id_lst :
        if id_pw[1] == pw_lst[id_lst.index(id_pw[0])]:
            return 'login'
        else:
            return "wrong pw"
    return "fail"