from math import sqrt
from Vector3 import Vector3
from Matrix4 import Matrix4


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

    def negate(self):
        self.x = - self.x
        self.y = - self.y
        self.z = - self.z
        self.w = - self.w
        
    def multiplyScalar(self, scalar: float):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        self.w *= scalar

    def addVector(self, vector: 'Vector4'):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z
        self.w += vector.w

    def multiplyMatrix4(self, matrix: Matrix4):
        temp = Vector4()
        x = self.x * matrix.ax + self.y * matrix.ay + self.z * matrix.az + self.w * matrix.aw 
        y = self.x * matrix.bx + self.y * matrix.by + self.z * matrix.bz + self.w * matrix.bw 
        z = self.x * matrix.cx + self.y * matrix.cy + self.z * matrix.cz + self.w * matrix.cw 
        w = self.x * matrix.dx + self.y * matrix.dy + self.z * matrix.dz + self.w * matrix.dw 
        self.copy(temp)

    def copy(self, vector):
        self.x = vector.x
        self.y = vector.y
        self.z = vector.z
        self.w = vector.w        
    def toCarthesian(self) -> Vector3:
        return Vector3(self.x/self.w, self.y/self.w, self.z/self.w)
    def __str__(self) -> str:
        return f"Vector4({self.x}, {self.y}, {self.z}, {self.w})"
    
    @staticmethod
    def dot(vectorA: 'Vector4', vectorB: 'Vector4') -> float:
        return vectorA.x*vectorB.x + vectorA.y*vectorB.y + vectorA.z*vectorB.z + vectorA.w*vectorB.w
    