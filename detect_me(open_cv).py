import cv2
import numpy as np
from PIL import Image
from keras import models

model = models.load_model('present or missing\present or missing model.h5')
name=input("Enter your name: ")

video = cv2.VideoCapture(0)

while True:
        _, frame = video.read()

        im = Image.fromarray(frame, 'RGB')

        im = im.resize((128,128))
        img_array = np.array(im)

        img_array = np.expand_dims(img_array, axis=0)

        prediction = int(model.predict(img_array)[0][0])

        if prediction < 0.5:
            f_name= "Hi " + name +"...!!!"
            cv2.putText(frame,f_name,(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(150,0,255),5)
        else:
            f_name= name + " is Missing...!!!"
            cv2.putText(frame,f_name,(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(150,0,255),5)


        cv2.imshow("Capturing", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
                break
video.release()
cv2.destroyAllWindows()