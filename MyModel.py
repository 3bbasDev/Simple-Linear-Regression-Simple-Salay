import math as mt
import pandas as pd
from sklearn.model_selection import train_test_split



# def GetTotalXY(x,y):
#     if len(x) == 0:
#         return 0
#     else:
#         return  (x[0] * y[0]) + GetTotalXY(x[1:],y[1:])

# def getSum(x):
#     if len(x) == 0:
#         return 0
#     else:
#         return x[0] + getSum(x[1:])

# def getSum1(x,y):
#     if len(x) == 0:
#         return 0
#     else:
#         return x[0] + getSum(x[1:]), y[0] + getSum(y[1:])

# def getinfo1(x, y):
#     return getSum1(x,y)
# def getinfo(x, y):
#     return getSum(x), getSum(y),GetTotalXY(x, y)



# import Dataset from csv
dataset = pd.read_csv('Salary_Data.csv')
x1 = dataset.iloc[:, :-1].values
y1 = dataset.iloc[:, -1].values

[x, X_test, y, Y_test] = train_test_split(x1, y1, test_size=0.2, random_state=0)



n = len(x)
ex = 0  # ∑x
ey = 0  # ∑y
exy = 0  # ∑xy
exp2 = 0  # ∑x^2

for i, j in zip(x, y):
    exy += i * j
    exp2 += mt.pow(i, 2)
    ex += i
    ey += j
nexy = n * exy[0]  # n∑xy
nexp2 = n * exp2  # n∑x^2
exp22 = mt.pow(ex, 2)  # (∑x)^2
# print('∑x = ', ex)
# print('∑y = ', ey)
# print('∑xy = ', exy[0])
# print('n∑xy = ', nexy)
# print('n∑x^2 = ', nexp2)
# print('(∑x)^2 = ', exp22)

b = (nexy - (ex * ey)) / (nexp2 - exp22)
print('b = ', b)

a = (ey-(b*ex)) / n
print('a = ', a)
