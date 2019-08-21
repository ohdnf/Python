#keras05_predict.py

# 1. Data
import numpy as np
np.random.seed(0)

# Training Data
x_train = np.array([1,2,3,4,5,6,7,8,9,10])
x_test = np.array([11,12,13,14,15,16,17,18,19,20])
# Test Data
y_train = np.array([1,2,3,4,5,6,7,8,9,10])
y_test = np.array([11,12,13,14,15,16,17,18,19,20])
z1 = np.array([101,102,103,104,105])
# z2 = np.array([range(30,50)])
z2 = np.array(range(30,50))

# 2. Model
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(5, input_dim=1, activation='relu'))
model.add(Dense(2))
model.add(Dense(1))

# 3. Train(Compile)
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=100, batch_size=1)

# 4. Evaluate / Predict
loss, acc = model.evaluate(x_test, y_test, batch_size=1)
print("acc: ", acc)
print("loss: ", loss)

# y_predict = model.predict(x_test)
y_predict = model.predict(z2)
print(y_predict)
