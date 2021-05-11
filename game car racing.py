import pygame
import time
import random
from time import sleep
class CarRacing:
    def __init__(self):
        #INITIALIZING PYGAME
        pygame.init()
        #CREATING THE SCREEN
        self.display_width=800
        self.display_height=600
        self.black=(0,0,0)
        self.white=(255,255,255)
        self.clock=pygame.time.clock()
        self.gameDisplay=None

        self.initialize()

    def initialize(self):
        self.crashed = False
        #ADDING PLAYER

        self.carImg= pygame.image.load('racingcar1.png')
        #passing x and y co-ordinate for car
        self.car_x_coordinate=(self.display_width*0.45)
        self.car_y_coordinate=(self.display_height*0.8)
        self.car_width = 49

        #ADDING ENEMY
        self.enemy_car=pygame.image.load('enemy.png')
        self.enemy_car_startx=random.randrange(310,450)
        self.enemy_car_starty=-600
        self.enemy_car_speed=5
        self.enemy_car_width=49
        self.enemy_car_height=100
