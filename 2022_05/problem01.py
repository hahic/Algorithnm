import queue
import sys

class Node:
    def __init__(self) -> None:
        self.marked = False
        self.visited = False
        self.adjacent = []

    def reset(self):
        self.marked = False
        self.visited = False

    def insert_adjacent(self, data):
        self.adjacent.append(data)
        self.adjacent.sort()
    

def dfs(root, nodes, answer):
    try:
        if len(nodes) < root:
            return

        answer.append(root)
        nodes[root].visited = True

        for n in nodes[root].adjacent:
            if nodes[n].visited != True:
                dfs(n, nodes, answer)

    except Exception as e:
        print(e)


def bfs(root, nodes, answer):
    process = queue.Queue()

    try:
        nodes[root].marked = True
        process.put(root)

        while not process.empty():
            target = process.get()

            answer.append(target)
            nodes[target].visited = True

            for n in nodes[target].adjacent:
                if nodes[n].marked != True:
                    nodes[n].marked = True
                    process.put(n)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    try:
        input = sys.stdin.readline().rstrip()

        count_n = int(input.split(' ')[0])
        count_m = int(input.split(' ')[1])
        start_node = int(input.split(' ')[2])

        nodes = [Node() for i in range(count_n+1)]
        for i in range(count_m):
            input = sys.stdin.readline().rstrip()
            node_first = int(input.split(' ')[0])
            node_second = int(input.split(' ')[1])

            test = nodes[node_first]
            nodes[node_first].insert_adjacent(node_second)
            nodes[node_second].insert_adjacent(node_first)

        # DFS(= Depth-First Search)
        for n in nodes:
            n.reset()
        result_dfs = []
        dfs(start_node, nodes, result_dfs)
        print(' '.join(str(x) for x in result_dfs))

        # BFS(= Breath-First Search)
        for n in nodes:
            n.reset()
        result_bfs = []
        bfs(start_node, nodes, result_bfs)
        print(' '.join(str(x) for x in result_bfs))

    except Exception as e:
        print(e)