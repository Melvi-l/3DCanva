from typing import List

import pygame
from graphic.Camera import OrthographicCamera
from geom.MathMatrix4 import MathMatrix4
from graphic.Scene import Scene
from graphic.meshes.Mesh import Mesh
from geom.Vector3 import Vector3


class Renderer:

    viewportMatrix: MathMatrix4

    def __init__(self, canva, width, height) -> None:
        self.initViewportMatrix(width, height)
        self.canva = canva
        return
    
    def initViewportMatrix(self, width, height):
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

    def render(self, scene: Scene, camera):
        for mesh in scene.meshList:
            mesh.draw(self.canva, camera.projectionMatrix, self.viewportMatrix)
        return
    

