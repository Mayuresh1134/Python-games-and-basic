import pyautogui
from PIL import Image, ImageGrab
import time
# from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)
    return


# def draw():


# def takeScreenshot():
#     return image

def iscollide(data):
    #rectangle for birds
    for i in range(250,300):
        for j in range(410,593):
            if data[i,j] < 50:
                hit("down")
                return 


    for i in range(275,325):
        for j in range(593,650):
            if data[i,j] < 100:
                hit("up")
                return 
    return 

if __name__ == "__main__":
    print("DINO game about to start in 3 seconds")
    time.sleep(3)
    hit("up")
    while(True):
        image= ImageGrab.grab().convert('L')
        data= image.load()
        iscollide(data)

        
        # Draw
        # print(asarray(image))
        
        # #rectangle for cactus
        # for i in range(275,325):
        #     for j in range(593,650):
        #         data[i,j]=0

        # #rectangle for birds
        # for i in range(250,300):
        #     for j in range(410,593):
        #         data[i,j]=171
                
        # image.show()
        # break
        