import numpy as np
import matplotlib.pyplot as plt

# 初期設定
c = 1
dt = 0.05
dx = 0.1

jmax = 21
nmax = 6

x = np.linspace(0, dx * (jmax - 1), jmax)

q = np.zeros(jmax)
for j in range(jmax):
    if (j < jmax / 2):
        q[j] = 1
    else:
        q[j] = 0


plt.figure(figsize=(7,7), dpi=100) # グラフのサイズ
plt.rcParams["font.size"] = 22 # グラフの文字サイズ

# 初期分布の可視化
plt.plot(x, q, marker='o', lw=2, label='n=0')

for n in range(1, nmax + 1):
    qold = q.copy()
    for j in range(1, jmax-1):
        q[j] = qold[j] - dt * c * (qold[j + 1] - qold[j - 1]) / (2 * dx)  # 式(2.7)

    # 各ステップの可視化
    if n % 2 == 0:
        plt.plot(x, q, marker='o', lw=2, label=f'n={n}')

# グラフの後処理
plt.grid(color='black', linestyle='dashed', linewidth=0.5)
plt.xlim([0, 2.0])
plt.xlabel('x')
plt.ylabel('q')
plt.legend()
plt.show()