import sys


class StackCustom:
    memory = list()

    def __init__(self):
        self.memory = list()


    def pop(self):
        result = -1

        try:
            result = self.memory.pop() if len(self.memory) > 0 else -1

        except Exception as e:
            result = -1
            print(e)

        return result


    def push(self, data):
        result = True

        try:
            self.memory.append(data)

        except Exception as e:
            result = False
            print(e)

        return result


    def top(self):
        result = -1

        try:
            result = self.memory[-1] if len(self.memory) > 0 else -1

        except Exception as e:
            result = -1
            print(e)

        return result


    def empty(self):
        result = True

        try:
            result = False if len(self.memory) > 0 else True

        except Exception as e:
            result = True
            print(e)

        return result

    
    def size(self):
        result = -1

        try:
            result = len(self.memory)

        except Exception as e:
            result = -1
            print(e)

        return result
    
        
def check_vps(ps):
    result = True

    try:
        s = StackCustom()
        count = len(ps)

        for i in range(count):
            if ps[i] == '(':
                s.push(1)

            elif ps[i] == ')':
                if s.size() == 0:
                    result = False
                    break
                else:
                    s.pop()

        if s.size() > 0:
            result = False

    except Exception as e:
        result = False
        print(e)

    return result

    
if __name__ == '__main__':
    try:
        step = sys.stdin.readline().rstrip()
        
        for i in range(int(step)):
            data = sys.stdin.readline().rstrip()
            result = check_vps(data)

            print('NO') if result == False else print('YES')
    
    except Exception as e:
        print(e)