from geom.Matrix import Matrix
class Camera: 
    cameraMatrix: Matrix
    viewMatrix: Matrix
    projectionMatrix: Matrix

    def updateViewMatrix(self):
        # self.viewMatrix = Matrix.multiply(
        #     Matrix.identity().setOrientation(self.cameraMatrix.getOrientation()).getInverse(), 
        #     Matrix.identity().setPosition(self.cameraMatrix.getPosition()).getInverse()
        # )
        self.viewMatrix = self.cameraMatrix.getInverse()