import numpy as np

class LinearRegression(object):
    def __init__(self):
        pass

    def initialize_weights(self, dim, std_dev=1e-2):
        """
        Initialize the weights of the model. The weights are initialized
        to small random values. Weights are stored in the variable dictionary
        named self.params.

        W: weight vector; has shape (D, 1)
        
        Inputs:
        - dim: (int) The dimension D of the input data.
        - std_dev: (float) Controls the standard deviation of the random values.
        """
        self.params = {}
        #############################################################################
        # TODO: Initialize the weight vector to random values with                  #
        # standard deviation determined by the parameter std_dev.                   #
        # Hint: Look up the function numpy.random.randn                             #
        #############################################################################
        self.params['W'] = np.random.randn(dim, 1) * std_dev
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################        
        
        
    def train(self, X, y, analytic_solution=False, learning_rate=1e-3, num_iters=100,
            batch_size=200, verbose=False):
        """
        Train Linear Regression using stochastic gradient descent.

        Inputs:
        - X: A numpy array of shape (N, D) containing training data; there are N
          training samples each of dimension D.
        - y: A numpy array of shape (N, 1) containing the ground truth values.
        - analytic_solution: (boolean) flag to toggle between analytical and iterative solutions.
        - learning_rate: (float) learning rate for optimization.
        - reg: (float) regularization strength.
        - num_iters: (integer) number of steps to take when optimizing
        - batch_size: (integer) number of training examples to use at each step.
        - verbose: (boolean) If true, print progress during optimization.
        
        Outputs:
        If analytic_solution is set to True this function returns None.
        Otherwise,
        return a list containing the value of the loss function at each training iteration.
        """
        X = self.feature_transform(X)
        num_train, dim = X.shape

        if analytic_solution:
            self.params = {}
            
            #############################################################################
            # TODO: Implement the analytical solution of the weight vector for linear   #
            # regression.                                                               #
            #############################################################################
            
            self.params['W'] = np.dot(np.linalg.inv(np.dot(np.transpose(X), X)), np.dot(np.transpose(X), y))
            #############################################################################
            #                              END OF YOUR CODE                             #
            #############################################################################

            return self.params['W']


        # Implement the initiaize_weights function.
        self.initialize_weights(dim)

        loss_history = []
        for it in range(num_iters):

            #########################################################################
            # TODO: Create a random minibatch of training data and labels, storing  #
            # them in X_batch and y_batch respectively.                             #
            # Hint: Look up the function numpy.random.choice                        #
            #########################################################################
            indices = np.random.choice(num_train, batch_size, replace=False)
            X_batch = X[indices]
            y_batch = y[indices]
            #########################################################################
            #                             END OF YOUR CODE                          #
            #########################################################################
            
            loss, grads = self.loss(X_batch, y=y_batch)
            loss_history.append(np.squeeze(loss))

            #########################################################################
            # TODO: Use the gradients in the grads dictionary to update the         #
            # parameters of the model (stored in the dictionary self.params)        #
            # using stochastic gradient descent. You'll need to use the gradients   #
            # stored in the grads dictionary defined above.                         #
            #########################################################################
            self.params['W'] = self.params['W'] - learning_rate * grads['W']
            #########################################################################
            #                             END OF YOUR CODE                          #
            #########################################################################
            if verbose and it % 100 == 0:
                print('iteration %d / %d: loss %f' % (it, num_iters, loss))

        return loss_history

    def loss(self, X, y=None):
        """
        Compute the loss and gradients for an iteration of linear regression.

        Inputs:
        - X: Input data of shape (N, D). Each X[i] is a training sample.
        - y: Vector of training labels. y[i] is the ground truth value for X[i].

        Returns:
        Return a tuple of:
        - loss: Loss for this batch of training samples.
        - grads: Dictionary mapping parameter names to gradients of those parameters
          with respect to the loss function; has the same keys as self.params.
        """
        
        # Unpack variables from the params dictionary
        W = self.params['W']
        N, D = X.shape

        #############################################################################
        # TODO: Compute for the prediction value given the current weight vector.   #
        # Store the result in the prediction variable                               #
        #############################################################################
        prediction = np.dot(X, W)
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################
        
        #############################################################################
        # TODO: Compute for the loss.                                               #
        #############################################################################
        loss = np.sum((np.square(prediction - y)) / (2 * N))
        
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################

        grads = {}
        #############################################################################
        # TODO: Compute the derivatives of the weights. Store the                   #
        # results in the grads dictionary. For example, grads['W'] should store     #
        # the gradient on W, and be a matrix of same size.                          #
        #############################################################################
        
        
        grads['W'] = (np.dot(np.transpose(X), prediction - y)) / N
        
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################

        return loss, grads
    
    def predict(self, X):
        """
        Predict values for test data using linear regression.

        Inputs:
        - X: A numpy array of shape (num_test, D) containing test data consisting
             of num_test samples each of dimension D.

        Returns:
        - y: A numpy array of shape (num_test, 1) containing predicted values for the
          test data, where y[i] is the predicted value for the test point X[i].  
        """

        W = self.params['W']
        X = self.feature_transform(X)
        #############################################################################
        # TODO: Compute for the predictions of the model on new data using the      #
        # learned weight vectors.                                                   #
        #############################################################################
    
        prediction = np.dot(X, W)
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################
    
        return prediction

    def feature_transform(self,X):
        """
        Appends a vector of ones for the bias term.

        Inputs:
        - X: A numpy array of shape (N, D) consisting
             of N samples each of dimension D.

        Returns:
        - f_transform: A numpy array of shape (N, D + 1)
        """

        #############################################################################
        # TODO: Append a vector of ones across the dimension of your input data.    #
        # This accounts for the bias or the constant in your hypothesis function.   #
        #############################################################################
        f_transform = np.append(X, np.ones((X.shape[0],1)), axis=1)
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################
        
        return f_transform
  
    
