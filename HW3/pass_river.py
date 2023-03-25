objs = ["人", "狼", "羊", "菜"]
state = [0, 0, 0, 0]  # 初始狀態: 人在左岸，其它物品都在左岸

# 取得鄰居狀態
def neighbors(s):
    side = s[0]  # 當前邊（左岸或右岸）
    next_states = []
    next_states.append(move(s, 0))  # 把人帶走
    for i in range(1, len(s)):
        # 如果 i 物品與人在同一邊，就可以把它帶到對岸
        if s[i] == side:
            next_states.append(move(s, i))
    return next_states

# 判斷是否有狀態不合法，也就是“狼吃羊”或“羊吃菜”
def is_dead(s):
    if s[1] == s[2] and s[1] != s[0]: # 狼吃羊
        return True
    if s[2] == s[3] and s[2] != s[0]: # 羊吃菜
        return True
    return False

# 移動物品到對岸
def move(s, obj):
    new_s = s.copy()  # 複製一份陣列
    side = s[0]  # 當前邊（左岸或右岸）
    another_side = 1 - side  # 對岸
    new_s[0] = another_side  # 人移到對岸
    new_s[obj] = another_side  # 物品移到對岸
    if is_dead(new_s):
        return None  # 狀態不合法
    return new_s

visited_map = {}  # 紀錄已經訪問過的狀態

# 判斷狀態是否已經被訪問過
def visited(s):
    str_s = "".join(str(x) for x in s)  # 把狀態轉換成字串
    return str_s in visited_map

# 判斷是否達到目標狀態
def success(s):
    for i in range(1, len(s)):
        if s[i] == 0:
            return False
    return True

# 把狀態轉換成字串
def state2str(s):
    str_s = ""
    for i in range(len(s)):
        str_s += objs[i] + str(s[i]) + " "
    return str_s

path = []  # 紀錄路徑

# 列印路徑
def print_path(path):
    for p in path:
        print(state2str(p))

def dfs(s):
    if visited(s): # 如果這個狀態已經被訪問過，則返回
        return
    path.append(s) # 將當前狀態加入路徑中
    if success(s): # 如果已經達到成功的狀態，則輸出結果並返回
        print("success!")
        print_path(path)
        return
    visited_map["".join(str(x) for x in s)] = True # 把當前狀態標記為已訪問
    next_states = neighbors(s) # 找到下一個可能的狀態
    for next_s in next_states: # 遍歷所有可能的下一個狀態
        if next_s is not None:
            dfs(next_s)  # 如果下一個狀態合法，則繼續往下搜索
    path.pop()
# 從路徑中移除當前狀態
dfs(state)
