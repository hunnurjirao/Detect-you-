# Detect-you-
 A simple Convolution Neural Network using Keras deep learning library to detect “you” whenever you are in front of your laptop.
 
 **capturing_images.py** : This is used to create our own dataset of our images for our model.
 
 **run model.py** : Here comes the actual CNN model and it also saves the model as *model.h5* file.
 
 **detect_me(open_cv).py** : Here I used OpenCV to get access of our web-cam and test our model.
 
### My environment details:

> Windows 10

> Python 3.5.6


### Python packages:

> Open CV (opencv-python)

> PIL (Pillow)

> keras (I used the one with tensorflow backend)

> numpy

### How to run the model:
1) Take some images(4000 images) with you present infront of webcam(2000 images) and without you(2000 images) infront of webcam by runnig the capturing_images.py file and store the both files in Train dir.

2) Similarly, take some images(1600 images) with you(800 images) and without you(800 images) infront of webcam by runnig the capturing_images.py file and store the both files in Validation dir.

3) Now make sure that both Train and Validation files are in one Directory.

4) Then run the run model.py file and save the model.

5) Finally, to see your outpyt running the detect_me(open_cv).py file.

### CNN Model Architecture:
![](Images/detect_you.png)
