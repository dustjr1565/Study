import cv2
import numpy as np

class Shape:
    def __init__(self,endX, endY, color, thickness):
        self.endX=endX
        self.endY=endY
        self.color=color
        self.thickness = thickness

    def Draw(self, img):
        cv2.circle(img, (self.endX,self.endY), self.thickness, self.color, -1)

class Line(Shape):
    def __init__(self, startX, startY, endX, endY, color, thickness):
        Shape.__init__(self, endX, endY, color,thickness)
        self.startX = startX
        self.startY = startY

    def Draw(self, img):
        cv2.line(img, (self.startX, self.startY), (self.endX, self.endY), self.color, self.thickness)

class Rect(Shape):
    def __init__(self, startX, startY, endX, endY, color, thickness):
        Shape.__init__(self, endX, endY, color,thickness)
        self.startX = startX
        self.startY = startY

    def Draw(self, img):
        cv2.rectangle(img, (self.startX, self.startY), (self.endX, self.endY), self.color, self.thickness)

class Circle(Shape):
    def __init__(self, startX, startY, endX, endY, color, thickness):
        Shape.__init__(self, endX, endY, color,thickness)
        self.startX = startX
        self.startY = startY

    def Draw(self, img):
        cv2.ellipse(img, ((self.startX+self.endX)//2, (self.startY+self.endY)//2), (abs(self.endX-self.startX)//2, abs(self.endY-self.startY)//2),0,0,360, self.color, self.thickness)

class Triangle(Shape):
    def __init__(self, startX, startY, endX, endY, color, thickness):
        Shape.__init__(self, endX, endY, color,thickness)
        self.startX = startX
        self.startY = startY

    def Draw(self, img):
        pos=np.array([[self.startX, self.endY], [self.endX, self.endY],[(self.startX+self.endX)//2, self.startY]],dtype=np.int32)
        cv2.polylines(img,[pos] ,True, self.color, self.thickness)