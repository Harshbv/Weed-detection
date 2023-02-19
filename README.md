# Weed-detection
 Basic idea behind this project is that instead of spraying pesticides/weedicides on all the food plants we can use it particularly on insects and plants. 
Objective:
This project develops a technique by which we can accurately concentrate on target weeds/insects instead of spraying on all the healthy plants.
By following the technique developed in this project we not only minimalize the use of pesticides but also decrease the exposure of the plants to unhealthy chemicals.
Working of the drone:
Drones used to  1) Capture the picture of the farm land
                2)  To relocate the spot where we have found the weed.
                3) Takes action based on the weed/insect found.
 Mobile software:
 -> A mobile game app is to be developed where in the user can spot the weed present in the field with the help of the drone connected to the mobile through WIFI.
-> Using the app the user controls the drone.
-> If they spot a weed , the already attached tool in the drone will pluck the weed then and there.
-> If they spot insects, the piston attached to the drone which contains insecticide is shot on the insect directly thereby killing it.
-> In this way we can ensure that the healthy plants are not exposed to the chemicals.

Weed killing code:
Output shows whether the weed is dead or alive.
It also guides the user with the corresponding action.
ie.,
Weed is killed if it is alive
Else it moves to the next target.

Weed Detection code:
The code to detect weeds present in the agricultural land. 
Here we have used 3 Python libraries here namely, opencv, numpy and urllib.
Firstly, i will download an image of the agricultural land from the specified url and convert that into grayscale.
Then Guassian blur is applied to reduce noise in the image and make it smoother. Next we detect edges in the image and fill the gaps to smooth out the boundaries and find contours. If the contour area is less than 1000 then it is likely to be a weed and so i draw a boundary around that. 
Then we analyze the size of the weed,it's age and health using deep learning and accordingly we determine if it is alive or dead. If it is alive then we instruct the drone to kill it, else leave it.
The area surrounded by the red coloured rectangle depicts the presence of weeds in the land.

Deep Learning code:
Automatic identification and classification of weeds can play a vital role in weed management contributing to better crop yields.
Firstly, image acquisition is done and the collected images are grouped into weed and crop categories. And then,
Several common deep-learning detection models are applied for weed identification model training
The models were trained with different values of epochs, batch sizes, and hyperparameters were tuned to get optimal performance.
In traditional machine learning methods, the color, texture, and other characteristics of weed images should be extracted with complex hand-crafting. So, similar weed species could not be distinguished if the weed image extraction was incomplete or if there were occluded features. But this can be handled by deep learning models which work as a human brain. Using artificial intelligence different variety of weeds can be identified by comparing them with the charachteristics of weeds that the model has already learned during the training phase. Thus, the identification accuracy would be significantly improved.

Working:
Planned to develop an android gaming app in which a drone is controlled manually. The drone is flown over farming lands to capture images and detect weeds and pests if present in the fields.
