from geom.Matrix import Matrix
class Camera: 
    cameraMatrix: Matrix
    viewMatrix: Matrix
    projectionMatrix: Matrix

    def updateViewMatrix(self):
        self.viewMatrix = self.cameraMatrix.getInverse()