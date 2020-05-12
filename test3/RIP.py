class RIP:
    def __init__(self, goal, distance, next):
        self.goal = goal
        self.distance = distance
        self.next = next
        self.result = '无更新'

    def adddistance(self):
        self.distance += 1

    def output(self, flag):
        if flag == 0:
            print("目的网络: %s,距离: %d,下一跳地址: %s" % (self.goal, self.distance, self.next))
        else:
            print("目的网络: %s,距离: %d,下一跳地址: %s,原因: %s" % (self.goal, self.distance, self.next, self.result))

    @staticmethod
    def updatetable(B_table, C_table):
        for i in range(len(C_table)):
            flag = True
            for j in range(len(B_table)):
                # 同目的
                if C_table[i].goal == B_table[j].goal:
                    # 同目的，同下一跳
                    if C_table[i].next == B_table[j].next:
                        # print("同目的，同下一跳，直接更新")
                        B_table[j].distance = C_table[i].distance
                        B_table[j].result = "同目的，同下一跳，直接更新"
                    # 同目的，不同下一跳
                    else:
                        if C_table[i].distance < B_table[j].distance:
                            # print('同目的，不同下一跳，选距离短的')
                            B_table[j].distance = C_table[i].distance
                            B_table[j].next = C_table[i].next
                            B_table[j].result = '同目的，不同下一跳，选距离短的'
                        elif C_table[i].distance == B_table[j].distance:
                            # print('同目的，不同下一跳，距离相同，不变')
                            B_table[j].result = '同目的，不同下一跳，距离相同，不变'
                        else:
                            # print('同目的，不同下一跳，来的距离长，不变')
                            B_table[j].result = '同目的，不同下一跳，来的距离长，不变'
                    flag = False
                    break
            if flag:
                # print('新项，直接添加')
                C_table[i].result = '新项，直接添加'
                B_table.append(C_table[i])

    @staticmethod
    def addvalue(List):
        for item in List:
            item.adddistance()

    @staticmethod
    def changenext(List, string):
        for item in List:
            item.next = string

    def cmp(self, item):
        if self.goal == item.goal and self.distance == item.distance and self.next == item.next:
            return True
        else:
            return False
