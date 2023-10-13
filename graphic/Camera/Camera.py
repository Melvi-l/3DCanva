from geom.Matrix import Matrix
from geom.Vector3 import Vector3
from rotation.Orientation import Orientation
class Camera: 
    cameraMatrix: Matrix
    viewMatrix: Matrix
    projectionMatrix: Matrix

    def updateViewMatrix(self):
        self.viewMatrix = self.cameraMatrix.getInverse()

    def setPosition(self, positionVector):
        self.cameraMatrix.setPosition(positionVector)
        self.updateViewMatrix()
        return self

    def setOrientation(self, orientationVector):
        self.cameraMatrix.setOrientation(orientationVector)
        self.updateViewMatrix()
        return self

    def rotate(self, rotationAxis, angle):
        rotationMatrix = Matrix.rotation(rotationAxis, angle)
        self.cameraMatrix.multiplyMatrix(rotationMatrix)
        self.updateViewMatrix()
        return self

    def lookAt(self, targetVector = Vector3()):
        up = Vector3.y()
        print(up)
        eyeVector = self.cameraMatrix.getPosition()
        direction = Vector3.difference(eyeVector, targetVector)
        if (Vector3.isColinear(direction, up)):
            self.cameraMatrix.setOrientation(Orientation(Vector3.x(), Vector3.z().negate(), Vector3.y()))
            self.updateViewMatrix()
            return self 
        z = Vector3().copy(direction).negate().normalize()
        x = Vector3.cross(direction, up).normalize()
        y = Vector3.cross(z, x)
        self.cameraMatrix.setOrientation(Orientation(x,y,z))
        self.updateViewMatrix()
        return self
