from typing import List

import pygame
from color import WHITE, YELLOW
from geom.MathMatrix4 import MathMatrix4
from geom.Matrix import Matrix
from rotation.Euler import Euler
from rotation.Orientation import Orientation
from rotation.Quaternion import Quaternion
from geom.Vector3 import Vector3


class Mesh:
    vertexList: List[Vector3]
    faceList: List[int]
    modelMatrix: Matrix
    solid: bool
    def __init__(self, vertexList, faceList, solid = False) -> None:
        self.vertexList = vertexList
        self.faceList = faceList
        self.modelMatrix = Matrix.identity()
        self.solid = solid
    def applyScale(self, scaleFactor):
        scaleMatrix = Matrix.scale(scaleFactor)
        self.modelMatrix.multiplyMatrix(scaleMatrix)
        return self
    def applyTranslation(self,translationVector):
        translationMatrix = Matrix.translation(translationVector)
        self.modelMatrix.multiplyMatrix(translationMatrix)
        return self
    def applyRotation(self, rotationAxis, angle):
        # Euler (TODO-impl: extrinsic)
        # euler = Euler()
        # if rotationAxis == Vector3.x()Axis():
        #     euler = Euler(angle, 0, 0)
        # if rotationAxis == Vector3.y()Axis():
        #     euler = Euler(0, angle, 0)
        # if rotationAxis == Vector3.x()Axis():
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

        # self.modelMatrix = rotationMatrix.setPosition(self.modelMatrix.getPosition()).multiplyMatrix(self.modelMatrix.setPosition(Vector3()))
        self.modelMatrix.multiplyMatrix(rotationMatrix)
        return self
    
    def getQuaternion(self):
        return self.modelMatrix.getQuaternion()
    def setQuaternion(self, quaternion):
        self.modelMatrix.setQuaternion(quaternion)
        return self
    def getEuler(self):
        return self.modelMatrix.getQuaternion()
    def setEuler(self, quaternion):
        self.modelMatrix.setQuaternion(quaternion)
        return self
    
    def draw(self, canva, viewMatrix, projectionMatrix, viewportMatrix, light):
        for face in self.faceList:
            print(light)
            self.drawFace(face, canva, viewMatrix, projectionMatrix, viewportMatrix, light)
        return
    
    def drawFace(self, face, canva, viewMatrix, projectionMatrix, viewportMatrix, light, backfaceCulling = True):
        computeVertexList = [self.vertexList[face[index]].getDrawPosition(self.modelMatrix, viewMatrix, projectionMatrix, viewportMatrix) for index in range(len(face))] # to reduce pipeline and looping around vertex
        if not(backfaceCulling) or self.isTriangleFacing(computeVertexList):
            if self.solid:
                color = WHITE
                print(light)
                if light:
                    color = WHITE * light.computeReflexion(self.getTriangleNormal(computeVertexList))
                self.fillFace(canva, computeVertexList, color)
                return
            for indexA in range(len(face)):
                indexB = (indexA+1)%len(face)
                vertexA = computeVertexList[indexA]
                vertexB = computeVertexList[indexB]
                self.drawEdge(canva, vertexA, vertexB)

    def fillFace(self, canva, vertexList, color=WHITE):
        pygame.draw.polygon(canva, color, [(vertex.x, vertex.y) for vertex in vertexList])

    def drawEdge(self, canva, vertexA, vertexB, color = YELLOW, width = 1):
        # print("draw", vertexA.x, vertexA.y, vertexB.x, vertexB.y)
        pygame.draw.line(canva, color, (vertexA.x,
                     vertexA.y), (vertexB.x, vertexB.y), width)

    def isTriangleFacing(self, faceVertexList):
        return self.sign(*faceVertexList) < 0
    
    def getTriangleNormal(self, faceVertexList):
        a,b,c = faceVertexList
        edgeAB = Vector3.difference(a,b)
        edgeAC = Vector3.difference(a,c)
        return Vector3.cross(edgeAB, edgeAC).normalize()
    
    def sign(self, a, b, c):
        return (a.x - c.x) * (b.y - c.y) - (b.x - c.x) * (a.y - c.y)
