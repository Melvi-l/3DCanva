from geom.Matrix import Matrix
from graphic.Camera.Camera import Camera

class OrthographicCamera(Camera):
    def __init__(self, left: float, right: float, top: float, bottom: float, near: float, far: float) -> None:
        self.cameraMatrix = Matrix.identity()
        self.updateViewMatrix()
        self.initProjectionMatrix(left, right, top, bottom, near, far)
    def initProjectionMatrix(self, left: float, right: float, top: float, bottom: float, near: float, far: float):
        self.projectionMatrix = Matrix(
            2/(right-left), 0, 0, -(right+left)/(right-left),
            0, 2/(top-bottom), 0, -(top+bottom)/(top-bottom),
            0, 0, -2/(far-near), -(far+near)/(far-near),
            0, 0, 0, 1
        )