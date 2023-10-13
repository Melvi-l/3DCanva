from typing import List
from debug.GUI import GUI
from graphic.meshes.Mesh import Mesh
from light.Light import Light


class Scene:
    debug: GUI
    light: Light
    drawableList: List[Mesh]
    def __init__(self) -> None:
        self.drawableList = []
        self.debug = None
        self.light = None
    def add(self,mesh: Mesh):
        self.drawableList.append(mesh)
    def draw(self, canva, viewMatrix, projectionMatrix, viewportMatrix):
        if hasattr(self, "debug") and self.debug is not None:
            self.debug.draw()
        for drawable in self.drawableList:
            if isinstance(drawable, Mesh):   
                drawable.draw(canva, viewMatrix, projectionMatrix, viewportMatrix, self.light)
                continue
            drawable.draw(canva, viewMatrix, projectionMatrix, viewportMatrix)
    