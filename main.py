from asyncio import get_event_loop
from math import pi
import sys
import pygame
from debug.GUI import GUI
from graphic.Camera import OrthographicCamera
from geom.MathMatrix4 import MathMatrix4
from graphic.Renderer import Renderer
from graphic.Scene import Scene
from graphic.meshes.CubeMesh import CubeMesh
from graphic.meshes.Mesh import Mesh
from geom.Vector3 import Vector3
from rotation.Quaternion import Quaternion


pygame.init()
width = 1000
height = 1000
canva = pygame.display.set_mode((width, height))
background = (0, 0, 0)
canva.fill(background)
font = pygame.font.Font(None, 24)  # Utilisation de la police par défaut de Pygame

scene = Scene()
cube = CubeMesh(2,2,2)

debug = GUI(canva)
scene.add(cube)
camera = OrthographicCamera(-4,4,4,-4,0.1,1000)
renderer = Renderer(canva, width, height)

speed = 0.1

# def animateRotation():
#     print("start")
#     cube.animateRotationTo(1000, Quaternion.fromAxisAngle(Vector3(1,0.75,0), 2*pi/3))



# debug.addButton("Slerp", animateRotation)


async def tick():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cube.applyRotation(Vector3(0,1,0), speed)
                if event.key == pygame.K_RIGHT:
                    cube.applyRotation(Vector3(0,1,0), -speed)
                if event.key == pygame.K_UP:
                    cube.applyRotation(Vector3(1,0,0), -speed)
                if event.key == pygame.K_DOWN:
                    cube.applyRotation(Vector3(1,0,0), speed)
                    
                if event.key == pygame.K_KP_PLUS:
                    cube.applyScale(1.1)
                if event.key == pygame.K_KP_MINUS:
                    cube.applyScale(0.9)

                if event.key == pygame.K_KP_4:
                    cube.applyTranslation(Vector3(-speed,0,0))
                if event.key == pygame.K_KP_6:
                    cube.applyTranslation(Vector3(speed,0,0))
                if event.key == pygame.K_KP_2:
                    cube.applyTranslation(Vector3(0,speed,0))
                if event.key == pygame.K_KP_8:
                    cube.applyTranslation(Vector3(0,-speed,0))

                if event.key == pygame.K_s:
                    pass
                
        
   
        canva.fill(background)
        renderer.render(scene, camera)
        debug.draw()
        pygame.display.flip()

if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(tick())
