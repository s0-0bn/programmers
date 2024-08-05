N, K = map(int, input().split())
cnt=0
prime = [None]*(N+1)

for i in range(2, N+1):
    for j in range(i, N+1, i):
        if prime[j] != 0:
            cnt+=1
            prime[j] = 0 
            if cnt == K:
                print(j)