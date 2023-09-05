'''Implementation of Gradient descendent algorithm to solve multilineal regression problems'''
import numpy as np

class MultilinearRegression():
    def __init__(self):
        pass

    def predict(self, X, w = None, b = None):
        '''
        Predicts the value of the Y variable of shape (N,1) given the array of w parameters (slopes) of shape (M,1), a single parameter b (intercept) and a 
        N-dimentional X array of shape (N,M)
        '''
        if w is None:
            w = self.W
        if b is None:
            b = self.b

        return b + np.dot(X,w)

    def loss_function(self, X, Y, w = None, b = None):
        '''
        Same as cost function, receives X and Y arrays as arguments and returns the cost function value. X and Y must have the same number of rows
        '''
        # loss_function has to be able to deal with w and b specific values when it is needed, in order to use it in 
        # forward and backward values in self.grad(). So, when w and b are not passed, the function uses the current value in the model
        if w is None:
            w = self.W
        if b is None:
            b = self.b

        N = len(Y)
        diff = self.predict(X, w, b) - Y

        return np.sum(diff**2)/N # chi squared
    
    def grad(self, X, Y, w, b, Dw = 1e-8, Db = 1e-8):
        '''
        Implementation of numerical gradient (central derivative). Delta values for w and b can be passed as arguments to
        the function, default values are 1e-8 in both cases.
        '''

        #forward (F) and backward (B) values are computed as auxiliar values
        Fw = self.loss_function(X, Y, w + Dw, b)
        Bw = self.loss_function(X, Y, w - Dw, b)
        Fb = self.loss_function(X, Y, w, b + Db)
        Bb = self.loss_function(X, Y, w, b - Db)

        grad_w = (Fw - Bw)/(2 * Dw)
        grad_b = (Fb - Bb)/(2 * Db)

        return grad_w, grad_b
    
    def score(self, X, Y):
        '''Computes the R^2 value given a sample'''
        N = len(Y)
        Y_mean = (1/N) * np.sum(Y)

        num = np.sum((self.predict(X) - Y)**2)
        den = np.sum((Y - Y_mean)**2)

        return 1 - num/den

    def optimizer(self, X, Y, w, b, tol, max_epoch, alpha, beta):
        '''
        Returns the optimized values of w and b, and the numbers of epochs reached. tol, max_epoch, alpha and beta parameters can be passed as arguments
        '''
        epsilon = 1
        epoch = 0
        while epsilon > tol and epoch < max_epoch:
            w_grad, b_grad = self.grad(X,Y,w,b)
            w = w - alpha*w_grad
            b = b - beta*b_grad

            self.history.append(self.loss_function(X, Y, w, b))

            epsilon = abs(self.history[epoch] - self.history[epoch + 1])
            epoch += 1

        return w, b, epoch

    # def optimizer(self, X, Y, w, b, alpha = 0.001, beta = 0.001):
    #     '''
    #     updates the parameters w and b given the gradient descendent algorithm
    #     '''
    #     w_grad, b_grad = self.grad(X,Y,w,b)
    #     w = w - alpha*w_grad
    #     b = b - beta*b_grad

    #     # w = w - alpha*self.grad(X,Y,w,b)
    #     # b = b - beta*self.grad(X,Y,w,b)

    #     return w, b
    
    def fit(self, X, Y, w0 = None, b0 = None, tol = 1e-13, max_epoch = 500000, alpha = 0.001, beta = 0.001):
        '''
        implementation of method, this method allows to pass custom initial guess of the parameters w and b
        as w0 and b0 (default value: None)
        '''

        self.n = X.shape[0] #number of samples
        self.m = X.shape[1] #number of features
        
        #load initial parameters
        if w0 is None and b0 is None:
            np.random.seed(413)
            self.W = np.random.rand(self.m,1)
            self.b = np.random.rand()

        else:
            self.W = w0
            self.b = b0

        self.history = []
        # epoch = 0
        # epsilon = 1 # will be used as variation between two consecutive values of self.loss_function() for two epochs
        # max = 500000 # max number of epochs
        # tol = 1e-13

        self.history.append(self.loss_function(X, Y, self.W, self.b)) # initial cost
        print('Initial cost :', self.history[0])

        # while epsilon > tol and epoch < max:
            
        #     self.W, self.b = self.optimizer(X, Y, self.W, self.b)
        #     self.history.append(self.loss_function(X, Y, self.W, self.b))
        #     epsilon = abs(self.history[epoch] - self.history[epoch + 1])
        #     epoch += 1

        #     if epoch == max:
        #         print(f'The model did not converge after {max} iterations. Note that it is possible that the model did not converge because of the initial guess, try passing w0 and b0 as parameters to self.fit() method')

        self.W, self.b, epoch = self.optimizer(X, Y, self.W, self.b, tol, max_epoch, alpha, beta)

        print('Final cost :', self.history[-1])
        print('Number of epochs :', epoch)

        return # breaks