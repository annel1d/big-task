import sys

import pygame
from pygame import font
import requests

first_coord = float(input("Первая координата (float):"))
second_coord = float(input("Вторая координата (float):"))
z = 10
a = 'sat'
map_file = "map.png"


def fun():
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={first_coord},{second_coord}&z={z}&l={a}"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))


pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 450))
font = pygame.font.SysFont('Arial', 20)

objects = []


class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, eee=None, onePress=False):
        self.x = x
        self.y = y
        self.eee = eee
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()
                    self.eee()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.eee()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


def sput():
    global a
    print('Спутник!')
    a = 'sat'


def shema():
    global a
    print('Схема!')
    a = 'map'


def hybrid():
    global a
    print('Гибрид!')
    a = 'sat,skl'


customButton = Button(30, 30, 100, 100, '1. Схема', shema, fun)
customButton = Button(30, 140, 100, 100, '2. Спутник', sput, fun)
customButton = Button(30, 250, 100, 100, '3. Гибрид', hybrid, fun)
fun()
running = True

while running:
    screen.blit(pygame.image.load(map_file), (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_PAGEDOWN:
                if z > 1:
                    z -= 1
                    print(z)
                    fun()

            if event.key == pygame.K_PAGEUP:
                if z < 13:
                    z += 1
                    print(z)
                    fun()

            ####################################

            if event.key == pygame.K_UP:
                if 85.0 > second_coord >= -85.0:
                    second_coord += 1.0
                    print(second_coord)
                    fun()

            if event.key == pygame.K_DOWN:
                if 85.0 >= second_coord > -85.0:
                    second_coord -= 1.0
                    print(second_coord)
                    fun()

            ######################################

            if event.key == pygame.K_RIGHT:
                if 175.0 > first_coord >= -175.0:
                    first_coord += 1.0
                    print(first_coord)
                    fun()

            if event.key == pygame.K_LEFT:
                if 175.0 >= first_coord > -175.0:
                    first_coord -= 1.0
                    print(first_coord)
                    fun()

            ######################################

    for object in objects:
        object.process()

    pygame.display.flip()

pygame.quit()
