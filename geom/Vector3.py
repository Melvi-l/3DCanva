from math import sqrt

class Vector3:
    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def xAxis(cls):
        return cls(1,0,0)
    @classmethod
    def yAxis(cls):
        return cls(0,1,0)
    @classmethod
    def zAxis(cls):
        return cls(0,0,1)

    def getSquareMagnitude(self) -> float:
        return self.x**2 + self.y**2 + self.z**2
    def getMagnitude(self) -> float:
        return sqrt(self.getSquareMagnitude())

    def normalize(self):
        magnitude = self.getMagnitude()
        if magnitude == 0:
            return
        self.x /= magnitude
        self.y /= magnitude
        self.z /= magnitude
        return self
    def negate(self):
        self.x = - self.x
        self.y = - self.y
        self.z = - self.z
        return self

    def multiplyScalar(self, scalar: float):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self
    def addVector(self, vector: 'Vector3'):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z
        return self

    def toHomogenous(self):
        from geom.Vector4 import Vector4
        return Vector4(self.x,self.y,self.z,1)
    
    @staticmethod
    def difference(vectorA, vectorB):
        return Vector3(vectorB.x + vectorA.x, vectorB.y + vectorA.y, vectorB.z + vectorA.z)
    @staticmethod
    def difference(vectorA, vectorB):
        return Vector3(vectorB.x - vectorA.x, vectorB.y - vectorA.y, vectorB.z - vectorA.z)
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
    @staticmethod
    def lerp(vectorA, vectorB, lerpFactor):
        return Vector3.add(vectorA, Vector3.difference(vectorA, vectorB).multiplyScalar(lerpFactor))

    def __str__(self) -> str:
        return f"Vector3({self.x}, {self.y}, {self.z})"
    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y and self.z == __value.z
    