# 신규 아이디 추천
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/72410
import re

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub("[^a-z|0-9|\-|\_|.]", "", answer)

    while (len(answer) > 1) and (answer.find('..') != -1):
        answer = answer.replace("..", ".")
    
    if answer[0] == '.':
        answer = 'a' if len(answer) == 1 else answer[1:]
    if answer[-1] == '.':
        answer =  'a' if len(answer) == 1 else answer[:len(answer)-1]
    if len(answer) == 0:
        answer = 'a'
    
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:len(answer)-1]
    elif len(answer) < 3:
        loop = 3 - len(answer)
        answer = answer + (answer[-1] * loop)

    return answer


# [ 정답 ]
# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st


if __name__ == "__main__":
    try:
        print(solution("a...a"))
    
    except Exception as e:
        print(e)