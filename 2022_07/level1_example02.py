# 로또의 최고 순위와 최저 순위
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]

    for lotto in lottos:
        if lotto in win_nums:
            win_nums.remove(lotto)

    zero_number = lottos.count(0)
    correct_number = len(lottos) - len(win_nums)
    answer = [rank[zero_number + correct_number], rank[correct_number]]

    return answer


# [ 정답 ]
# def solution(lottos, win_nums):

#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]


if __name__ == '__main__':
    try:
        print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))

    except Exception as e:
        print(e)