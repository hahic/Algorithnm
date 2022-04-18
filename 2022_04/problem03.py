import sys

if __name__ == '__main__':
    try:
        count = sys.stdin.readline().rstrip()
        result = 0

        loop = int(count)
        while(loop > 0):
            if (loop % 5) == 0:
                result += 1
                loop -= 5
            elif (loop % 3) == 0:
                result += 1 
                loop -= 3
            elif loop > 5:
                result += 1
                loop -= 5
            else:
                result = -1
                break

        print(result)

    except Exception as e:
        print(e)