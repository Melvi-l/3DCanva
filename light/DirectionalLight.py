from geom.Vector3 import Vector3
from light.Light import Light


class DirectionalLight(Light):
    def __init__(self, origin) -> None:
        super().__init__()
        self.origin = origin
        self.ray = Vector3().copy(self.origin).negate().normalize()

    def computeReflexion(self, normal):
        return max(Vector3.cross(self.ray, normal),0)