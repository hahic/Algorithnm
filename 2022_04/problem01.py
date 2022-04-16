import sys

def push(stack, data):
    result = stack

    try:
        result.append(data)

    except Exception as e:
        result = stack
        print(e)

    return result


def pop(stack):
    result_stack, result = stack, -1

    try:
        result = result_stack.pop() if len(result_stack) > 0 else -1

    except Exception as e:
        result_stack, result = stack, -1
        print(e)

    return result_stack, result


def size(stack):
    result = 0

    try:
        result = len(stack)

    except Exception as e:
        result = 0
        print(e)

    return result


def empty(stack):
    result = 0

    try:
        result = 0 if len(stack) > 0 else 1

    except Exception as e:
        result = 0
        print(e)

    return result


def top(stack):
    result = -1

    try:
        result = stack[-1] if len(stack) > 0 else -1

    except Exception as e:
        result = -1
        print(e)

    return result



if __name__ == '__main__':
    try:
        step = sys.stdin.readline().rstrip()
        stack = list()

        for x in range(int(step)):
            command = sys.stdin.readline().rstrip()

            if 'push' in command:
                data = int(command.replace('push', '').strip())
                stack = push(stack, data)

            elif 'pop' in command:
                stack, result = pop(stack)
                print(result)
                
            elif 'size' in command:
                result = size(stack)
                print(result)

            elif 'empty' in command:
                result = empty(stack)
                print(result)

            elif 'top' in command:
                result = top(stack)
                print(result)

    except Exception as e:
        print(e)