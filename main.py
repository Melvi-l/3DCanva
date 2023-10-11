from asyncio import get_event_loop
from math import pi
import sys
from threading import Thread
import pygame
from debug.AxesHelper import AxesHelper
from debug.GUI import GUI
from geom.Matrix import Matrix
from graphic.Camera.OrthographicCamera import OrthographicCamera
from geom.MathMatrix4 import MathMatrix4
from graphic.Camera.PerspectiveCamera import PerspectiveCamera
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
camera = PerspectiveCamera(45,width/height)
# camera = OrthographicCamera(-5,5,5,-5,0.1,1000)
renderer = Renderer(canva, width, height)

# DEBUG
debug = GUI(canva)
scene.debug = debug

# CUBE
cube = CubeMesh(2,2,2)
scene.add(cube)
# axesHelper = AxesHelper()
# scene.add(axesHelper)


# def animateRotation(cube):
#     thread = Thread(target=animateRotation, args=(cube,))
#     cube.animateRotationTo(1000, Quaternion.fromAxisAngle(Vector3(1,0.75,0), 2*pi/3))
#     thread.start()


# debug.addButton("Slerp", lambda: animateRotation(cube))


matrix = Matrix(
    0, 0, 1, 0,
    0, 1, 0, 0,
    -1, 0, 0, 0,
    0, 0, -5, 1
)

inv = matrix.getInverse()

Matrix.multiply

def tick():
    speed = 0.3
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            debug.eventHandler(event)
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

   
        canva.fill(background)
        renderer.render(scene, camera)
        pygame.display.flip()

tick()
