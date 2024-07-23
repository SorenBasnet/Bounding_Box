# Classification problem 

import numpy as np
from collections import Counter


# euclidean distance global function 

def euclidean_distance(x1, x2): 
    distance = np.sqrt(np.sum((x1-x2)**2))
    return distance 

class KNN: 

    # k value is required to compare the point 
    # point to the nearest k points

    def __init__(self, k=3): 
        self.k = k 

    # keeping the data points

    def fit(self, X, y): 
        self.X_train = X 
        self.y_train = y 
    

    def predict(self, X): 
        predictions = [self.__predict(x) for x in X] 
        return predictions 
    
    # helper function 
    # _function indicates that function is intended for 
    # internal use and should not be called directly by users
    def __predict(self, x):
        
        # compute the distance with the given data set and all the other data
        # set found in fit 

        distances = [euclidean_distance(x, x_train) for x_train in self.X_train] 

        # get the closest k 
        # argsort tells us the original indices from the distance
        k_indices = np.argsort(distances)[:self.k] 
        k_nearest_labels = [self.y_train[i] for i in k_indices] 
        
        # majority vote 
        most_common = Counter(k_nearest_labels).most_common() 
        return most_common[0][0] 



