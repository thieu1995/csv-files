# MNIST

**Training Sample** : 60000

**Evaluation Sample** : 10000

**Coded using Keras with Theano backend**.

**Accuracy : 99%**

**Saved Model in mnistmodel.h5 file**

**File** : cnn-mnist.py

* Loaded Dataset from Keras Datasets
* Reshaped the training and test sets as 28x28 
* Normalized inputs to range 0 - 1
* Enocoded output sets (y_train and y_test)
* **Defined cnn model with two Conv2D layers of 5x5 and 3x3, MaxPooling2D layer of 2,2 with 0.2 Dropout**
  **Flattened and passed to the Dense layers 128->50->10**
* Compiled with categorical_crossentropy loss and adam optimizer
* Fitted training set validating on the test set for 20epochs
* Evaluated the model to find the accuracy -  **Accuracy of 99% was obtained**
* Saved the model to disk for future use
* Loaded the model from disk
* Loaded the image to make prediction on and appplied reshaping and normalization
* Predictions were made and displayed

**File** : mnist-from-disk.py

* **Load the saved model**
* Load the image
* Apply normalization and reshaping
* **Make prediction**
* Display the prediction
