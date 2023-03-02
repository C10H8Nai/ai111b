'''
參考資料：
老師的範例
chatGPT的解說
110910541 魏仲彥 的TSP.py代碼
'''
import math
import numpy as np
import random

#使用字典做儲存，key為點，value為[x, y]
xy = {  1: [0 , 0],
        2: [1 , 0],
        3: [2 , 0],
        4: [3 , 0],
        5: [3 , 1],
        6: [3 , 2],
        7: [3 , 3],
        8: [2 , 3],
        9: [1 , 3],
        10: [0 , 3],
        11: [0 , 2],
        12: [0 , 1]
    }
class TSP:
    """
    搜尋最短路徑，主要觸發函數是calculate
    graph : 輸入圖形
    """
    def __init__(self , graph):
        self.graph = graph  # 字典，存圖
        self.score = 0  # 存路徑長度。越低越好
        self.order = []  # 存順序，就是存取上面字典的key
    
    def calculate(self, tolerate, times):
        """
        搜尋最短路徑，主要觸發函數是calculate
        param tolerate : 比較次數，如果跑多次都大於原本的值，就退出並return最好的結果
        param times : swap的次數 
        return [score, order] : 回傳路徑長度(越低越好)和路徑排序
        """
        # 初始化參數
        self.ListInit() # 將self.order初始化為字典的key順序
        l = len(self.order) # 計算點的個數
        pre_score = self.score # 初始化之前的路徑長度
        pre_order = self.order # 初始化之前的路徑排序
        tol = tolerate # 複製tolerate的值
        loop = 0 # 初始化迴圈次數
        while True:
            self.score = 0 # 初始化路徑長度
            # self.order = self.swap()
            for i in range(l - 1):
                # 計算兩個點之間的距離
                now_pos = self.graph[self.order[i]]
                next_pos = self.graph[self.order[i + 1]]
                h = self.distance(now_pos , next_pos)
                for _ in range(times):
                    # 使用random做replace
                    new_order = self.replace(i+1, random.randint(i+1, l-1))
                    # 呼叫self.replace方法，以第i+1個點和i+1到l-1的其中一個隨機點進行交換，返回新的順序new_order
                    now_pos = self.graph[new_order[i]] # 根據新順序，取得第i個點的座標now_pos
                    next_pos = self.graph[new_order[i + 1]] # 根據新順序，取得下一個點的座標next_pos
                    nh = self.distance(now_pos , next_pos) # 根據新順序，取得下一個點的座標next_pos
                    print(self.order)
                    print(new_order)
                    loop += 1 # 迴圈次數加1
                    if h > nh:
                        self.order = new_order # 更新路徑排序
                self.score += self.distance(now_pos , next_pos) # 更新路徑長度
                
            # 判斷是否需要退出
            if not tol: # tolerate為0時
                print('loop = ', loop) # 輸出迴圈次數
                return [pre_score, pre_order] # 回傳之前的結果

            if self.score < pre_score: # 當路徑長度變小時
                if not tol: # tolerate為0時
                    return [self.score, self.order] # 回傳最好的結果
                else:
                    # print(tol)
                    pre_order = self.order # 更新之前的路徑排序
                    pre_score = self.score # 更新之前的路徑排序
                    tol = tolerate # 更新之前的路徑排序
            elif not pre_score: # 當之前的路徑長度為0時
                pre_score = self.score # 更新之前的路徑長度
            else:
                tol -= 1 # 更新之前的路徑長度
        
            


    def distance(self, a, b):
        """
        計算距離
        return distence: 兩點的路徑
        """
        dx = a[0]-b[0]
        dy = a[1]-b[1]
        return (dx**2 + dy**2)**0.5

    def replace(self, a, b):
        """
        兩點做交換，上方的calculate裡面是使用random與除第一點外的點做交換
        :param a: 交換成b
        :param b: 交換成a
        :return new_order: 新的順序
        """
        l = len(self.order)
        new_order = []
        for i in range(l):
            if a == i:
                new_order.append(self.order[b])
            elif b == i:
                new_order.append(self.order[a])
            else:
                new_order.append(self.order[i])

        return new_order
    
    def ListInit(self):
        """
        使用.items()抓字典元素
        初始化順序(self.order)
        :return : 初始順序
        """
        for key, value in self.graph.items():
            self.order.append(key)
            
ans = TSP(xy)
print(xy)
print(ans.calculate(10, 3))  # 裡面的tolerate和times越大，就會算越準



'''
    def circle_length(self, s):
        d = 0.0
        for i in range(len(s)):
            d += self.distance(xy[i], xy[s[i]])
        return d
        
    def get_neighbor(s):
        idx1, idx2 = random.sample(range(len(s)), 2)
        s_new = s.copy()
        s_new[idx1], s_new[idx2] = s_new[idx2], s_new[idx1]
        return s_new

    def hill_climbing(s):
        d = circle_length(s)
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                print(s)
                new_s = s.copy()
                new_s[i], new_s[j] = new_s[j], new_s[i]
                new_d = circle_length(new_s)
                if new_d <= d:
                    s = new_s
                    d = new_d
        return s
    
'''

"""
s0 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1]
#sa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
sa = s0.copy()
random.shuffle(sa)
print('sa=', sa)
"""

'''
def hill_climbing(s):
    print(s)
    replace(s)
    best_s = s.copy()
    best_d = circle_length(s)
    neighbors = get_neighbors(s)
    for neighbor in neighbors:
        d = circle_length(neighbor)
        if d < best_d:
            best_s = neighbor.copy()
            best_d = d
    return best_s, best_d
def replace(stemp):
    idx1, idx2 = random.sample(range(len(stemp)), 2)
    stemp[idx1], stemp[idx2] = stemp[idx2], stemp[idx1]
loop = 0
loop_Pos = 0
loop_Nega = 0

d0 = circle_length(s0)
dt = circle_length(sa)
print('circle_length(s0) = ', circle_length(s0))
print('circle_length(sa) = ', circle_length(sa))

while True:
    print(sa)
    print('circle_length(sa) = ', circle_length(sa))
    neighbor = hill_climbing(sa)
    dn = circle_length(neighbor)
    if(d0-dn < d0-dt):
        sa = neighbor
        dt = circle_length(neighbor)
        continue
    elif(sa == s0):
        break
    else:
        print('s0=', s0)
        print('circle_length(s0)=', circle_length(s0))

        print('sa=', sa)
        print('circle_length(sa)=', circle_length(sa))
        
        print('sn=', neighbor)
        print('circle_length(sn)=', circle_length(neighbor))
        
        continue

while True:
    loop += 1
    d0 = circle_length(s0)
    dt = circle_length(sa)
    
    if(d0 != dt):
        sa = hill_climbing(sa)
        if(d0 - circle_length(sa) < d0 - dt):
            print('sa=', sa)
            print('circle_length(sa)=', circle_length(sa))
            loop_Pos += 1
            continue
        else:
            loop_Nega += 1
            continue
    else:
        if (sa == s0):
            break
        else:
            sa = hill_climbing(sa)
    if(d0 != dt):
        replace(sa)
        if(d0 - circle_length(sa) < d0 - dt):
            print('sa=', sa)
            print('circle_length(sa)=', circle_length(sa))
            loop_Pos += 1
            continue
        else:
            loop_Nega += 1
            continue
    else:
        print('sa=', sa)
        if (sa == s0):
            break
        break
    
    
    #if(circle_length(sa) < circle_length(s0)):
        #break
    if(loop > 1000):
        break

while dt != d0:
    sa, dt = hill_climbing(sa)
    
print('loop_Pos = ', loop_Pos)
print('loop_Nega = ', loop_Nega)

print('s0=', s0)
print('circle_length(s0)=', circle_length(s0))

print('sa=', sa)
print('circle_length(sa)=', circle_length(sa))
'''
