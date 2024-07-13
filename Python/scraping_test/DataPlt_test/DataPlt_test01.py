import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("test 0010 ----------------------------------------------------------------------------")

sns.set_style('whitegrid')
 # カリフォルニア住宅価格のデータセット
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['Price'] = housing.target
df.head()

print("test 0020 ----------------------------------------------------------------------------")

df.info()
df.describe()
#df.hist(bins=30, figsize=(15, 13))
#plt.show()
df.corr()

print("test 0030 ----------------------------------------------------------------------------")

df = df[df['HouseAge'] < df['HouseAge'].max()]
df = df[df['Price'] < df['Price'].max()]
df.info()
#df.hist(bins=30, figsize=(15, 13))
#plt.show()

print("test 0040 ----------------------------------------------------------------------------")

# 説明変数
X = df.drop(['Price'], axis=1)
# 目的変数
y = df['Price']

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
#標準化
X = scaler.fit_transform(X)

print("test 0050 ----------------------------------------------------------------------------")

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
print(X_train.shape, X_test.shape)

print("test 0060 ----------------------------------------------------------------------------")

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print(model.intercept_)
print(model.coef_)

print("test 0070 ----------------------------------------------------------------------------")

X_some = X_train[:4]
y_some = y_train[:4]
print(f'予測結果{np.round(model.predict(X_some), 3)}')
print(f'正解ラベル{list(y_some)}')

print("test 0080 ----------------------------------------------------------------------------")

model_pred = model.predict(X_train)
err_sum = ((y_train - model_pred) ** 2).sum()
mse = err_sum / len(y_train)
rmse = np.sqrt(mse)

print(f'誤差の合計:{err_sum}')
print(f'誤差の平均値(MSE):{mse}')
print(f'RMSE:{rmse}')

print("test 0090 ----------------------------------------------------------------------------")

from sklearn.metrics import mean_squared_error

model_train_pred = model.predict(X_train)
model_train_mse = mean_squared_error(y_train, model_train_pred)
model_train_rmse = np.sqrt(model_train_mse)

print(f'誤差の平均値(MSE):{model_train_mse}')
print(f'RMSE:{model_train_rmse}')

print("test 0100 ----------------------------------------------------------------------------")

model_test_pred = model.predict(X_test)
model_test_mse = mean_squared_error(y_test, model_test_pred)
model_test_rmse = np.sqrt(model_test_mse)

print(f'誤差の平均値(MSE):{model_test_mse}')
print(f'RMSE:{model_test_rmse}')

print("test 0110 ----------------------------------------------------------------------------")

plt.figure(figsize=(5,5))
plt.xlim(-1, 6)
plt.ylim(-1, 6)
plt.plot(model.predict(X_test), y_test, 'o')
plt.title('RMSE: {:.3f}'.format(model_test_rmse))
plt.xlabel('Predict')
plt.ylabel('Actual')
#plt.show()

print("test 0120 ----------------------------------------------------------------------------")

from sklearn.datasets import load_diabetes
data_diabetes = load_diabetes()

print("test 0130 ----------------------------------------------------------------------------")

plt.show()








