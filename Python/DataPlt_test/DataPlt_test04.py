import matplotlib.pyplot as plt
import numpy as np

# データ生成
x = np.linspace(0, 10, 100)
y = x + np.random.randn(100) 

# Figureの初期化
fig = plt.figure(figsize=(12, 8)) #...1

# Figure内にAxesを追加()
ax = fig.add_subplot(111) #...2
ax.plot(x, y, label="test") #...3

# 凡例の表示
plt.legend()

# プロット表示(設定の反映)
plt.show()