import sys

import pygame
import requests

first_coord = float(input("Первая координата (float):"))
second_coord = float(input("Вторая координата (float):"))
first_scale = 25.0
second_scale = 25.0
map_file = "map.png"


def fun():
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={first_coord},{second_coord}&spn={first_scale},{second_scale}&l=sat"
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
            if event.key == pygame.K_PAGEUP:
                if first_scale >= 10.0 and first_scale >= 10.0:
                    first_scale -= 5.0
                    second_scale -= 5.0
                    print(first_scale, second_scale)
                    fun()

            if event.key == pygame.K_PAGEDOWN:
                if first_scale <= 90.0 and first_scale <= 90.0:
                    first_scale += 5.0
                    second_scale += 5.0
                    print(first_scale, second_scale)
                    fun()
    pygame.display.flip()

pygame.quit()
