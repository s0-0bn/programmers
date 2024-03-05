import re
def solution(my_string):
    my_string = re.sub('[^1-9]','',my_string) 
    return sum([int(i) for i in str(my_string)])