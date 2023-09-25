from math import sqrt

class Vector3:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def getSquareMagnitude(self) -> float:
        return self.x**2 + self.y**2 + self.z**2
    
    def getMagnitude(self) -> float:
        return sqrt(self.getSquareMagnitude())
    
    def normalize(self):
        magnitude = self.getMagitude()
        if magnitude == 0:
            return
        self.x /= magnitude
        self.y /= magnitude
        self.z /= magnitude

    def negate(self):
        self.x = - self.x
        self.y = - self.y
        self.z = - self.z

    def multiplyScalar(self, scalar: float):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar

    def addVector(self, vector: 'Vector3'):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    def toHomogenous(self):
        from geom.Vector4 import Vector4
        return Vector4(self.x,self.y,self.z,1)
    
    @staticmethod
    def dot(vectorA: 'Vector3', vectorB: 'Vector3') -> float:
        return vectorA.x*vectorB.x + vectorA.y*vectorB.y + vectorA.z*vectorB.z
    
    @staticmethod
    def cross(vectorA: 'Vector3', vectorB: 'Vector3') -> 'Vector3':
        return Vector3(
            vectorA.y * vectorB.z - vectorA.z * vectorB.y, 
            vectorA.z * vectorB.x - vectorA.x * vectorB.z, 
            vectorA.x * vectorB.y - vectorA.y * vectorB.x
        )
    
    def __str__(self) -> str:
        return f"Vector3({self.x}, {self.y}, {self.z})"
    