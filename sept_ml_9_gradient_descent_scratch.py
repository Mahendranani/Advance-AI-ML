x = 10
learning_rate = 0.1
for i in range(10):
    grad = 2*x
    x -= learning_rate * grad
print(x)