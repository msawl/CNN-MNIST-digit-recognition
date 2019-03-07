import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
import pickle 


#import the minst dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data() 


# Reshaping the array to 4-dims so that it can work with the Keras API

x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

# Making sure that the values are float so that we can get decimal points after division

x_test = x_test.astype('float32')
# Normalizing the RGB codes by dividing it to the max RGB value.

x_test /= 255
print('x_train shape:', x_train.shape)
print('Number of images in x_test', x_test.shape[0])




filename = 'finalized_model_fun.sav'
loaded_model = pickle.load(open(filename, 'rb'))
image_index = 124   #insert any number you want from 1 to 10000
plt.imshow(x_test[image_index].reshape(28, 28),cmap='Greys')
pred = loaded_model.predict(x_test[image_index].reshape(1, 28,28, 1))

print(pred.argmax())
plt.show()