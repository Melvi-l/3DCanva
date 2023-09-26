from geom.Vector3 import Vector3
from graphic.meshes.Mesh import Mesh


class CubeMesh(Mesh):
    def __init__(self, width, height, depth) -> None:
        super().__init__([
            Vector3(-width/2,-height/2,-depth/2),
            Vector3(-width/2,-height/2,depth/2),
            Vector3(-width/2,height/2,-depth/2),
            Vector3(-width/2,height/2,depth/2),
            Vector3(width/2,-height/2,-depth/2),
            Vector3(width/2,-height/2,depth/2),
            Vector3(width/2,height/2,-depth/2),
            Vector3(width/2,height/2,depth/2),
        ],[
                [0,1,2],
                [1,3,2],
                [2,3,7],
                [2,7,6],
                [1,7,3],
                [1,5,7],
                [4,6,7],
                [4,7,5],
                [0,5,1],
                [0,4,5],
                [0,2,6],
                [0,6,4]
        ])