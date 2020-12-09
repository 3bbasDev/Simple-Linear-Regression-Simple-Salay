import matplotlib.pyplot as pl
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# import Dataset from csv
dataset = pd.read_csv('Salary_Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values



# splitting dataset to training and test
[X_train, X_test, Y_train, Y_test] = train_test_split(x, y, test_size=0.2, random_state=0)
print(len(Y_train))
# Train simple model by LinearRegression class
regression: object = LinearRegression()
regression.fit(X_train, Y_train)

# Predicting Test result
Y_perdict: object = regression.predict(X_test)

# print predict 1 year experience

print(regression.coef_)
print(regression.intercept_)
# Y = b0 + b1*X
# dependent value DV =  intercept_ + ( coef_ * independent value IV)
# Salary =
print(regression.predict([[12]]))
print( (regression.coef_*12) + regression.intercept_)

# Visualising Training
plot1 = pl.figure(1)
pl.scatter(X_train, Y_train, color='red')
pl.plot(X_train, regression.predict(X_train), color='black')
pl.title('Salary Vs Experience (Training)')
pl.xlabel('Years of Experience')
pl.ylabel('Salary')

# Visualising Test
plot2 = pl.figure(2)
pl.scatter(X_test, Y_test, color='red')
pl.plot(X_train, regression.predict(X_train), color='blue')
pl.title('Salary Vs Experience (Test)')
pl.xlabel('Years of Experience')
pl.ylabel('Salary')
pl.show()


