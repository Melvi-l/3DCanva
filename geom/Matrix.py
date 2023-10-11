from math import sqrt
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
    def setPosition(self, positionVector):
        self.dx = positionVector.x 
        self.dy = positionVector.y 
        self.dz = positionVector.z 
        return self
    def setOrientation(self, orientation):
        self.ax, self.ay, self.az = orientation.xAxis.x, orientation.xAxis.y, orientation.xAxis.z
        self.bx, self.by, self.bz = orientation.yAxis.x, orientation.yAxis.y, orientation.yAxis.z
        self.cx, self.cy, self.cz = orientation.zAxis.x, orientation.zAxis.y, orientation.zAxis.z
        return self
    
    def lookAt(self, target):
        pass


    # def getQuaternion(self):
    #     from rotation.Quaternion import Quaternion
    #     # from https://gamemath.com/book/orient.html#matrix_to_quaternion
    #     fourWSquaredMinus1 = self.ax + self.by + self.cz    
    #     fourXSquaredMinus1 = self.ax - self.by - self.cz    
    #     fourYSquaredMinus1 = self.by - self.ax - self.cz    
    #     fourZSquaredMinus1 = self.cz - self.ax - self.by   
    #     biggestIndex = 0
    #     fourBiggestSquaredMinus1 = fourWSquaredMinus1
    #     if (fourXSquaredMinus1 > fourBiggestSquaredMinus1):
    #         fourBiggestSquaredMinus1 = fourXSquaredMinus1
    #         biggestIndex = 1
    #     if (fourYSquaredMinus1 > fourBiggestSquaredMinus1):
    #         fourBiggestSquaredMinus1 = fourYSquaredMinus1
    #         biggestIndex = 2
    #     if (fourZSquaredMinus1 > fourBiggestSquaredMinus1):
    #         fourBiggestSquaredMinus1 = fourZSquaredMinus1
    #         biggestIndex = 3
    #     biggestVal = sqrt(fourBiggestSquaredMinus1 + 1) / 2
    #     mult = 1 / 4*biggestVal
    #     match biggestIndex:
    #         case 0:
    #             w = biggestVal
    #             x = (self.bz - self.cy) * mult
    #             y = (self.cx - self.az) * mult
    #             z = (self.ay - self.bx) * mult

    #         case 1:
    #             x = biggestVal
    #             w = (self.bz - self.cy) * mult
    #             y = (self.ay + self.bx) * mult
    #             z = (self.cx + self.az) * mult

    #         case 2:
    #             y = biggestVal
    #             w = (self.cx - self.az) * mult
    #             x = (self.ay + self.bx) * mult
    #             z = (self.bz + self.cy) * mult

    #         case 3:
    #             z = biggestVal
    #             w = (self.ay - self.bx) * mult
    #             x = (self.cx + self.az) * mult
    #             y = (self.bz + self.cy) * mult

    #     return Quaternion(w,x,y,z)

    def getQuaternion(self):
        from rotation.Quaternion import Quaternion
        w = sqrt(self.getTrace())/2
        x = (self.cy - self.bz) / (4 * w)
        y = (self.az - self.cx) / (4 * w)
        z = (self.bx - self.ay) / (4 * w)
        return Quaternion(w,x,y,z)
    
    def setQuaternion(self, quaternion):
        rotationMatrix = quaternion.toRotationMatrix()
        self.ax, self.ay, self.az = rotationMatrix.ax, rotationMatrix.ay, rotationMatrix.az
        self.bx, self.by, self.bz = rotationMatrix.bx, rotationMatrix.by, rotationMatrix.bz
        self.cx, self.cy, self.cz = rotationMatrix.cx, rotationMatrix.cy, rotationMatrix.cz
        return self
