class Node:
    def __init__(self, data, depth, f):
        self.data = data
        self.depth = depth
        self.f = f


    def move(self, puz, x1, y1, x2, y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            for i in puz:
                t = []
                for j in i:
                    t.append(j)
                temp_puz.append(t)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp

            return temp_puz
        else:
            return None

    def find(self, puz, x):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j

    def g_child(self):
        x, y = self.find(self.data, '*')
        list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in list:
            child = self.move(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.depth + 1, 0)
                children.append(child_node)
        return children



class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def input_m(self):
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def h_score(self, start, goal):
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '*':
                    temp += 1
        return temp

    def f_score(self, start, goal):
        return self.h_score(start.data, goal) + start.depth

    def generate(self):
        print("Enter the start state matrix (using * as the blank block in the puzzle) \n")
        start = self.input_m()
        print("Enter the goal state matrix (using * as the blank block in the puzzle) \n")
        goal = self.input_m()
        start = Node(start, 0, 0)
        start.f = self.f_score(start, goal)
        self.open.append(start)
        ste = 1
        while True:
            cur = self.open[0]
            print("----- step ",ste,"-----")
            ste +=1

            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")
            for i in cur.g_child():
                i.f = self.f_score(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]
            self.open.sort(key=lambda x: x.f, reverse=False)
            print("f --> ", self.f_score(cur,goal))
            print("h --> ", self.h_score(cur.data,goal))
            print("g --> ",cur.depth)
            if (self.h_score(cur.data, goal) == 0):
                break

n = input("please enter n : ")
puz = Puzzle(int(n))
puz.generate()