import pgzrun
from pgzero.actor import Actor


class Paddle:

    def __init__(self):
        self.actor = Actor('i.png', center=(300, 765))
        self.position = Vector(300, 765)

    def draw(self):
        self.actor.draw()

    def update(self, pos):
        self.position = Vector(pos[0], self.position.y)
        self.actor.x = self.position.x


class Background:

    def __init__(self):
        self.actor = Actor('bg.jpg', center=(300, 400))

    def draw(self):
        self.actor.draw()


class Ball:

    def __init__(self):
        self.position = Vector(265, 700)
        self.velocity = Vector(0, 0)  # speed- scalar, velocity - vector
        self.acceleration = Vector(0, 0)

    def draw(self):
        screen.draw.filled_circle((self.position.x, self.position.y), 13, "indigo")

    def update(self):
        pass


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
    pass


def on_mouse_move(pos):
    pad.update(pos)


pgzrun.go()
