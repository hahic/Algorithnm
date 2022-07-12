import sys

if __name__ == '__main__':
    count = sys.stdin.readline().rstrip()
    datas = sys.stdin.readline().rstrip()

    parent = -1
    result = []
    for i in range(int(count)):
        target = int(datas.split(' ')[i])
        
        if parent < target:
            parent = target
            result.append(target)

    print(len(result))
    print(' '.join(str(x) for x in result))
