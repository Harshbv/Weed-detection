import tensorflow as tf

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0

model = tf.keras.Sequential(
  [
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(10)
  ]
)

model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)

predictions = model.predict(test_images)




#Code to detect weeds

import cv2
import numpy as np
import urllib.request

flag=False
url='https://www.agric.wa.gov.au/sites/gateway/files/styles/page_featured_image/public/Weeds%20in%20paddocks%20August%202017.JPG?itok=uahM6mgT.jpg'
urllib.request.urlretrieve(url,'image.jpg')
img = cv2.imread('image.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)
kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(edges, kernel, iterations=1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    area = cv2.contourArea(contour)
    if area < 1000:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        weedSize = 10;
        weedAge = 2;
        weedHealth = 50;

        if weedSize < 12 and weedAge < 4:
            weedHealth -= 30;

        if weedSize > 12 and weedSize < 24 and weedHealth > 50:
            weedHealth -= 50;

        if weedSize > 24 and weedAge > 8:
            weedHealth -= 80;


            # Code to check if weed is alive or dead and kill if it is alive.
        
        if weedHealth <= 0:
            print("The weed is dead!")
            flag=True
        else:
            print("The weed is still alive.")
            flag=False
        if flag==False:
            print("Kill the weed.") 

     
cv2.imshow('Detected Weeds and Pests', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

