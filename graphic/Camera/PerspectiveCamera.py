from math import radians, tan
from geom.Matrix import Matrix
from geom.Vector3 import Vector3
from graphic.Camera.Camera import Camera
from rotation.Orientation import Orientation


class PerspectiveCamera(Camera):
    def __init__(self, fovInDeg, aspectRatio, near=.1, far=1000):
        self.initCameraMatrix()
        self.initProjectionMatrix(fovInDeg, aspectRatio, near, far)

    def initCameraMatrix(self):
        eyeVector = Vector3(0,0,5)
        targetVector = Vector3(0,0,0)
        direction = Vector3.difference(eyeVector, targetVector)
        z = Vector3().copy(direction).negate().normalize()
        x = Vector3.cross(direction, Vector3.y()).normalize()
        y = Vector3.cross(z, x)
        self.cameraMatrix = Matrix(
            x.x, y.x, z.x, eyeVector.x,
            x.y, y.y, z.y, eyeVector.y,
            x.z, y.z, z.z, eyeVector.z,
            0, 0, 0, 1
        )
        self.updateViewMatrix()
        print("view matrix: \n", self.viewMatrix)

    def initProjectionMatrix(self, fovInDeg, aspectRatio, near, far):
        fovInRad = radians(fovInDeg)
        d = 1 / tan(fovInRad/2)
        self.projectionMatrix = Matrix(
            d/aspectRatio, 0, 0, 0,
            0, d, 0, 0,
            0, 0, (near + far) / (near - far), 2*near*far/(near-far),
            0, 0, -1, 0
        )
        # self.projectionMatrix = Matrix(
        #     d/aspectRatio, 0, 0, 0,
        #     0, d, 0, 0,
        #     0, 0, (near + far) / (near - far), 1,
        #     0, 0, -near*far/(near-far), 0
        # )
        print("projection matrix: \n", self.projectionMatrix)


