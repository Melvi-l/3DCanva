from math import sqrt
from geom.MathMatrix4 import MathMatrix4


class Vector4:

    def __init__(self, x=0, y=0, z=0, w=0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def getSquareMagnitude(self) -> float:
        return self.x**2 + self.y**2 + self.z**2 + self.w**2
    def getMagnitude(self) -> float:
        return sqrt(self.getSquareMagnitude())

    def normalize(self):
        magnitude = self.getMagitude()
        if magnitude == 0:
            return
        self.x /= magnitude
        self.y /= magnitude
        self.z /= magnitude
        self.w /= magnitude
        return self
    def negate(self):
        self.x = - self.x
        self.y = - self.y
        self.z = - self.z
        self.w = - self.w
        return self
        
    def multiplyScalar(self, scalar: float):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        self.w *= scalar
        return self
    def addVector(self, vector: 'Vector4'):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z
        self.w += vector.w
        return self
    def multiplyMatrix4(self, matrix: MathMatrix4):
        x = self.x * matrix.ax + self.y * matrix.bx + self.z * matrix.cx + self.w * matrix.dx
        y = self.x * matrix.ay + self.y * matrix.by + self.z * matrix.cy + self.w * matrix.dy
        z = self.x * matrix.az + self.y * matrix.bz + self.z * matrix.cz + self.w * matrix.dz
        w = self.x * matrix.aw + self.y * matrix.bw + self.z * matrix.cw + self.w * matrix.dw
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        return self

    @staticmethod
    def add(vectorA, vectorB):
        result = Vector4()
        result.x = vectorA.x + vectorB.x
        result.y = vectorA.y + vectorB.y
        result.z = vectorA.z + vectorB.z
        result.w = vectorA.w + vectorB.w
        return result
    
    def copy(self, vector):
        self.x = vector.x
        self.y = vector.y
        self.z = vector.z
        self.w = vector.w   
        return self

    def toCarthesian(self):
        from geom.Vector3 import Vector3
        return Vector3(self.x/self.w, self.y/self.w, self.z/self.w)
    def __str__(self) -> str:
        return f"Vector4({self.x}, {self.y}, {self.z}, {self.w})"
    
    @staticmethod
    def dot(vectorA: 'Vector4', vectorB: 'Vector4') -> float:
        return vectorA.x*vectorB.x + vectorA.y*vectorB.y + vectorA.z*vectorB.z + vectorA.w*vectorB.w
    