from typing import List

import pygame
from graphic.Camera import OrthographicCamera
from geom.MathMatrix4 import MathMatrix4
from graphic.Scene import Scene
from graphic.TriangleMesh import TriangleMesh
from geom.Vector3 import Vector3

GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 226, 82)

class Renderer:

    viewportMatrix: MathMatrix4

    def __init__(self, canva, width: float, height: float) -> None:
        self.initViewportMatrix(width, height)
        self.canva = canva
        return
    
    def initViewportMatrix(self, width: float, height: float):
        originX = 0 
        originY = 0
        nearDepth = 0
        farDepth = 1
        self.viewportMatrix = MathMatrix4(
            width/2, 0, 0, originX + width/2,
            0, height/2, 0, originY + height/2,
            0, 0, (farDepth-nearDepth)/2, (nearDepth+farDepth)/2,
            0, 0, 0, 1  
        )

    def render(self, scene: Scene, camera: OrthographicCamera):
        for mesh in scene.meshList:
            self.drawMesh(mesh, camera.projectionMatrix)
        return
    
    def drawMesh(self, mesh: TriangleMesh, projectionMatrix: MathMatrix4):
        for face in mesh.faceList:
            self.drawFace(mesh.vertexList, face, mesh.modelMatrix, projectionMatrix)
        return
    def drawFace(self, vertexList: List[Vector3], face: List[int], modelMatrix: MathMatrix4, projectionMatrix: MathMatrix4):
        computeVertex = [None for _ in range(len(face))] # to reduce pipeline and looping around vertex
        for indexA in range(len(face)):
            if computeVertex[indexA] is None:
                computeVertex[indexA] = self.getDrawPosition(vertexList[face[indexA]], modelMatrix, projectionMatrix) 
            vertexA = computeVertex[indexA]

            indexB = (indexA+1)%len(face)
            if computeVertex[indexB] is None:
                computeVertex[indexB] = self.getDrawPosition(vertexList[face[indexB]], modelMatrix, projectionMatrix) 
            vertexB = computeVertex[indexB]

            # print("inp", vertexList[face[indexA]], vertexList[face[indexB]])
            # print("seg", vertexA, vertexB)
            self.drawEdge(vertexA, vertexB)

    def getDrawPosition(self, vertex: Vector3, modelMatrix: MathMatrix4, projectionMatrix: MathMatrix4):
        vertexHomogenous = vertex.toHomogenous()
        # print(vertexHomogenous)
        vertexHomogenous.multiplyMatrix4(modelMatrix)
        # print(vertexHomogenous)
        vertexHomogenous.multiplyMatrix4(projectionMatrix)
        # print(vertexHomogenous)
        vertexHomogenous.multiplyMatrix4(self.viewportMatrix)
        # print(vertexHomogenous)
        return vertexHomogenous

    def drawEdge(self, vertexA: Vector3, vertexB: Vector3):
        # print("draw", vertexA.x, vertexA.y, vertexB.x, vertexB.y)
        pygame.draw.line(self.canva, YELLOW, (vertexA.x,
                     vertexA.y), (vertexB.x, vertexB.y), 1)
