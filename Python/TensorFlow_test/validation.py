import numpy as np
import random
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#def create_feature_sets_and_labels(test_size = 0.3):

test_size = 0.3

# known patterns (5 features) output of [1] of positions [0,4]==1
features = []
features.append([[0, 0, 0, 0, 0], [0,1]])
features.append([[0, 0, 0, 0, 1], [0,1]])
features.append([[0, 0, 0, 1, 1], [0,1]])
features.append([[0, 0, 1, 1, 1], [0,1]])
features.append([[0, 1, 1, 1, 1], [0,1]])
features.append([[1, 1, 1, 1, 0], [0,1]])
features.append([[1, 1, 1, 0, 0], [0,1]])
features.append([[1, 1, 0, 0, 0], [0,1]])
features.append([[1, 0, 0, 0, 0], [0,1]])
features.append([[1, 0, 0, 1, 0], [0,1]])
features.append([[1, 0, 1, 1, 0], [0,1]])
features.append([[1, 1, 0, 1, 0], [0,1]])
features.append([[0, 1, 0, 1, 1], [0,1]])
features.append([[0, 0, 1, 0, 1], [0,1]])
features.append([[1, 0, 1, 1, 1], [1,0]])
features.append([[1, 1, 0, 1, 1], [1,0]])
features.append([[1, 0, 1, 0, 1], [1,0]])
features.append([[1, 0, 0, 0, 1], [1,0]])
features.append([[1, 1, 0, 0, 1], [1,0]])
features.append([[1, 1, 1, 0, 1], [1,0]])
features.append([[1, 1, 1, 1, 1], [1,0]])
features.append([[1, 0, 0, 1, 1], [1,0]])
#print(features)

# shuffle out features and turn into np.array
random.shuffle(features)
#print(features)

#features = np.array(features)
    
# split a portion of the features into tests
testing_size = int(test_size*len(features))
print(len(features))
print(testing_size)
print(features[0][0])
print(features[0][1])
print(features[1][0])
print(features[1][1])
print(features[:0][:-1])
print(features[1:][:-2])
print(features[0:][:-3])
print(features[:1][:-4])

print(features[:0][-1:])
print(features[:1][-1:])
print(features[:2][-2:])
print(features[:3][-3:])
print(features[:4][-4:])
print(features[:5][-5:])
print(features[:6][-6:])
#print(features[:,0][:-testing_size])

# create train and test lists
#train_x = list(features[:,0][:-testing_size])
#train_y = list(features[:,1][:-testing_size])
#test_x = list(features[:,0][-testing_size:])
#test_y = list(features[:,1][-testing_size:])

#print(train_x)
#print(train_y)
#print(test_x)
#print(test_y)

##    return train_x, train_y, test_x, test_y
