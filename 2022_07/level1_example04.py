# 숫자 문자열과 영단어
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = 0
    list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in list:
        if i in s:
           s = s.replace(i, str(list.index(i)))
        #    print(s)

    answer = int(s)

    return answer


if __name__ == '__main__':
    try:
        print(solution("2three45sixseven"))

    except Exception as e:
        print(e)