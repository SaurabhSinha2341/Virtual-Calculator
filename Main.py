import numpy as np
import cv2
import time
from collections import deque
import draw_calc

#The kernel to be used for dilation purpose 
kernel = np.ones((5,5),np.uint8)

# READ X,Y,H,W VALUES FOR CALC
values = np.loadtxt('data/values.txt', int)
x = values[0]
y = values[1]
h = values[2]
w = values[3]
a, b = 6,-3

#default called trackbar function 
def setValues(x):
   print("")


# Creating the trackbars needed for adjusting the marker colour
cv2.namedWindow("Color detectors")
cv2.createTrackbar("Upper Hue", "Color detectors", 153, 180,setValues)
cv2.createTrackbar("Upper Saturation", "Color detectors", 255, 255,setValues)
cv2.createTrackbar("Upper Value", "Color detectors", 255, 255,setValues)
cv2.createTrackbar("Lower Hue", "Color detectors", 64, 180,setValues)
cv2.createTrackbar("Lower Saturation", "Color detectors", 72, 255,setValues)
cv2.createTrackbar("Lower Value", "Color detectors", 49, 255,setValues)



# Loading the default webcam of PC.
cap = cv2.VideoCapture(0)

last_number=""
current_number=""
symbol=""
ans=0


while True:
    # Reading the frame from the camera
    ret, frame = cap.read()
    #Flipping the frame to see same side of yours
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (800, 600))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    u_hue = cv2.getTrackbarPos("Upper Hue", "Color detectors")
    u_saturation = cv2.getTrackbarPos("Upper Saturation", "Color detectors")
    u_value = cv2.getTrackbarPos("Upper Value", "Color detectors")
    l_hue = cv2.getTrackbarPos("Lower Hue", "Color detectors")
    l_saturation = cv2.getTrackbarPos("Lower Saturation", "Color detectors")
    l_value = cv2.getTrackbarPos("Lower Value", "Color detectors")
    Upper_hsv = np.array([u_hue,u_saturation,u_value])
    Lower_hsv = np.array([l_hue,l_saturation,l_value])
    

    # Identifying the pointer by making its mask
    Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
    Mask = cv2.erode(Mask, kernel, iterations=1)
    Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
    Mask = cv2.dilate(Mask, kernel, iterations=1)

    # Find contours for the pointer after idetifying it
    cnts,_ = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    center = None
    # If the contours are formed
    if len(cnts) > 0:
        # sorting the contours to find biggest 
        cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
        # Get the radius of the enclosing circle around the found contour
        ((xc, yc), radius) = cv2.minEnclosingCircle(cnt)
        # Draw the circle around the contour
        cv2.circle(frame, (int(xc), int(yc)), int(radius), (0, 255, 255), 2)
        # Calculating the center of the detected contour
        M = cv2.moments(cnt)
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

    #draw calculator
    draw_calc.draw_calc(frame,[x,y,w,h,a,b])

    #Do calculations, based on the center point of contour
    
    if len(cnts)==0:
        last_number=""
    if len(cnts) > 0:
        if x<=center[0]<=x+a+20 and y<=center[1]<=y + 3 * h + b:
            if last_number!="c":
                print("c")                
                last_number="c"
                current_number=current_number[:-1]
                
            
        elif x+w<=center[0]<=x + w + a+20 and y<=center[1]<=y + 3 * h + b:
            if last_number!="^":
                print("^")
                last_number="^"
                current_number+="^"
                symbol+="^"
            
        elif x + 2 * w<=center[0]<=x + 2 * w + a - 6+20 and y<=center[1]<=y + 3 * h + b:
            if last_number!="//":
                print("//")
                last_number="//"
                current_number+="//"
                symbol+="//"

        elif x + 3 * w<=center[0]<=x + 3 * w + a - 6+20 and y<=center[1]<=y + 3 * h + b:
            if last_number!="Off":
                print("Off")
                last_number="Off"
                current_number=""
                symbol=""
                ans=""

        elif x <=center[0]<=x +a+20 and y+h<=center[1]<=y + 4 * h + b - 5:
            if last_number!="%":
                print("%")
                last_number="%"
                current_number+="%"
                symbol+="%"
                
        elif x + w <=center[0]<=x + 1 * w + a+20 and y+h<=center[1]<=y + 4 * h + b - 5:
            if last_number!="/":
                print("/")
                last_number="/"
                current_number+="/"
                symbol+="/"

        elif x +2 * w <=center[0]<=x + 2 * w + a+20 and y+h<=center[1]<=y + 4 * h + b:
            if last_number!="*":
                print("*")
                last_number="*"
                current_number+="*"
                symbol+="*"
            
        elif x + 3 * w<=center[0]<=x + 3 * w + a+20 and y+h<=center[1]<=y + 4 * h + b:
            if last_number!="-":
                print("-")
                last_number="-"
                current_number+="-"
                symbol+="-"
            
        elif x <=center[0]<=x+ a+20 and y+2*h<=center[1]<=y + 5 * h + b:
            if last_number!="7":
                print("7")
                last_number="7"
                current_number+="7"

        elif x + w<=center[0]<=x + 1 * w + a+20 and y+2*h<=center[1]<=y + 5 * h + b:
            if last_number!="8":
                print("8")
                last_number="8"
                current_number+="8"

            
        elif x + 2 * w<=center[0]<=x + 2 * w + a+20 and y+2*h<=center[1]<=y + 5 * h + b:
            if last_number!="9":
                print("9")
                last_number="9"
                current_number+="9"
            
        elif x <=center[0]<=x + 0 * w + a+20 and y+3*h<=center[1]<=y + 6 * h + b:
            if last_number!="4":
                print("4")
                last_number="4"
                current_number+="4"
            
        elif x + 1 * w<=center[0]<=x + 1 * w + a+20 and y+3*h<=center[1]<=y + 6 * h + b:
            if last_number!="5":
                print("5")
                last_number="5"
                current_number+="5"

        elif x + 2 * w<=center[0]<=x + 2 * w + a+20 and y+3*h<=center[1]<=y + 6 * h + b:
            if last_number!="6":
                print("6")
                last_number="6"
                current_number+="6"
            
        elif x <=center[0]<=x + 0 * w + a+20 and y+4*h<=center[1]<=y + 7 * h + b:
            if last_number!="1":
                print("1")
                last_number="1"
                current_number+="1"

        elif x + 1 * w<=center[0]<=x + 1 * w + a+20 and y+4*h<=center[1]<=y + 7 * h + b:
            if last_number!="2":
                print("2")
                last_number="2"
                current_number+="2"
            
        elif x + 2 * w<=center[0]<=x + 2 * w + a+20 and y+4*h<=center[1]<=y + 7 * h + b:
            if last_number!="3":
                print("3")
                last_number="3"            
                current_number+="3"

        elif x + 2 * w<=center[0]<=x + 2 * w + a+20 and y+5*h<=center[1]<=y + 8 * h + b:
            if last_number!=".":
                print(".")
                last_number="."
                current_number+="."
            
        elif x + int(0.5 * w)<=center[0]<=x + int(0.5 * w) + a+20 and y+7*h<=center[1]<=y + 8 * h + b:
            if last_number!="0":
                print("0")
                last_number="0"
                current_number+="0"
            
        elif x + 3 * w<=center[0]<=x + 3 * w + a+20 and y+int(4.5 * h)<=center[1]<=y + int(5.5 * h) + b:
            if last_number!="+":
                print("+")
                last_number="+"
                current_number+="+"
                symbol+="+"

            
        elif x + 3 * w<=center[0]<=x + 3 * w + a+20 and y+int(6.5 * h)<=center[1]<=y + int(7.5 * h) + b:
            if last_number!="=":
                if symbol!="" and current_number!="":
                    if len(symbol)>1:
                       symbol=list(symbol)
                       for i in range(0,len(symbol)-1):
                          current_number=current_number.replace(symbol[i],"")
                       symbol=symbol[-1]
                    index=current_number.index(symbol)
                    
                    num1=current_number[:index]
                    num2=current_number[index+1:]
                    if symbol=="+":
                       ans=float(num1)+float(num2)
                    if symbol=="-":
                       ans=float(num1)-float(num2)
                    if symbol=="*":
                       ans=float(num1)*float(num2)
                    if symbol=="/":
                       ans=float(num1)/float(num2)
                    if symbol=="%":
                       ans=float(num1)%float(num2)
                    if symbol=="^":
                       ans=pow(float(num1),float(num2))
                    if symbol=="//":
                       ans=float(num1)//float(num2)
                else:
                   ans=current_number
                   print("code yha phuch gya")
                print(ans)   
                last_number="="
                current_number=""
                symbol=""
    


    # MAKE ANSWER LONG ENOUGH TO DISPLAY ON DISPLAY BOARD
    l = len(current_number)
    if l > 10:
        current_number1 = current_number[l - 9:l]
        current_number1 = "..." + current_number1
    else:
        current_number1 = current_number


    cv2.putText(frame, current_number1, (x + int(w * 0.15), y + int(h * 0.7)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.putText(frame, "="+str(ans), (x + int(w * 0.15), y + int(h * 1.7)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)            
    cv2.imshow("Tracking", frame)
        # If the 'q' key is pressed then stop the application 
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
