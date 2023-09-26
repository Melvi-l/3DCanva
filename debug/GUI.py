import pygame

from color import RED, YELLOW

WHITE = (255,255,255)

class GUI:
    def __init__(self, screen, position="top-right"):
        self.position = position
        self.screen = screen
        self.initPosition()
        self.elementList = []
        self.clock = pygame.time.Clock()

    def initPosition(self):
        # cst
        self.width = 128
        self.height = 48
        self.gap = 10
        self.margin = 50
        # var
        self.top = 0 
        self.left = 0
    def setDimension(self):
        if "top" in self.position:
            self.top = self.margin
        if "bottom" in self.position:
            self.top = self.screen.get_height() - self.margin - self.height*len(self.elementList) - self.gap*(len(self.elementList)-1)
        if "left" in self.position:
            self.left = self.margin
        if "right" in self.position:
            self.left = self.screen.get_width() - self.margin - self.width
        
    def addButton(self, label, action, color=(100,100,100)):
        self.elementList.append(DebugElement("button", label, action, color))
        self.setDimension()
    def draw(self):
        self.drawFpsText()
        for index in range(len(self.elementList)):
            self.elementList[index].draw(self.screen, self.left, self.top + self.height*index + self.gap*(index-1), self.width, self.height)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for element in self.elementList:
                    if element.button.collidepoint(event.pos):
                        element.action()
    def drawFpsText(self):
        self.clock.tick(60)
        current_fps = self.clock.get_fps()
        text = pygame.font.Font("C:\Windows\Fonts\8514fix.fon", 24).render(f"{'{:.2f}'.format(current_fps)} FPS", True, YELLOW)
        self.screen.blit(text, (10, 10))
            


class DebugElement:
    def __init__(self, category, label, action, color):
        self.category = category
        font = pygame.font.Font("C:\Windows\Fonts\8514fix.fon", 32)
        self.textSurface = font.render(label, True, tuple([min(i + 100,255) for i in color]))
        self.action = action
        self.color = color
        self.fadeColor = tuple([max(i - 100,10) for i in color])
        self.button = None
    def draw(self, screen, left, top, width, height):
        self.button = pygame.Rect(left, top, width, height) 
        self.text = self.textSurface.get_rect(center=self.button.center)
        pygame.draw.rect(screen, self.fadeColor, self.button, border_radius=5)
        pygame.draw.rect(screen, self.color, self.button, width=3, border_radius=5)
        screen.blit(self.textSurface, self.text)



        