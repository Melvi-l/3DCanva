from typing import List
from geom.MathMatrix4 import MathMatrix4
from graphic.meshes.Mesh import Mesh


class Scene:
    meshList: List[Mesh]
    def __init__(self) -> None:
        self.meshList = []
    def add(self,mesh: Mesh):
        self.meshList.append(mesh)
    