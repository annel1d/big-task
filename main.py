import sys

import pygame
import requests

first_coord = float(input("Первая координата (float):"))
second_coord = float(input("Вторая координата (float):"))
z = 10
map_file = "map.png"


def fun():
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={first_coord},{second_coord}&z={z}&l=sat"
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
screen = pygame.display.set_mode((600, 450))
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

    pygame.display.flip()

pygame.quit()