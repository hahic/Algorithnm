# 키패드 누르기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''

    left, right = "*", "#"
    keypad = {
        "0": {"owner": "empty", "price": {"2": 3, "5": 2, "8": 1}},
        "1": {"owner": "L", "price": {"2": 1, "5": 2, "8": 3, "0": 4}},
        "2": {"owner": "empty", "price": {"5": 1, "8": 2, "0": 3}},
        "3": {"owner": "R", "price": {"2": 1, "5": 2, "8": 3, "0": 4}},
        "4": {"owner": "L", "price": {"2": 2, "5": 1, "8": 2, "0": 3}},
        "5": {"owner": "empty", "price": {"2": 1, "8": 1, "0": 2}},
        "6": {"owner": "R", "price": {"2": 2, "5": 1, "8": 2, "0": 3}},
        "7": {"owner": "L", "price": {"2": 3, "5": 2, "8": 1, "0": 2}},
        "8": {"owner": "empty", "price": {"2": 2, "5": 1, "0": 1}},
        "9": {"owner": "R", "price": {"2": 3, "5": 2, "8": 1, "0": 2}},
        "*": {"owner": "empty", "price": {"2": 4, "5": 3, "8": 2, "0": 1}},
        "#": {"owner": "empty", "price": {"2": 4, "5": 3, "8": 2, "0": 1}}
    }
    
    for n in numbers:
        if keypad[str(n)]['owner'] == "empty":
            if keypad[left]['price'][str(n)] == keypad[right]['price'][str(n)]:
                if hand == "left":
                    answer += 'L'
                    left = str(n)
                else:
                    answer += 'R'
                    right = str(n)
            elif keypad[left]['price'][str(n)] < keypad[right]['price'][str(n)]:
                answer += 'L'
                left = str(n)
            else:
                answer += 'R'
                right = str(n)
        elif keypad[str(n)]['owner'] == "L":
            answer += 'L'
            left = str(n)
        else:
            answer += 'R'
            right = str(n)

    return answer


if __name__ == '__main__':
    try:
        print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))
    
    except Exception as e:
        print(e)