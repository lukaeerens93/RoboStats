import numpy as np 
import matplotlib.pyplot as plt

def multi_perceptron_predict(x_t, W_t):
    '''
    Multi-class perceptron prediction

    input: 
        x_t: d-dim feature vector
        W_t: the current weight matrix in dim (k X d):

    Output: 
        hat{y}_t: the prediction your perceptron algorithm would make
    '''

    # TODO: implement the prediction procedure
    #hat_y = 0 # replace this line with your implemention
    hat_y = np.argmax( np.dot(W_t, x_t) )


    return hat_y

def multi_perceptron_update(x_t, y_t, W_t):
    '''
    Multi-class perceptron update procedure:
    
    input: 
            x_t: d-dim feature vector
            y_t: label, integer from [0,1,2..,k-2,k-1]
            W_t: the current Weight Matrix in dim (k X d)
    
    Output:
            W_tp1: the updated weighted matrix W_{t+1}.
    '''
   
    # TODO: implement the update rule to compute W_{t+1}
    #W_tp1 = W_t # replace this line with your implementation

    # Expand x_t to have 1 axis
    expanded_x = np.expand_dims(x_t, axis = 1)

    # Expand the difference between prediction and ground truth
    # First step is to find the prediction
    hat_y_t = multi_perceptron_predict(x_t, W_t)

    # Next, verify that u get vector showing which elements
    # of y and y_hat = elements of a 0 -> 9 vector
    verify_y = ( np.array([0,1,2,3,4,5,6,7,8,9]) == y_t)*1
    verify_y_hat = ( np.array([0,1,2,3,4,5,6,7,8,9]) == hat_y_t)*1

    # Now expand the loss
    expanded_y = np.expand_dims( verify_y - verify_y_hat, axis = 0)

    # Now update the weights based on weight update rule:
    W_tp1 = W_t + np.transpose( np.dot(expanded_x, expanded_y) )

    return W_tp1

def online_perceptron(X, Y):
    '''
    This function simulates the online learning procedure.  
    (you do not need to implement anything here)

    input:
        X: N x d, where N is the number of examples, and d is the dimension of the feature.
        Y: N-dim vector.
            --Multi-Class: Y[i] is the label for example X[i]. Y[i] is an integer from [0,1.,..k-2,k-1] (k classes).
            --Binary: Y[i] is 0 or 1. 
    
    output: 
        M: a list: M[t] is the average number of mistakes we make up to and including time step t. Note t starts from zero.  
           you should expect M[t] decays as t increases....
           you should expect M[-1] to be around ~0.2 for the mnist dataset we provided. 

        W: final predictor.
            --Binary: W is a d-dim vector, 
            --Multi-Class: W is a k X d matrix. 
    '''

    d = X.shape[1] # feature dimension
    k = np.unique(Y).shape[0] # num unique labels. k=2: binary; k>2: multi-class
    M = []

    t_mistakes = 0
    # initialization for W
    W = np.zeros((k, d)) if k>2 else np.zeros(d) 

    
    # iterate through examples
    for t in range(X.shape[0]):
        x_t = X[t] # nature reveals x_t
        hat_y_t = multi_perceptron_predict(x_t, W) # we predict
        y_t = Y[t] # nature reveals y_t

        if y_t != hat_y_t: 
            t_mistakes = t_mistakes + 1
        
        W = multi_perceptron_update(x_t, y_t, W) # perceptron update 
        M.append(t_mistakes/(t+1.) ) # record the average number of mistakes

    return M, W

if __name__ == "__main__":
    '''
    Runner for mnist 10-class classification 
    '''
    
    mnist_X_Y = np.load("mnist_feature_label.npz") #load mnist dataset. 
    X = mnist_X_Y["X"]  #X: N x d, where N is the number of examples, and d is the dimension of the feature. 
    Y = mnist_X_Y["Y"]  #Y: N, Y[i] is the label for example X[i]. Y[i] is an integer from [0,1.,..k-2,k-1].
    
    M, W = online_perceptron(X, Y)
    
    fig = plt.gcf()
    plt.plot(M)
    plt.xlabel('time')
    plt.ylabel('average mistakes')
    plt.show()
    # fig.savefig('perceptron.pdf')
