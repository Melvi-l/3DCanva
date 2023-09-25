from math import cos, sin
from geom.Matrix4 import Matrix4
from rotation.Orientation import Orientation


class Euler:
    def __init__(self, pitch=0, heading=0, bank=0):
        self.pitch = pitch
        self.heading = heading
        self.bank = bank

    def toRotationMatrix(self, orientation = Orientation()):
        pitchMatrix = Matrix4.rotation(orientation.xAxis, self.pitch)
        headingMatrix = Matrix4.rotation(orientation.yAxis, self.heading)
        bankMatrix = Matrix4.rotation(orientation.zAxis, self.bank)
        pitchMatrix.multiplyMatrix(headingMatrix)
        bankMatrix.multiplyMatrix(pitchMatrix)
        return bankMatrix
    
    def multiplyScalar(self, scalar):
        self.pitch *= scalar
        self.heading *= scalar
        self.bank *= scalar
        return self

    @staticmethod
    def add(eulerA, eulerB):
        return Euler(eulerB.pitch + eulerA.pitch, eulerB.heading + eulerA.heading, eulerB.bank + eulerA.bank)
    @staticmethod
    def difference(eulerA, eulerB):
        return Euler(eulerB.pitch - eulerA.pitch, eulerB.heading - eulerA.heading, eulerB.bank - eulerA.bank)
    @staticmethod
    def lerp(eulerA, eulerB, lerpFactor):
        return Euler.add(eulerA, Euler.difference(eulerA, eulerB).multiplyScalar(lerpFactor))
            
    