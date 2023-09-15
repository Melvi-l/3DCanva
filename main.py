import sys
import pygame
from Camera import OrthographicCamera
from Matrix4 import Matrix4
from Renderer import Renderer
from Scene import Scene
from TriangleMesh import TriangleMesh
from Vector3 import Vector3


pygame.init()
width = 1000
height = 1000
canva = pygame.display.set_mode((width, height))
background = (0, 0, 0)
canva.fill(background)
font = pygame.font.Font(None, 24)  # Utilisation de la police par défaut de Pygame

scene = Scene()
cube = TriangleMesh([
    Vector3(-1,-1,-1),
    Vector3(-1,-1,1),
    Vector3(-1,1,-1),
    Vector3(-1,1,1),
    Vector3(1,-1,-1),
    Vector3(1,-1,1),
    Vector3(1,1,-1),
    Vector3(1,1,1),
    ],
    [
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
    ]
)

scene.add(cube)
camera = OrthographicCamera(-4,4,4,-4,0.1,1000)
renderer = Renderer(canva, width, height)
v=Vector3(1,0,0)
renderer.getDrawPosition(v, Matrix4.identity(), camera.projectionMatrix)
speed = 0.1
def tick():
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
                
                
        canva.fill(background)
        renderer.render(scene, camera)
        pygame.display.flip()
tick()
