from math import radians, tan
from geom.Matrix import Matrix
from geom.Vector3 import Vector3
from graphic.Camera.Camera import Camera
from rotation.Orientation import Orientation


class PerspectiveCamera(Camera):
    def __init__(self, fovInDeg, aspectRatio, near=.1, far=100):
        self.initCameraMatrix()
        self.initProjectionMatrix(fovInDeg, aspectRatio, near, far)

    def initCameraMatrix(self):
        eyeVector = Vector3(0,0,5)
        targetVector = Vector3(0,0,0)
        direction = Vector3.difference(eyeVector, targetVector)
        z = Vector3().copy(direction).negate().normalize()
        x = Vector3.cross(direction, Vector3(0,1,0)).normalize()
        y = Vector3.cross(z, x)
        print(" x: ",x , "\n", "y: ", y, "\n", "z: ", z)
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
            0, 0, (near + far) / (near - far), -near*far/(near-far),
            0, 0, 1, 0
        )
        # self.projectionMatrix = Matrix(
        #     d/aspectRatio, 0, 0, 0,
        #     0, d, 0, 0,
        #     0, 0, (near + far) / (near - far), 1,
        #     0, 0, -near*far/(near-far), 0
        # )
        print("projection matrix: \n", self.projectionMatrix)

    def setPosition(self, positionVector):
        self.cameraMatrix.setPosition(positionVector)
        self.updateViewMatrix()

    def setOrientation(self, orientationVector):
        self.cameraMatrix.setOrientation(orientationVector)
        self.updateViewMatrix()

    def rotate(self, rotationAxis, angle):
        rotationMatrix = Matrix.rotation(rotationAxis, angle)
        self.cameraMatrix.multiplyMatrix(rotationMatrix)
        self.updateViewMatrix()

    def lookAt(self, targetVector = Vector3()):
        eyeVector = self.cameraMatrix.getPosition()
        direction = Vector3.difference(eyeVector, targetVector)
        z = Vector3().copy(direction).negate().normalize()
        x = Vector3.cross(direction, Vector3(0,1,0)).normalize()
        y = Vector3.cross(z, x)
        orientation = Orientation(x,y,z)
        self.cameraMatrix.setOrientation(orientation)
        self.updateViewMatrix()

