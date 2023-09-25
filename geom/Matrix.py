from pygame import Vector3
from geom.MathMatrix4 import MathMatrix4
from rotation.Orientation import Orientation


class Matrix(MathMatrix4):
    def getPosition(self):
        return Vector3(
            self.dx,
            self.dy,
            self.dz,
        )
    def getOrientation(self):
        return Orientation(
            Vector3(self.ax, self.ay, self.az),
            Vector3(self.bx, self.by, self.bz),
            Vector3(self.cx, self.cy, self.cz),
        )
    def setPosition(self, position):
        self.dx = position.x 
        self.dy = position.y 
        self.dz = position.z 
        return self
    def setOrientation(self, orientation):
        self.ax, self.ay, self.az = orientation.xAxis.x, orientation.xAxis.y, orientation.xAxis.z
        self.bx, self.by, self.bz = orientation.yAxis.x, orientation.yAxis.y, orientation.yAxis.z
        self.cx, self.cy, self.cz = orientation.zAxis.x, orientation.zAxis.y, orientation.zAxis.z
        return self