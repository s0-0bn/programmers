def solution(babbling):
    answer = 0
    box = []
    babe = ['aya','ye','woo','ma']
    
    for i in babbling:
        for j in babe:
            if j in i:
                i = i.replace(j,'%%')
            
        box.append(i)
    for i in box:
        if set(i) == {"%"}:
            answer+=1
    return answer


'''babbling의 단어가 4가지로 다 나눠줘야 함
ayayee 가 나왔다. 하면, 일단 %% 으로 교체 해줬음
지금 테스트1에서 wyeoo 때문에 문제가 발생했는데
ye가 수정되면 woo 가 되서 이게 바뀌면 안되는데 바뀌고 있음
그래서 이부분 수정해야함!! 우얄까 우얘'''