from geom.Vector3 import Vector3

class Orientation:
    def __init__(self, xAxis = Vector3.xAxis(), yAxis = Vector3.yAxis(), zAxis = Vector3.zAxis()):
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.zAxis = zAxis