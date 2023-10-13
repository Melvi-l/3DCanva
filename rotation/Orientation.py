from geom.Vector3 import Vector3

class Orientation:
    def __init__(self, xAxis = Vector3.x(), yAxis = Vector3.y(), zAxis = Vector3.z()):
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.zAxis = zAxis

    def toMatrix(self):
        from geom.Matrix import Matrix
        return Matrix(
            self.xAxis.x, self.yAxis.x, self.zAxis.x, 0, 
            self.xAxis.y, self.yAxis.y, self.zAxis.y, 0, 
            self.xAxis.z, self.yAxis.z, self.zAxis.z, 0, 
            0, 0, 0, 1
        )
    
    def __str__(self) -> str:
        return f"Orientation: [{'{:.2f}'.format(self.xAxis.x)}, {'{:.2f}'.format(self.yAxis.x)}, {'{:.2f}'.format(self.zAxis.x)}]\n" \
               f"             [{'{:.2f}'.format(self.xAxis.y)}, {'{:.2f}'.format(self.yAxis.y)}, {'{:.2f}'.format(self.zAxis.y)}]\n" \
               f"             [{'{:.2f}'.format(self.xAxis.z)}, {'{:.2f}'.format(self.yAxis.z)}, {'{:.2f}'.format(self.zAxis.z)}]\n" \
    