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
        #CREATE BACKGROUND
        self.bgImg=pygame.image.loaf('track11.png')
        self.bg_x1=(self.display_width / 2) - (360 / 2)
        self.bg_x2=(self.display_width / 2) -(360 /2)
        self.bg_y1= 0
        self.bg_y2= -600
        self.bg_speed= 3
        self.count= 0

    def car(self, car_x_coordinate, car_y_coordinate):
        self.gameDisplay.blit(self.carImg, (car_x_coordinate, car_y_coordinate))
    def racing_window(self):
        pygame.display.set_caption('CAR RACING')
        self.run_car()
     #DECLARED FUNTION FOR RUN CAR
    def run_car(self):
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed=True
                    ## if keystroke is pressed whether its right or left
                    if(event.type== pygame.KEYDOWN):
                        if(event.key==pygame.K_LEFT):
                            self.car_x_coordinate -=50
                        if(event.key==pygame.K_RIGHT):
                            self.car_x_coordinate +=50
            self.gameDisplay.fill(self.black)
            self.back_ground_road()
            self.run_enemy_car(self.enemy_car_startx,self.enemy_car_starty)
            self.enemy_car_starty +=self.enemy_car_speed

            if self.enemy_car_starty >self.display.height:
                self.enemy_car_starty= 0-self.enemy_car_height
                self.enemy_car_startx = random.randrange(310,450)

            self.car(self.car_x_coordinate, self.car_y_coordinate)
            self.highscore(self.count)
            self.count +=1
            if (self.count % 100==0):
                self.enemy_car_speed +=1
                self.bg_speed +=1
            if self.car_y_coordinate <self.enemy_car_starty + self.enemy_car_height:
                if self.car_x_coordinate > self.enemy_car_startx and self.car_x_coordinate < self.enemy_car_startx+self.enemy_car_width or self.car_x_coordinate + self.car_width
                    self.crashed=True
                    self.display_message("GAME OVER !!!")

                if self.car_x_coordinate <310 or self.car_x_coordinate >460:
                    self.crashed = True
                    self.display_messagw("GAME  OVER!!!")

                pygame.display.update()
                self.clock.tick(60)

