import matplotlib.pyplot as plt
from scipy.optimize import minimize
import random
import numpy as np

# x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
# y = np.array([2, 3, 4, 5, 6], dtype=np.float32)
x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([1.2 , 3.4 , 4.8 , 5.4 , 6.8], dtype=np.float32)

def predict(a, xt):
    return a[0]+a[1]*xt

def MSE(a, x, y):
    total = 0
    for i in range(len(x)):
	    total += (y[i]-predict(a,x[i]))**2
    return total

def loss(p):
	return MSE(p, x, y)

# p = [0.0, 0.0]
# plearn = optimize(loss, p, max_loops=3000, dump_period=1)
def optimize():
    # 請修改這個函數，自動找出讓 loss 最小的 p 
    #p = [2,1] # 這個值目前是手動填的，請改為自動尋找。(即使改了 x,y 仍然能找到最適合的回歸線)
    #p = [2,1] # 這個值目前是手動填的，請改為自動尋找。(即使改了 x,y 仍然能找到最適合的回歸線)
    """
        # 定義初始參數值
        p = [0, 0]
        # 最小化 MSE
        res = minimize(loss, p, method='BFGS')
        # 取得最小化後的參數值    
        p = res.x.tolist()
    """
     # 定義初始參數值
    p = [0, 0]
    best_loss = float('inf')

    # 定義爬山演算法的參數
    step_size = 0.01
    max_iterations = 100000

    # 執行爬山演算法
    for i in range(max_iterations):
        # 在鄰域中隨機選擇一個參數
        j = random.randint(0, 1)

        # 嘗試增加或減少該參數的值
        delta = random.uniform(-step_size, step_size)
        p[j] += delta

        # 計算目標函數的值
        current_loss = loss(p)

        # 如果目標函數的值更小，就更新最佳參數值
        if current_loss < best_loss:
            best_loss = current_loss
        else:
            p[j] -= delta
    return p

p = optimize()


# Plot the graph
y_predicted = list(map(lambda t: p[0]+p[1]*t, x))
print('y_predicted=', y_predicted)
plt.plot(x, y, 'ro', label='Original data')
plt.plot(x, y_predicted, label='Fitted line')
plt.legend()
plt.show()
