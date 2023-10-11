from typing import List
from debug.GUI import GUI
from graphic.meshes.Mesh import Mesh


class Scene:
    debug: GUI
    drawableList: List[Mesh]
    def __init__(self) -> None:
        self.drawableList = []
    def add(self,mesh: Mesh):
        self.drawableList.append(mesh)
    def draw(self, canva, viewMatrix, projectionMatrix, viewportMatrix):
        if hasattr(self, "debug") and self.debug is not None:
            self.debug.draw()
        for drawable in self.drawableList:
            drawable.draw(canva, viewMatrix, projectionMatrix, viewportMatrix)
    