#importing libraries
import cv2
import numpy as np
import tensorflow as tf


def get_class_arg(array):
    return np.argmax(array)

def get_class(argument):
    if argument==0:
        return "flap"
    elif argument==1:
        return "none"
    else:
        return "quit"

#loading the trained model
model = tf.keras.models.load_model('saved_model/model_t')


#video capture and model prediction
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)
cv2.namedWindow("ChidiyaUdd!")

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # rectangle for user to play
    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)


    # extract the region of image within the user rectangle
    roi = frame[100:500, 100:500]
    img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img=img/255.0 #normalizing pixel values between 0 and 1

    # predict the move made
    pred = model.predict(np.array([img]))
    move=get_class(get_class_arg(pred))
    
    
    #adding text information
    font = cv2.FONT_HERSHEY_SIMPLEX
    # org
    org = (50, 50)
    # fontScale
    fontScale = 0.8
    # Blue color in BGR
    color = (255, 0, 0)
    # Line thickness of 2 px
    thickness = 2
    # Using cv2.putText() method
    frame = cv2.putText(frame,move, org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
    
    cv2.imshow("ChidiyaUdd!", frame)
    
    k = cv2.waitKey(1) #waitKey(1) will display a frame for 1 ms, after which display will be automatically closed
    if k%256 == 27: #escape key for quitting 
        # ESC pressed
        break

cap.release()
cv2.destroyAllWindows()
