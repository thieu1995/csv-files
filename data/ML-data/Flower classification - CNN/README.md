# FLOWER CLASSIFFICATION

**DATASET** : FROM TENSORFLOW WEBISTE. 
**URL** : http://download.tensorflow.org/example_images/flower_photos.tgz

**CLASSES** : 5 {Daisy, Dandelion, Rose, Sunflower, Tulips}
**IMAGES** : 2871 {Total}

CODED IN PYTHON WITH KERAS WITH PYCHARM IDE

**BACKEND : THEANO**
**ACCURACY : 72% (10 EPOCHS)**

**FILES**
1. flower-classification-CNN.py
2. CNN-model-from-weight.py
3. flowers-CNN-make-prediction.py
4. CNN-weight-72.h5 ( Best weight obtained 72% accuracy)
5. CNN-saved-model-72.h5 (Best model on best weight)
6. External and images from dataset for prediction

**FILE** : flower-classification-CNN.py
**OUTPUT** : trained CNN model's weight 

* Randomness fixed with seed
* Specified the rows and columns as 32 (to use **32x32** image)
* Color channels as 3 (For **RGB**)
* Loaded the downloaded dataset situated at the home folder after resizing to **32x32**
* Changed the image dimension ordering for the backend
* Declared the labels array with the corresponding flower value ( Daisy - 0, Dandelion - 1, so on)
* One hot encoded labels and stored to dummy_y
* Shuffeled the dataset
* Split the dataset to test and train
* **Defined a CNN with**
  3 Convolution2D layers and 3 MaxPooling2D layers
  Followed by a 128 node nerural net layer
  Last layer with number of classes(5) and softmax activation
* Compiled using adam optimizer
* Defined checkpoints to save the best weight
* Fitted the model with training sets
* Plotted the epochs v/s accuracy graph
* Evaluated the model printing the accuracy
* Loaded external image to test
* Made prediction and displayed it


**FILE** : CNN-model-from-weight.py

* Randomness fixed with seed
* Loaded the saved weight
* Compiled the model
* Saved the model

**FILE** : flowers-CNN-make-prediction.py

* Loaded the saved model
* Loaded the image to make prediction
* Applyed needed image dimension ordering
* Made prediction and displayed the accuracy - 72% - could be improved by increasing the number of pixels


