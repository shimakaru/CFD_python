import numpy as np
import matplotlib.pyplot as plt

# 初期設定
g=9.8
v0=10
h0=0
dt=0.1

plt.figure(figsize=(7,7),dpi=100)
plt.rcParams["font.size"]=25

# 解析解(Analytical Solution)
t = np.linspace(0, 2 * v0 / g, 100)
h = - 0.5 * g * t ** 2 + v0 * t + h0  # 式(1.1)
la, = plt.plot(t, h, color='blue')

# 数値解(Numerical Solution)
t = 0
h = h0
while h >= h0:
    ln = plt.scatter(t, h, marker='o', c='black')
    h += (-g * t + v0) * dt # 式(1.7)
    t += dt 

# グラフの後処理
plt.grid(color='black', linestyle='dashed', linewidth=0.5)
plt.xlabel('Time')
plt.ylabel('Height')
plt.legend(handles=[la, ln], labels=['Analytical', 'Numerical'])
plt.show()