def solution1(array, commands):
    answer = []
    for i in range(len(commands)):
        rst = array[commands[i][0]-1:commands[i][1]]
        rst.sort()
        answer.append(rst[commands[i][2]-1])
    return answer

def solution2(array, commands):
    answer = []
    for i in range(len(commands)):
        rst = array[commands[i][0]-1:commands[i][1]]
        rst.sort()
        answer.append(rst[commands[i][2]-1])
    return answer

def solution(arr, com):
    ans = []
    for i in range(len(com)):
        rst = arr[com[i][0]-1:com[i][1]]
        rst.sort()
        ans.append(rst[com[i][2]-1])
    return ans