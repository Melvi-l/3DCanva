from typing import List
from geom.Matrix import Matrix
from rotation.Euler import Euler
from rotation.Orientation import Orientation
from rotation.Quaternion import Quaternion
from geom.Vector3 import Vector3


class TriangleMesh:
    vertexList: List[Vector3]
    faceList: List[int]
    modelMatrix: Matrix
    def __init__(self, vertexList, faceList) -> None:
        self.vertexList = vertexList
        self.faceList = faceList
        self.modelMatrix = Matrix.identity()
    def applyScale(self, scaleFactor: float):
        scaleMatrix = Matrix.scale(scaleFactor)
        self.modelMatrix.multiplyMatrix(scaleMatrix)
        return self
    def applyTranslation(self,translationVector: Vector3):
        translationMatrix = Matrix.translation(translationVector)
        self.modelMatrix.multiplyMatrix(translationMatrix)
        return self
    def applyRotation(self, rotationAxis: Vector3, angle):
        # Euler (TODO-impl: extrinsic)
        # euler = Euler()
        # if rotationAxis == Vector3.xAxis():
        #     euler = Euler(angle, 0, 0)
        # if rotationAxis == Vector3.yAxis():
        #     euler = Euler(0, angle, 0)
        # if rotationAxis == Vector3.xAxis():
        #     euler = Euler(0, 0, angle)
        # rotationMatrix = euler.toRotationMatrix()

        # Axis-angle
        # rotationAxis.normalize()
        # rotationMatrix = Matrix4.rotation(rotationAxis, angle)

        # Exponential Map
        # rotationAxis.normalize()
        # rotationAxis.multiplyScalar(angle) # is the exponential map

        # extractAngle = rotationAxis.getMagnitude()
        # rotationAxis.normalize()
        # rotationMatrix = Matrix4.rotation(rotationAxis, extractAngle)


        # Quaternion
        quaternion = Quaternion.fromAxisAngle(rotationAxis, angle)
        rotationMatrix = quaternion.toRotationMatrix()

        self.modelMatrix = rotationMatrix.setPosition(self.modelMatrix.getPosition()).multiplyMatrix(self.modelMatrix.setPosition(Vector3()))
        # self.modelMatrix.multiplyMatrix(rotationMatrix)
        return self
