def solution(numbers):
    answer = 0
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i,j in enumerate(nums):
        numbers = numbers.replace(j,str(i))
    return int(numbers)