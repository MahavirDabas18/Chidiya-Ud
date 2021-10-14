desc = '''Script to gather data images with a particular label.
The script will collect <num_samples> number of images and store them
in its own directory.
Only the portion of the image within the box displayed
will be captured and stored.
Press 'space' to start/pause the image collecting process.
Press 'q' to quit.
'''


#importing libraries
import cv2
import os

cam = cv2.VideoCapture(0) #defining the opencv video camera object, 0-get the first webcam

#setting height and width of the image capturing window
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)
cv2.namedWindow("flap images")

img_counter = 0
num_samples=1000 #the max number of samples to be captured
path = 'images'
img_class_path = os.path.join(path, "flap")

#creating the image folder
try:
    os.mkdir(path)
except FileExistsError:
    pass

#creating the class folder inside the image folder image folder
os.mkdir(img_class_path)

while True:
    ret, frame = cam.read() #return true/false and the frame
    if not ret: #if the script is not able to grab the frame
        print("failed to grab frame")
        break
    
    #defining a region of interest from where the hand sign will be captured from
    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)
    
    
    
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
    frame = cv2.putText(frame, 'Flap (Finger Up) Images: {}/{}  Space: Capture, Esc: Escape'.format(img_counter,num_samples), org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
    
    cv2.imshow("flap images", frame) #shows the user the whole frame being captured by the cv2 window

    #defining hot keys for actions
    k = cv2.waitKey(1) #waitKey(1) will display a frame for 1 ms, after which display will be automatically closed
    #.waitKey(0) will display the window infinitely until any keypress (it is suitable for image display).
    if k%256 == 27: #escape key for quitting 
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32: #space key for capturing the image
        # SPACE pressed
        roi= frame[100:500, 100:500] #capturing only the region of interest
        img_name = "flap_{}.png".format(img_counter) #defining the image name
        cv2.imwrite(os.path.join(img_class_path , img_name), roi) #saving the roi image in the required path
        print("{} written!".format(img_name))
        img_counter += 1
    
    elif img_counter==num_samples: #desired number of images captured
        break
        

cam.release()

cv2.destroyAllWindows()
