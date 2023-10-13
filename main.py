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
from graphic.meshes.HoverableCubeMesh import HoverableCubeMesh
from graphic.meshes.Mesh import Mesh
from geom.Vector3 import Vector3
from light.DirectionalLight import DirectionalLight
from rotation.Quaternion import Quaternion
from rotation.RotationAnimation import RotationAnimation


pygame.init()
width = 1000
height = 1000
canva = pygame.display.set_mode((width, height))
background = (0, 0, 0)
canva.fill(background)
font = pygame.font.Font(None, 24)  # Utilisation de la police par défaut de Pygame

scene = Scene()
# camera = PerspectiveCamera(100,width/height)
camera = OrthographicCamera(-5,5,5,-5,0.1,1000).setPosition(Vector3(1,1,1)).lookAt(Vector3(0,0,0))
renderer = Renderer(canva, width, height)

# DEBUG
debug = GUI(canva)
scene.debug = debug

# CUBE
cube = HoverableCubeMesh(2,2,2, solid=True)
scene.add(cube)
axesHelper = AxesHelper()
scene.add(axesHelper)

# LIGHT
light = DirectionalLight(Vector3(1,1,-1))
scene.light = light

rotate = RotationAnimation(cube)


debug.addButton("Slerp", lambda: rotate.animateRotationOf(1000, Quaternion.fromAxisAngle(Vector3(1,0.75,0), pi/3)))
debug.addButton("showCameraParams", lambda: print("\n\n\tcamera orientation: \n", camera.cameraMatrix.getOrientation(),
                                                  "\n\n\tcamera position: \n", camera.cameraMatrix.getPosition(),
                                                  "\n\nmerci\n\n"))

def tick():
    speed = 0.3
    clock = pygame.time.Clock()
    framerate=60
    lastTime = pygame.time.get_ticks()
    while True:
        clock.tick(framerate)
        currentTime = pygame.time.get_ticks()
        elapsedTime = currentTime - lastTime
        lastTime = currentTime
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            debug.eventHandler(event)
            cube.eventHandler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cube.applyRotation(Vector3.y(), -speed)
                if event.key == pygame.K_RIGHT:
                    cube.applyRotation(Vector3.y(), speed)
                if event.key == pygame.K_UP:
                    cube.applyRotation(Vector3.x(), speed)
                if event.key == pygame.K_DOWN:
                    cube.applyRotation(Vector3.x(), -speed)
                    
                if event.key == pygame.K_KP_PLUS:
                    cube.applyScale(1.1)
                if event.key == pygame.K_KP_MINUS:
                    cube.applyScale(0.9)

                if event.key == pygame.K_KP_4:
                    cube.applyTranslation(Vector3.x().multiplyScalar(-speed))
                if event.key == pygame.K_KP_6:
                    cube.applyTranslation(Vector3.x().multiplyScalar(speed))
                if event.key == pygame.K_KP_2:
                    cube.applyTranslation(Vector3.y().multiplyScalar(-speed))
                if event.key == pygame.K_KP_8:
                    cube.applyTranslation(Vector3.y().multiplyScalar(speed))

                if event.key == pygame.K_x: # X view
                    camera.setPosition(Vector3.x()).lookAt()
                if event.key == pygame.K_y: # Y view
                    camera.setPosition(Vector3.y()).lookAt()
                if event.key == pygame.K_z: # Z view
                    camera.setPosition(Vector3.z()).lookAt()
                if event.key == pygame.K_h: # Hybrid view
                    camera.setPosition(Vector3(1,1,1)).lookAt()

        if (rotate.isActive):
            rotate.update(elapsedTime)
            
   
        canva.fill(background)
        renderer.render(scene, camera)
        pygame.display.flip()

tick()
