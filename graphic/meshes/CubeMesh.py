import pygame
from geom.Vector3 import Vector3
from graphic.meshes.Mesh import Mesh
from rotation.Quaternion import Quaternion


class CubeMesh(Mesh):
    def __init__(self, width, height, depth, solid) -> None:
        super().__init__([
            Vector3(-width/2,-height/2,-depth/2),
            Vector3(-width/2,-height/2,depth/2),
            Vector3(-width/2,height/2,-depth/2),
            Vector3(-width/2,height/2,depth/2),
            Vector3(width/2,-height/2,-depth/2),
            Vector3(width/2,-height/2,depth/2),
            Vector3(width/2,height/2,-depth/2),
            Vector3(width/2,height/2,depth/2),
        ],[
                [0,1,2],
                [1,3,2],
                [2,3,7],
                [2,7,6],
                [1,7,3],
                [1,5,7],
                [4,6,7],
                [4,7,5],
                [0,5,1],
                [0,4,5],
                [0,2,6],
                [0,6,4]
        ], solid)

    # def animateRotationTo(self, duration, endQuaternion):
    #     clock = pygame.time.Clock()        
    #     startQuaternion = self.getQuaternion()
    #     startTime = pygame.time.get_ticks()
    #     print("start", startQuaternion)
    #     print("end", endQuaternion)
    #     while True: 
    #         elapsedTime = pygame.time.get_ticks() - startTime
    #         if  elapsedTime > duration:
    #             break
    #         lerpFactor = elapsedTime / duration
    #         currentQuaternion = Quaternion.slerp(startQuaternion, endQuaternion, lerpFactor)
    #         if elapsedTime % 100 == 0:
    #             print(lerpFactor, currentQuaternion)
    #         self.setQuaternion(currentQuaternion)
    def animateRotationTo(self, duration, euler):
        clock = pygame.time.Clock()        
        startQuaternion = self.getQuaternion()
        startTime = pygame.time.get_ticks()
        print("start", startQuaternion)
        print("end", euler)
        while True: 
            elapsedTime = pygame.time.get_ticks() - startTime
            if  elapsedTime > duration:
                break
            lerpFactor = elapsedTime / duration
            currentQuaternion = Quaternion.slerp(startQuaternion, euler, lerpFactor)
            if elapsedTime % 100 == 0:
                print(lerpFactor, currentQuaternion)
            self.setQuaternion(currentQuaternion)