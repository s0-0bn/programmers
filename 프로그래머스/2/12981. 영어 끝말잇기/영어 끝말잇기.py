def solution(n, words):
    box = [words[0]]
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0]:
            return [(i%n)+1, (i//n)+1]
        
        if words[i] in box:
            print(i)
            return [(i%n)+1, (i//n)+1]
        
        box.append(words[i])
    return [0,0]