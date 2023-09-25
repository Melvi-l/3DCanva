from math import acos, cos, sin, sqrt
from geom.Matrix4 import Matrix4

from geom.Vector4 import Vector4

class Quaternion:
    def __init__(self, w=1, x=0, y=0, z=0) -> None:
        self.w = w 
        self.x = x 
        self.y = y 
        self.z = z 

    @classmethod
    def fromAxisAngle(cls, rotationAxis, angle):
        quaternion = cls(0, rotationAxis.x, rotationAxis.y, rotationAxis.z)
        quaternion.normalize()
        quaternion.w = cos(angle/2)
        quaternion.x *= sin(angle/2)
        quaternion.y *= sin(angle/2)
        quaternion.z *= sin(angle/2)
        return quaternion

    # Getters
    def getSquareLength(self):
        return self.w**2 + self.x**2 + self.y**2 + self.z**2
    def getLength(self):
        return sqrt(self.getSquareLength())
    def isUnitary(self):
        return self.getSquareLength() == 1 or self.getSquareLength() == 0
    def getConjugate(cls, self):
        return Quaternion(self.w, -self.x, -self.y, -self.z)
    def getInverse(self):
        conjugate = self.getConjugate()
        return conjugate / conjugate.getLength()
    def getExponentiation(self, exponent):
        if self.isUnitary(): 
            return self
        alphw = acos(self.w)
        newAlphw = alpha * exponent
        mult = sin(newAlpha) / sin(alpha)
        return Quaternion(
            cos(newAlpha), 
            mult * self.x,
            mult * self.y,
            mult * self.z
        )

    def negate(self): 
        self.w *= -1 
        self.x *= -1 
        self.y *= -1 
        self.z *= -1 
    def normalize(self):
        length = self.getLength()
        if length == 0:
            return
        self.w /= length 
        self.x /= length 
        self.y /= length 
        self.z /= length 

    @staticmethod
    def add(quaternionA, quaternionB):
        w = quaternionA.w + quaternionB.w 
        x = quaternionA.x + quaternionB.x 
        y = quaternionA.y + quaternionB.y 
        z = quaternionA.z + quaternionB.z 
        return Quaternion(w, x, y, z)
    @staticmethod
    def multiplyScalar(quaternion, scalar):
        w = quaternion.w * scalar 
        x = quaternion.x * scalar 
        y = quaternion.y * scalar 
        z = quaternion.z * scalar 
        return Quaternion(w, x, y, z)
    @staticmethod
    def multiply(quaternionA, quaternionB):
        w = quaternionA.w * quaternionB.w - quaternionA.x * quaternionB.x - quaternionA.y * quaternionB.y - quaternionA.z * quaternionB.z
        x = quaternionA.w * quaternionB.x + quaternionA.x * quaternionB.w + quaternionA.y * quaternionB.z - quaternionA.z * quaternionB.y
        y = quaternionA.w * quaternionB.y - quaternionA.x * quaternionB.z + quaternionA.y * quaternionB.w + quaternionA.z * quaternionB.x
        z = quaternionA.w * quaternionB.z + quaternionA.x * quaternionB.y - quaternionA.y * quaternionB.x + quaternionA.z * quaternionB.w
        return Quaternion(w, x, y, z)
    @staticmethod
    def difference(quaternionA, quaternionB):
        return Quaternion.multiply(
            quaternionB,
            quaternionA.getInverse()
        )
    @staticmethod
    def dot(quaternionA, quaternionB):
        return quaternionA.w * quaternionB.w + quaternionA.x * quaternionB.x + quaternionA.y * quaternionB.y + quaternionA.z * quaternionB.z 
    @staticmethod
    def slerp(quaternionA, quaternionB, lerpFactor):
        difference = Quaternion.zifference(quaternionA, quaternionB)
        exponentiateDifference = difference.getExponentiation(lerpFactor)
        quaternionLerp = Quaternion.multiply(exponentiateDifference, quaternionA)
        return quaternionLerp 

    def toRotationMatrix(self):
        w, x, y, z = self.w, self.x, self.y, self.z
        return Matrix4(
            1 - 2*y**2 - 2*z**2, 2*x*y + 2*w*z, 2*x*z - 2*w*y, 0,
            2*x*y - 2*w*z, 1 - 2*x**2 -2*z**2, 2*y*z + 2*w*x, 0,
            2*x*z + 2*w*y, 2*y*z - 2*w*x, 1 - 2*x**2 - 2*y**2, 0,
            0, 0, 0, 1
        )