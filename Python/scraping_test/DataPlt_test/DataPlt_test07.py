import matplotlib.pyplot as plt
# プロット領域の初期化(今回は1行2列の配列)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))

# データのプロット
ax1.bar([1,2,3], [3,4,5])
ax2.barh([0.5, 1, 2.5], [0,1,2])

plt.show()