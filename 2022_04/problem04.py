import sys

if __name__ == '__main__':
    result = 0

    try:
        count = sys.stdin.readline().rstrip()
        times = sys.stdin.readline().rstrip().split(' ')
        times = [int(x) for x in times]
        times.sort(reverse=True)

        for i in range(int(count)):
            target = times[i]
            result += (target * (i + 1))

        print(result)

    except Exception as e:
        print(e)