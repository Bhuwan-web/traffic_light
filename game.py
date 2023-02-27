"""
    Traffic light visualization in python
"""
import sys
import pygame
import schedule
pygame.init()

size = width, height = 1500, 800
speed = [2, 0]
screen = pygame.display.set_mode(size)
# load images
background = pygame.image.load("background.jpg")
car = pygame.image.load("car.png")
traffic_red = pygame.image.load("red.png")
traffic_green = pygame.image.load("green.png")
traffic_yellow = pygame.image.load("yellow.png")
# transform images
car = pygame.transform.scale(car, (width*0.3, height*0.4))
background = pygame.transform.scale(background, size)
car_rect = car.get_rect(x=0, y=300)
traffic_red = pygame.transform.scale(traffic_red, (width*0.1, height*0.4))
traffic_green = pygame.transform.scale(traffic_green, (width*0.1, height*0.4))
traffic_yellow = pygame.transform.scale(
    traffic_yellow, (width*0.1, height*0.4))

traffics = [traffic_red, traffic_yellow, traffic_green]


class Traffic:
    active = traffic_green
    step = 1

    @classmethod
    def change_traffic(cls):
        index = traffics.index(cls.active)
        if index == len(traffics)-1:
            cls.step = -cls.step
            cls.active = traffics[index+cls.step]
        elif index == 0:
            cls.step = -cls.step
            cls.active = traffics[index+cls.step]
        else:
            cls.active = traffics[index+cls.step]
        return


change_traffic = Traffic().change_traffic

schedule.every(2).seconds.do(change_traffic)


while True:
    schedule.run_pending()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if not Traffic.active in [traffic_red, traffic_yellow] or car_rect.x < width*0.5 or car_rect.x > width*0.7:
        car_rect = car_rect.move(speed)
    if car_rect.x >= width:
        car_rect.x = 0
    screen.blit(background, (0, 0))
    screen.blit(Traffic.active, (width*0.85, height*0.1))
    screen.blit(car, car_rect)
    pygame.display.update()
