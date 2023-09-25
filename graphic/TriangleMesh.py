from typing import List
from geom.Matrix4 import Matrix4
from rotation.Euler import Euler
from rotation.Quaternion import Quaternion
from geom.Vector3 import Vector3


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
    def applyScale(self, scaleFactor: float):
        scaleMatrix = Matrix4.scale(scaleFactor)
        self.modelMatrix.multiplyMatrix(scaleMatrix)
    def applyTranslation(self,translationVector: Vector3):
        translationMatrix = Matrix4.translation(translationVector)
        self.modelMatrix.multiplyMatrix(translationMatrix)
    def applyRotation(self, rotationAxis: Vector3, angle):
        # Matrix
        # rotationMatrix = Matrix4.rotation(rotationAxis, angle)

        # Euler 
        euler = Euler()
        if rotationAxis == Vector3.xAxis():
            euler = Euler(angle, 0, 0)
        if rotationAxis == Vector3.yAxis():
            euler = Euler(0, angle, 0)
        if rotationAxis == Vector3.xAxis():
            euler = Euler(0, 0, angle)
        rotationMatrix = euler.toRotationMatrix()

        # Quaternion
        # quaternion = Quaternion.fromAxisAngle(rotationAxis, angle)
        # rotationMatrix = quaternion.toRotationMatrix()
        self.modelMatrix.multiplyMatrix(rotationMatrix)