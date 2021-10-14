# Chidhiya Ud

A Hand Gesture Controlled Version of the Flappy Bird Game.

## Description

The flappy bird game has been developed using the Pygame module, while the neural network to predict gestures has been fined tuned over the pre-trained 
MobileNet offered by Keras. The training was done over 3k images which I collected myself. I chose MobileNet due to its low latency which becomes a 
critical factor while developing games.
There are 3 simple actions to play the game-
1.     Finger Pointing Up- Flap/ Start Game
2.     Closed Fist- Do Nothing
3.     Thumbs Down- Quit Game

## Demo



### Dependencies

* Python 3.8.8
* pygame 2.0.1
* tensorflow 2.6.0
* keras 2.6.0
* opencv-python 4.5.3.56
* numpy 1.20.1

### Executing program

* There are 3 main directories- Game Standard (The standard flappy bird game developed using Pygame), Neural Network (contains all resources
regarding the creation/training/testing of the neural network for hand gesture recognition) and Game (The final game developed which is controlled using hand
gestures).

* After installing all the dependencies, You can collect your own images for the abovementioned gestures by running all the 3 "capture_gesture_images.py" scripts 
in the neural network directory. Since I trained the model on only 3k images over all the classes, it is better that you retrain the model by capturing
images at your own end. Just run the 3 scripts and press "space" to capture images.

* After the collection of images, all the images would be stored in a folder named "images" inside the neural network directory. The next step would be to run 
each and every cell of the "train.ipynb" file. The trained model would automatically be stored.

* You can check the performance of the trained model by running the "test.py" script.

* Now to play the final game, just go to the "Game" directory and run the "main.py" script.
