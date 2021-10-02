import cv2
import numpy as np
import time
from collections import deque



def draw_calc(frame,calc_postion):
    x,y,w,h,a,b=calc_postion
    #To draw calc on frame
    # DRAW HORIZONTAL LINES OF CALC
    color = (255, 0, 0)
    cv2.line(frame, (x, y), (x, y + h * 8), color, 2)
    cv2.line(frame, (x + w, y + h * 2), (x + w, y + h * 7), color, 2)
    cv2.line(frame, (x + w * 2, y + h * 2), (x + w * 2, y + h * 8), color, 2)
    cv2.line(frame, (x + w * 3, y + h * 2), (x + w * 3, y + h * 8), color, 2)
    cv2.line(frame, (x + w * 4, y), (x + w * 4, y + h * 8), color, 2)

    # DRAW VERTICLE LINES OF CALC
    cv2.line(frame, (x, y), (x + w * 4, y), color, 2)
    cv2.line(frame, (x, y + h * 2), (x + w * 4, y + h * 2), color, 2)
    cv2.line(frame, (x, y + h * 3), (x + w * 4, y + h * 3), color, 2)
    cv2.line(frame, (x, y + h * 4), (x + w * 4, y + h * 4), color, 2)
    cv2.line(frame, (x, y + h * 5), (x + w * 3, y + h * 5), color, 2)
    cv2.line(frame, (x, y + h * 6), (x + w * 4, y + h * 6), color, 2)
    cv2.line(frame, (x, y + h * 7), (x + w * 3, y + h * 7), color, 2)
    cv2.line(frame, (x, y + h * 8), (x + w * 4, y + h * 8), color, 2)

    # PUT TEXT IN EVERY CELL
    cv2.putText(frame, "C", (x + a, y + 3 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "^", (x + w + a, y + 3 * h + b - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "<-", (x + 2 * w + a - 6, y + 3 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, "OFF", (x + 3 * w + a - 6, y + 3 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    cv2.putText(frame, "%", (x + 0 * w + a, y + 4 * h + b - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, "%", (x + 0 * w + a, y + 4 * h + b - 3), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, "/", (x + 1 * w + a, y + 4 * h + b - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    cv2.putText(frame, "*", (x + 2 * w + a, y + 4 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "-", (x + 3 * w + a, y + 4 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "7", (x + 0 * w + a, y + 5 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "8", (x + 1 * w + a, y + 5 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "9", (x + 2 * w + a, y + 5 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "4", (x + 0 * w + a, y + 6 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "5", (x + 1 * w + a, y + 6 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "6", (x + 2 * w + a, y + 6 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "1", (x + 0 * w + a, y + 7 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "2", (x + 1 * w + a, y + 7 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "3", (x + 2 * w + a, y + 7 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, " .", (x + 2 * w + a, y + 8 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "0", (x + int(0.5 * w) + a, y + 8 * h + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "+", (x + 3 * w + a, y + int(5.5 * h) + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.putText(frame, "=", (x + 3 * w + a, y + int(7.5 * h) + b), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)

