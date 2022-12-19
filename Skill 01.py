#Implementation of Single Layer Perceptron
import numpy as np

class perceptron:

  def __init__(self,r, bias, lr):
    self.w = r
    self.bias = bias
    self.learning_rate = lr

  def get_weights(self):
    return self.w

  def train(self, X,Y, epochs):
    Y_pred = np.zeros(len(y))
    for t in range(epochs):
      for i,x in enumerate(X):
        if (np.dot(X[i], self.w)) + self.bias <= 0:
          Y_pred[i] = 0
        else :
          Y_pred[i] = 1
        self.bias = self.bias + self.learning_rate * (Y[i]-Y_pred[i])
        self.w = self.w + self.learning_rate * X[i] * (Y[i]-Y_pred[i])
        print("error", Y[i]-Y_pred[i] , "bias", self.bias )
    return self.w

  def predcit(self, x_new):
    if (np.dot(x_new, self.w)) + self.bias <= 0:
      return 0
    else :
      return 1

if __name__ == "__main__":

    #Training Inputs
    x = np.array([
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1]
    ])

    #Training Outputs
    y = np.array([0,1,1,1,1,1,1,1])

    r = np.random.rand(3)
    model = perceptron(r,-0.9,0.1)
    print(model.get_weights())

    trained_model = model.train(x,y,20)
    print(model.predcit(x_new = [1,1,0]))
    print(model.get_weights())