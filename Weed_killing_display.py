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
