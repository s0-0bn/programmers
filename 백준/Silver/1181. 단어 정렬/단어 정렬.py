N = int(input())

lst = []
for _ in range(N):
    lst.append(input())
    
lst = list(set(lst))
lst.sort()
lst.sort(key = lambda x : len(x))

for i in lst:
    print(i)