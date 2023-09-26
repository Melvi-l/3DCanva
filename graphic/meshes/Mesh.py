from typing import List

import pygame
from color import YELLOW
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
    def __init__(self, vertexList, faceList) -> None:
        self.vertexList = vertexList
        self.faceList = faceList
        self.modelMatrix = Matrix.identity()
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
    
    def getQuaternion(self):
        return self.modelMatrix.getQuaternion()
    def setQuaternion(self, quaternion):
        self.modelMatrix.setQuaternion(quaternion)
        return self
        
    def animateRotationTo(self, duration, endQuaternion):
        clock = pygame.time.Clock()        
        startQuaternion = self.getQuaternion()
        startTime = pygame.time.get_ticks()
        while True: 
            elapsedTime = pygame.time.get_ticks() - startTime
            print(elapsedTime)
            if  elapsedTime > duration:
                break
            lerpFactor = elapsedTime / duration
            currentQuaternion = Quaternion.slerp(startQuaternion, endQuaternion, lerpFactor)
            self.setQuaternion(currentQuaternion)

    def draw(self, canva, projectionMatrix, viewportMatrix):
        for face in self.faceList:
            self.drawFace(face, canva, projectionMatrix, viewportMatrix)
        return
    
    def drawFace(self, face, canva, projectionMatrix, viewportMatrix):
        computeVertexList = [self.getDrawPosition(self.vertexList[face[index]], self.modelMatrix, projectionMatrix, viewportMatrix) for index in range(len(face))] # to reduce pipeline and looping around vertex
        for indexA in range(len(face)):
            indexB = (indexA+1)%len(face)
            vertexA = computeVertexList[indexA]
            vertexB = computeVertexList[indexB]
            self.drawEdge(canva, vertexA, vertexB)

    def getDrawPosition(self, vertex, modelMatrix, projectionMatrix, viewportMatrix):
        vertexHomogenous = vertex.toHomogenous()
        vertexHomogenous.multiplyMatrix4(modelMatrix)
        vertexHomogenous.multiplyMatrix4(projectionMatrix)
        vertexHomogenous.multiplyMatrix4(viewportMatrix)
        return vertexHomogenous

    def drawEdge(self, canva, vertexA, vertexB):
        # print("draw", vertexA.x, vertexA.y, vertexB.x, vertexB.y)
        pygame.draw.line(canva, YELLOW, (vertexA.x,
                     vertexA.y), (vertexB.x, vertexB.y), 1)