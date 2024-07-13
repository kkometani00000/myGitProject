import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.express as px

path = 'Python\scraping_test\pandas_test'

df = pd.read_csv(f'{path}\_iris.csv', index_col=0)
print(df.head())
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 3           4.6          3.1           1.5          0.2  setosa
# 4           5.0          3.6           1.4          0.2  setosa

index = 0

plt.figure()
df.plot()
plt.savefig(f'{path}\_{(index+1):02}_pandas_iris_line.png')
plt.close('all')

print(type(df.plot()))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
df.plot(ax=ax)
fig.savefig(f'{path}\_{(index+2):02}_pandas_iris_line.png')

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(9, 6))
df.plot(ax=axes[0, 0], legend=False)
df.plot(ax=axes[1, 2], legend=False, kind='hist')
fig.savefig(f'{path}\_{(index+3):02}_pandas_iris_line_axes.png')

current_figsize = mpl.rcParams['figure.figsize']
print(current_figsize)
# [6.0, 4.0]

plt.figure()
df.plot(figsize=(9, 6))
plt.savefig(f'{path}\_{(index+4):02}_pandas_iris_line_figsize.png')
plt.close('all')

current_dpi = mpl.rcParams['figure.dpi']
print(current_dpi)
# 72.0

plt.figure()
df.plot()
plt.savefig(f'{path}\_{(index+5):02}_pandas_iris_line_dpi.png', dpi=current_dpi * 1.5)
plt.close('all')

plt.figure()
df.plot(subplots=True)
plt.savefig(f'{path}\_{(index+6):02}_pandas_iris_line_subplots.png')
plt.close('all')

print(type(df.plot(subplots=True)))
print(type(df.plot(subplots=True)[0]))
# <class 'numpy.ndarray'>
# <class 'matplotlib.axes._subplots.AxesSubplot'>

plt.figure()
df.plot(subplots=True, layout=(2, 2))
plt.savefig(f'{path}\_{(index+7):02}_pandas_iris_line_subplots_layout.png')
plt.close('all')

plt.figure()
df.plot(subplots=True, layout=(2, 2), sharex=True, sharey=True)
plt.savefig(f'{path}\_{(index+8):02}_pandas_iris_line_subplots_share.png')
plt.close('all')

plt.figure()
df.plot(title='Iris Data Set',
        grid=True,
        colormap='Accent',
        legend=False,
        alpha=0.5)
plt.savefig(f'{path}\_{(index+9):02}_pandas_iris_line_etc.png')
plt.close('all')

plt.figure()
df.plot(kind='line')
plt.savefig(f'{path}\_{(index+10):02}_pandas_iris_line.png')
plt.close('all')

plt.figure()
df.plot.line()
plt.savefig(f'{path}\_{(index+11):02}_pandas_iris_line.png')
plt.close('all')

plt.figure()
df.plot.line(subplots=True, layout=(2, 2))
plt.savefig(f'{path}\_{(index+12):02}_pandas_iris_line_subplots_layout.png')
plt.close('all')

plt.figure()
df.plot.line(style=['r--', 'b.-', 'g+', 'k:'])
plt.savefig(f'{path}\_{(index+13):02}_pandas_iris_line_style.png')
plt.close('all')

plt.figure()
#df[:5].plot.bar()
df.plot.bar()
plt.savefig(f'{path}\_15e{(index+50):02}_pandas_iris_bar.png')
plt.close('all')

plt.figure()
#df[:5].plot.barh()
df.plot.barh()
plt.savefig(f'{path}\_16e{(index+51):02}_pandas_iris_barh.png')
plt.close('all')

plt.figure()
#df[:5].plot.bar(stacked=True)
df.plot(stacked=True)
plt.savefig(f'{path}\_14e{(index+52):02}_pandas_iris_bar_stack.png')
plt.close('all')


plt.figure()
df.plot.box()
plt.savefig(f'{path}\_{(index+17):02}_pandas_iris_box.png')
plt.close('all')

plt.figure()
df.plot.hist()
plt.savefig(f'{path}\_{(index+18):02}_pandas_iris_hist.png')
plt.close('all')

plt.figure()
df.plot.hist(alpha=0.5)
plt.savefig(f'{path}\_{(index+19):02}_pandas_iris_hist_alpha.png')
plt.close('all')

plt.figure()
df.plot.hist(stacked=True)
plt.savefig(f'{path}\_{(index+20):02}_pandas_iris_stacked.png')
plt.close('all')

plt.figure()
df.plot.hist(bins=20, histtype='step', orientation='horizontal')
plt.savefig(f'{path}\_{(index+21):02}_pandas_iris_hist_h_step.png')
plt.close('all')

plt.figure()
df.plot.kde(style=['r-', 'g--', 'b-.', 'c:'])
plt.savefig(f'{path}\_{(index+22):02}_pandas_iris_kde.png')
plt.close('all')

plt.figure()
df.plot.area()
plt.savefig(f'{path}\_{(index+23):02}_pandas_iris_area.png')
plt.close('all')

df_pie = pd.DataFrame([[1, 50], [2, 20], [3, 30]],
                      index=['a', 'b', 'c'], columns=['ONE', 'TWO'])

print(df_pie)
#    ONE  TWO
# a    1   50
# b    2   20
# c    3   30

plt.figure()
df_pie.plot.pie(subplots=True)
plt.savefig(f'{path}\_{(index+28):02}_pandas_pie.png')
plt.close('all')

print(type(df_pie.plot.pie(subplots=True)))
print(type(df_pie.plot.pie(subplots=True)[0]))
# <class 'numpy.ndarray'>
# <class 'matplotlib.axes._subplots.AxesSubplot'>

plt.figure()
df_pie['ONE'].plot.pie()
plt.savefig(f'{path}\_{(index+29):02}_pandas_pie_single.png')
plt.close('all')


df = px.data.iris() # iris is a pandas DataFrame
#fig = px.scatter(df, x="sepal_width", y="sepal_length")
#fig.show()

plt.figure()
df.plot(x="sepal_width", y="sepal_length")
plt.savefig(f'{path}\_e{(index+40):02}_pandas_iris_line_xy.png')
plt.close('all')

plt.figure()
df.plot(x='sepal_length')
plt.savefig(f'{path}\_e{(index+41):02}_pandas_iris_line_x.png')
plt.close('all')

plt.figure()
df.plot(y='sepal_length')
plt.savefig(f'{path}\_e{(index+42):02}_pandas_iris_line_y.png')
plt.close('all')

# df.plot(y=['sepal_length', 'sepal_width'])
# UserWarning: Pandas doesn't allow columns to be created via a new attribute name

plt.figure()
ax = df.plot(y='sepal_length')
df.plot(y='sepal_width', ax=ax)
plt.savefig(f'{path}\_e{(index+43):02}_pandas_iris_line_multi.png')
plt.close('all')

plt.figure()
df[['sepal_length', 'sepal_width']].plot()
plt.savefig(f'{path}\_e{(index+44):02}_pandas_iris_line_multi.png')
plt.close('all')


plt.figure()
df.plot.scatter(x='sepal_length', y='petal_length', alpha=0.5)
plt.savefig(f'{path}\_e{(index+61):02}_pandas_iris_scatter.png')
plt.close('all')

plt.figure()
ax = df.plot.scatter(x='sepal_length', y='petal_length', alpha=0.5)
df.plot.scatter(x='sepal_length', y='petal_width',
                marker='s', c='r', s=50, alpha=0.5, ax=ax)
plt.savefig(f'{path}\_e{(index+62):02}_pandas_iris_scatter_multi.png')
plt.close('all')

plt.figure()
df.plot.line(x='sepal_length',
             style=['ro', 'g+', 'bs'], alpha=0.5)
plt.savefig(f'{path}\_e{(index+63):02}_pandas_iris_scatter_line.png')
plt.close('all')

plt.figure()
df.plot.hexbin(x='sepal_length', y='petal_length',
               gridsize=15, sharex=False)
plt.savefig(f'{path}\_e{(index+64):02}_pandas_iris_hexbin.png')
plt.close('all')


X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
H = [10.3,11.6,15.4,19.0,25.3,25.8,27.5,32.8,29.4,23.3,17.7,12.6]
L = [1.4,3.3,6.2,9.2,15.3,18.5,21.6,25.2,21.7,16.4,9.3,5.2]
fig, ax = plt.subplots()
ax.plot(X, H, 'o-', color='tab:red')
ax.plot(X, L, 'x-', color='tab:blue')
for x, hi, lo in zip(X, H, L):
    hs = f'{hi:.1f}'
    ls = f'{lo:.1f}'
    ax.annotate(hs, (x, hi), textcoords='offset points', xytext=(0,10), ha='center', va='bottom')
    ax.annotate(hs, (x, lo), textcoords='offset points', xytext=(0,-10), ha='center', va='top')
ax.set_ylim(-5, 40)
ax.grid()
#plt.show()
plt.savefig(f'{path}\_{(index+70):02}_pandas_iris_ylim.png')
plt.close('all')
