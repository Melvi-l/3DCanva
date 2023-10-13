from graphic.meshes.CubeMesh import CubeMesh
from rotation.Quaternion import Quaternion


class RotationAnimation:
    def __init__(self, object: CubeMesh):
        self.duration = 0
        self.time = 0
        self.object = object
        self.originQuaternion = Quaternion()
        self.targetQuaternion = Quaternion()

    @property
    def isActive(self):
        return self.time < self.duration
    
    def animateRotationTo(self, time, targetQuaternion):
        self.time = 0
        self.duration = time
        self.originQuaternion = self.object.getQuaternion()
        print(self.originQuaternion)
        self.targetQuaternion = targetQuaternion
        print(self.targetQuaternion)

    def animateRotationOf(self, time, rotationQuaternion):
        targetQuaternion = Quaternion.multiply(self.object.getQuaternion(), rotationQuaternion)
        self.animateRotationTo(time, targetQuaternion)

    def update(self, elapsedTime):
        if (self.duration == 0):
            return 
        self.time += elapsedTime 
        lerpFactor = self.time / self.duration
        currentQuaternion = Quaternion.slerp(self.originQuaternion, self.targetQuaternion, lerpFactor)
        self.object.setQuaternion(currentQuaternion)
