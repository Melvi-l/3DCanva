from typing import List
import pygame
from color import RED, WHITE, YELLOW
from geom.Vector3 import Vector3
from geom.Vector4 import Vector4
from graphic.meshes.CubeMesh import CubeMesh

pygame.init()
font = pygame.font.Font(None, 24)


class HoverableCubeMesh(CubeMesh):
    mousePosition = (0,0)
    barycentricCoord = ""

    def draw(self, canva, viewMatrix, projectionMatrix, viewportMatrix):
        self.drawBarycentricCoord(canva)
        self.barycentricCoord = ""
        super().draw(canva, viewMatrix, projectionMatrix, viewportMatrix)

    def drawFace(self, face, canva, viewMatrix, projectionMatrix, viewportMatrix, backfaceCulling = False):
        if self.solid:
            super().drawFace(face, canva, viewMatrix, projectionMatrix, viewportMatrix,backfaceCulling)
            return
        computeVertexList = [self.vertexList[face[index]].getDrawPosition(self.modelMatrix, viewMatrix, projectionMatrix, viewportMatrix) for index in range(len(face))] # to reduce pipeline and looping around vertex
        for indexA in range(len(face)):
            indexB = (indexA+1)%len(face)
            vertexA = computeVertexList[indexA]
            vertexB = computeVertexList[indexB]
            if not(backfaceCulling):
                if self.isMouseInTriangle(computeVertexList) and self.isTriangleFacing(computeVertexList):
                    self.drawEdge(canva, vertexA, vertexB, RED, 3)
                    self.barycentricCoord = self.getBarycentricCoord(computeVertexList)
                self.drawEdge(canva, vertexA, vertexB)
                continue
            if self.isTriangleFacing(computeVertexList):
                if self.isMouseInTriangle(computeVertexList):
                    self.drawEdge(canva, vertexA, vertexB, RED, 3)
                    self.barycentricCoord = self.getBarycentricCoord(computeVertexList)
                self.drawEdge(canva, vertexA, vertexB)

    # MouseHover triangle
    def isMouseInTriangle(self, faceVertexList):
        a, b, c = faceVertexList
        mousePositionVector = Vector4(self.mousePosition[0], self.mousePosition[1])
        subAB = self.sign(mousePositionVector, a, b)
        subBC = self.sign(mousePositionVector, b, c)
        subCA = self.sign(mousePositionVector, c, a)

        neg = (subAB < 0) or (subBC < 0) or (subCA < 0)
        pos = (subAB > 0) or (subBC > 0) or (subCA > 0)

        return not (neg and pos)

    # Barycentre
    def getBarycentricCoord(self, faceVertexList): 
        a, b, c = faceVertexList

        AB = (b.x - a.x, b.y - a.y)
        AC = (c.x - a.x, c.y - a.y)
        AM = (self.mousePosition[0] - a.x, self.mousePosition[1] - a.y)

        detT = AB[0] * AC[1] - AB[1] * AC[0]

        u = (AM[0] * AC[1] - AM[1] * AC[0]) / detT
        v = (AB[0] * AM[1] - AB[1] * AM[0]) / detT
        w = 1 - u - v

        return f"{u:.2f}, {v:.2f}, {w:.2f}"
    
    def drawBarycentricCoord(self, canva):
        text_surface = font.render(self.barycentricCoord, True, WHITE)
        canva.blit(text_surface, (self.mousePosition[0] + 20, self.mousePosition[1]))

    def eventHandler(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.mousePosition = event.pos