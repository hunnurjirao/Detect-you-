import os
import cv2
from PIL import Image

directory= "..." #enter your dir path here


cap = cv2.VideoCapture(0)

num_images=int(input("Enter no. of images to be taken: "))
i=0

while i<num_images:
        i=i+1
        _, frame = cap.read()
        im = Image.fromarray(frame, 'RGB')
        im = im.resize((128,128))
        im.save(os.path.join(directory, str(i)+".jpg"), "JPEG")

        cv2.imshow("Capturing", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()