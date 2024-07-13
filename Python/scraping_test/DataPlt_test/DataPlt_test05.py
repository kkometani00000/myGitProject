import matplotlib.pyplot as plt
import numpy as np

# データ生成
x = np.linspace(0, 10, 100)
y = x + np.random.randn(100) 

# Figureの初期化
fig = plt.figure(figsize=(12, 8))

# Figure内にAxesを追加
ax = fig.add_axes([0,0,1,1])
ax.plot(x, y, label="test")

# 凡例の表示
plt.legend()

# プロット表示(設定の反映)
plt.show()