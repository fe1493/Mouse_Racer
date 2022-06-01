import math
import pygame
import random

COLLISION_SIZE = 112
X_BORDER = 800
Y_BORDER = 600
SIZE = 128
ADJUSTED_SIZE = 120
'''Abstract Element Class'''


class AbstractElement:
    def __init__(self,name,  type, size, speed, win, game_info, move_x=0, move_y=0, ):
        self.name = name
        self.type = type
        self.size = size
        self.speed = speed
        self.win = win
        self.x = random.randint(150, 650)
        self.y = random.randint(150, 450)
        self.move_x = move_x
        self.move_y = move_y
        self.game_info = game_info
        self.angle = 0

    '''Calculate the angle based on the element'''
    def get_angle(self, dx, dy):
        if self.name == "Chase":
            self.angle = math.atan2(dx, dy)
        else:
            self.angle = math.atan2(dy, dx)


    '''Draw the element'''

    def draw_element(self):
        self.win.blit(self.type, (self.x, self.y))

    '''Bounce off the border and continue- For Random Element'''

    def bounce(self):
        self.speed = -self.speed

    '''Check if the mouse collided with an object'''

    def check_for_collision(self, mx, my):
        if (self.x <= mx <= self.x + COLLISION_SIZE) and (self.y <= my <= self.y + COLLISION_SIZE) and\
                (mx != 0) and (my != 0):
            self.on_hit_target()


    '''Move the elements each on there requested direction'''

    def move_direction(self):
        # get the mouse pos
        mx, my = pygame.mouse.get_pos()
        # calculate the route
        self.calculate_route()
        # watch for the borders
        self.watch_border()
        # move according to what we calculated in the previous functions
        self.x += self.move_x
        self.y += self.move_y
        # check if our mouse collided with an element
        self.check_for_collision(mx, my)

    '''Ensures that the sub classes implement these functions'''

    def calculate_route(self):
        # get the mouse position
        mx, my = pygame.mouse.get_pos()
        # calculate the slope
        dx = mx - self.x
        dy = my - self.y
        # get the angle based on the slope
        self.get_angle(dx, dy)
        # move according to the angle
        self.move_x = math.sin(self.angle)
        self.move_y = math.cos(self.angle)

    '''Each element has its own calculation because they are different sizes'''
    def watch_border(self):
        pass

    '''On hit is the same for the random and chase elements'''

    def on_hit_target(self):
        self.game_info.end_game()


'''Chase Element Class'''


class Chase(AbstractElement):
    def __init__(self,name, type, size, speed, win, game_info):
        self.name = name
        self.move_x = 0
        self.move_y = 0
        super().__init__(self.name, type, size, speed, win, game_info, self.move_x, self.move_y)

    """ Calculate the border"""

    def watch_border(self):
        # adjustments if we hit the border
        if self.x + SIZE >= X_BORDER:
            self.x = 672
        elif self.x <= 0:
            self.x = 0
        elif self.y + ADJUSTED_SIZE >= Y_BORDER:
            self.y = 479
        elif self.y <= 0:
            self.y = 50


'''Escape Element Class'''


class Escape(AbstractElement):
    def __init__(self,name, type, size, speed, win, game_info):
        self.name = name
        self.move_x = 0
        self.move_y = 0
        super().__init__(self.name, type, size, speed, win, game_info, self.move_x, self.move_y)

    """ Calculate the border"""

    def watch_border(self):
        # adjustments if we hit the border
        if self.x + ADJUSTED_SIZE >= X_BORDER:
            self.x = 672
        elif self.x + 5 <= 0:
            self.x = 50
        elif self.y + ADJUSTED_SIZE >= Y_BORDER:
            self.y = 450
        elif self.y + 5 <= 0:
            self.y = 20

    '''Special implementation of the on_hit_target function for the escape element '''

    def on_hit_target(self):
        # update the score by 5
        self.game_info.special_update_score()
        # jump to a random spot
        self.x = random.randint(150, 650)
        self.y = random.randint(150, 450)


'''Random Element Class'''


class Random(AbstractElement):
    def __init__(self, name, type, size, speed, win, game_info):
        self.name = name
        super().__init__(self.name, type, size, speed, win, game_info)

    '''Calculate the route - Separate from the other two elements because the route calculation is different'''

    def calculate_route(self):
        self.x = self.x + self.speed
        if self.x + SIZE >= X_BORDER or self.x <= 0:
            # if we hit the border bounce off it
            self.bounce()
            # and continue moving
            self.move_direction()
