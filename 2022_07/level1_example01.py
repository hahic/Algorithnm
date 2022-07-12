# 신고 결과 받기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/92334?language=python3


def solution(id_list, report, k):
    answer = [0 for id in id_list]

    id_data = {}
    for id in id_list:
        id_data[id] = {"declare": [], "abort": [], "count": 0}

    id_abort = []
    for r in report:
        person1, person2 = str(r).split(' ')[0], str(r).split(' ')[1]

        if not person2 in id_data[person1]["declare"]:
            id_data[person1]["declare"].append(person2)
            id_data[person2]['count'] += 1

            if id_data[person2]['count'] == k:
                id_abort.append(person2)

    count = 0
    for data in id_data:
        for abort in id_abort:
            if abort in id_data[data]["declare"]:
                id_data[data]["abort"].append(abort)
        
        answer[count] = len(id_data[data]["abort"])
        count += 1

    return answer

# [ 정답 ]
# def solution(id_list, report, k):
#     answer = [0] * len(id_list)    
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer


if __name__ == "__main__":
    try:
        solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
    
    except Exception as e:
        print(e)