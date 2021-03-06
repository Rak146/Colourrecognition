#importing the necessary libraries
import cv2
import pandas as pd
from tkinter import *
from PIL import ImageTk,Image,ImageEnhance
from tkinter import filedialog
from matplotlib.pyplot import text, title
import mult
mult.open()
img_path = mult.h

img = cv2.imread(img_path)


clicked = False
r = g = b = x_pos = y_pos = 0


index = ["color", "color_name", "hex", "R", "G", "B"]
#read the dataset using pandas
csv = pd.read_csv('C:/Users/raksr/Downloads/colors.csv', names=index, header=None)


#according to csv file the colour are extracted for particular mouse pointer in image window
def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


#the mouse event is call through the function
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('image') #cv2.WINDOW_NORMAL
cv2.setMouseCallback('image', draw_function)

while True:

    #take the width and height for image size
    up_width = 1500
    up_height = 800
    up_points = (up_width, up_height)
    img = cv2.resize(img, up_points, interpolation= cv2.INTER_LINEAR)
    cv2.imshow('image', img)
    
    if clicked:

        
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        #Creating text string to display(Color name and RGB values)
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    #Break the loop when the user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
