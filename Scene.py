from typing import List
from Matrix4 import Matrix4
from TriangleMesh import TriangleMesh


class Scene:
    meshList: List[TriangleMesh]
    def __init__(self) -> None:
        self.meshList = []
    def add(self,mesh: TriangleMesh):
        self.meshList.append(mesh)
    