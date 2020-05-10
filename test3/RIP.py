class RIP:
    def __init__(self, goal, distance, next):
        self.goal = goal
        self.distance = distance
        self.next = next

    def adddistance(self):
        self.distance += 1

    def output(self):
        print("目的地址%s,距离%d,下一跳地址%s" % (self.goal, self.distance, self.next))
