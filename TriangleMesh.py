from typing import List
from Matrix4 import Matrix4
from Vector3 import Vector3


class TriangleMesh:
    vertexList: List[Vector3]
    faceList: List[int]
    modelMatrix: Matrix4
    def __init__(self, vertexList, faceList) -> None:
        self.vertexList = vertexList
        self.faceList = faceList
        self.modelMatrix = Matrix4.identity()
    def setPosition(self, position: Vector3):
        self.modelMatrix.dx = position.x 
        self.modelMatrix.dy = position.y 
        self.modelMatrix.dz = position.z 
    def applyTranslation(self,translationVector: Vector3):
        translationMatrix = Matrix4.translation(translationVector)
        self.modelMatrix.multiplyMatrix(translationMatrix)
    def applyRotation(self, rotationAxis: Vector3):
        return