def solution(bandage, health, attacks):
    max_health = health
    last_attack = attacks[-1][0]
    
    cnt = 0
    
    for i in range(1,last_attack+1):
        if i == attacks[0][0]:
            health -= attacks[0][1]
            cnt = 0
            attacks.pop(0)
            if health <= 0 :
                return -1
            
        else:
            cnt+=1
            if cnt < bandage[0] : 
                health = min(health+bandage[1], max_health)
            else:
                health = min(max_health, health+bandage[1]+bandage[2])
                cnt = 0
        print(i , health, cnt)
    return health