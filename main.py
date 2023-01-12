import time

import pgzrun
from pgzero.actor import Actor

ball_x_speed = 3
ball_y_speed = 3


class Paddle:

    def __init__(self):
        self.actor = Actor('i.png', center=(300, 765))
        self.position = Vector(300, 765)
        self.center = Vector(62, 765)

    def draw(self):
        self.actor.draw()

    def update(self, pos):
        mouse_x = pos[0]
        if mouse_x < self.center.x:
            mouse_x = self.center.x
        if mouse_x > WIDTH - self.center.x:
            mouse_x = WIDTH - self.center.x
        self.position = Vector(mouse_x, self.position.y)
        self.actor.x = self.position.x


class Background:

    def __init__(self):
        self.actor = Actor('bg.jpg', center=(300, 400))

    def draw(self):
        self.actor.draw()


class Ball:

    def __init__(self):
        self.position = Vector(265, 630)
        self.velocity = Vector(0, 0)  # speed- scalar, velocity - vector
        self.goal = Vector(pad.position.x, pad.position.y)

    def draw(self):
        screen.draw.filled_circle((self.position.x, self.position.y), 13, "indigo")

    def update(self):
        global ball_x_speed, ball_y_speed
        self.position.x += ball_x_speed
        self.position.y += ball_y_speed
        if (self.position.x >= WIDTH) or (self.position.x <= 0):
            ball_x_speed *= -1
        if self.position.y <= 0:
            ball_y_speed *= -1
        if self.position.y >= pad.position.y - 5:
            if pad.position.x - 62 < self.position.x < pad.position.x + 62:
                ball_x_speed *= -1
                ball_y_speed *= -1
            else:
                time.sleep(2)
                self.position = Vector(265, 700)


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, 0)

    def __sub__(self, other):
        return Vector(self.x - other.x, 0)


WIDTH = 600
HEIGHT = 800

pad = Paddle()
bg = Background()
bb = Ball()


def draw():
    screen.clear()
    bg.draw()
    pad.draw()
    bb.draw()


def update(dt):
    bb.update()


def on_mouse_move(pos):
    pad.update(pos)


pgzrun.go()
