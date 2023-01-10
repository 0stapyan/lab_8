import pgzrun
from pgzero.actor import Actor


class Paddle:

    def __init__(self):
        self.actor = Actor('i.png', center=(300, 765))

    def draw(self):
        self.actor.draw()


class Background:
    def __init__(self):
        self.actor = Actor('bg.jpg', center=(300, 400))

    def draw(self):
        self.actor.draw()


WIDTH = 600
HEIGHT = 800

pad = Paddle()
bg = Background()


def draw():
    bg.draw()
    pad.draw()


def update(dt):
    pass


pgzrun.go()
