import sys

if __name__ == '__main__':
    try:
        count = int(sys.stdin.readline().rstrip())
        data = []
        result = 0

        for i in range(int(count)):
          d = sys.stdin.readline().rstrip()
          data.append({'t': int(d.split(' ')[0]), 'p': int(d.split(' ')[1])})  

        for index in reversed(range(count)):
            if index + data[index]['t'] > count:
                data[index]['p'] = 0 if (index+1) >= count else data[index+1]['p']
            else:
                p1 = 0 if (index+1) >= count else data[index+1]['p']
                p2 = data[index]['p'] if index+data[index]['t'] >= count else data[index]['p'] + data[index+data[index]['t']]['p']

                data[index]['p'] = max(p1, p2)

        result = data[0]['p']
        print(result)

    except Exception as e:        
        print(e)