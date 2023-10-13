import pygame
from color import BLUE, GREEN, RED
from geom.Matrix import Matrix
from geom.Vector3 import Vector3


class AxesHelper:
    def __init__(self, size = 1):
        self.helperSize = size
        self.createHelper()
    def createHelper(self):
        origin = Vector3()
        self.xAxisLine = (origin, Vector3.x().multiplyScalar(self.helperSize))
        self.xAxisColor = RED
        self.yAxisLine = (origin, Vector3.y().multiplyScalar(self.helperSize))
        self.yAxisColor = GREEN
        self.zAxisLine = (origin, Vector3.z().multiplyScalar(self.helperSize))
        self.zAxisColor = BLUE
    def draw(self, canva, viewMatrix, projectionMatrix, viewportMatrix):
        self.drawLine(self.xAxisLine, self.xAxisColor, canva, viewMatrix, projectionMatrix, viewportMatrix)
        self.drawLine(self.yAxisLine, self.yAxisColor, canva, viewMatrix, projectionMatrix, viewportMatrix)
        self.drawLine(self.zAxisLine, self.zAxisColor, canva, viewMatrix, projectionMatrix, viewportMatrix)
    def drawLine(self, line, color, canva, viewMatrix, projectionMatrix, viewportMatrix):
        computeVertexA = line[0].getDrawPosition(Matrix.identity(), viewMatrix, projectionMatrix, viewportMatrix)
        computeVertexB = line[1].getDrawPosition(Matrix.identity(), viewMatrix, projectionMatrix, viewportMatrix)
        pygame.draw.line(canva, color, (computeVertexA.x, computeVertexA.y), (computeVertexB.x, computeVertexB.y), 2)