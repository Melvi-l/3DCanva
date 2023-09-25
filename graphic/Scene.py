from typing import List
from geom.MathMatrix4 import MathMatrix4
from graphic.TriangleMesh import TriangleMesh


class Scene:
    meshList: List[TriangleMesh]
    def __init__(self) -> None:
        self.meshList = []
    def add(self,mesh: TriangleMesh):
        self.meshList.append(mesh)
    