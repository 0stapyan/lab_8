import random
import time

import pgzrun
import pygame
from pgzero.actor import Actor


class Paddle:

    def __init__(self):
        self.actor1 = Actor("i.png", center=(300, 765))
        self.actor2 = Actor("i2.png", center=(300, 765))
        self.position = Vector(300, 765)
        self.center = Vector(62, 765)

    def draw(self):
        if bns == 1:
            self.actor2.draw()
        else:
            self.actor1.draw()
        screen.draw.filled_rect(pygame.Rect((0, 0, 600, 60)), "thistle")
        screen.draw.line((0, 60), (600, 60), "indigo")

    def update(self, pos):
        if bns == 1:
            self.actor1.x = self.position.x
        else:
            self.actor2.x = self.position.x
        mouse_x = pos[0]
        if mouse_x < self.center.x:
            mouse_x = self.center.x
        if mouse_x > WIDTH - self.center.x:
            mouse_x = WIDTH - self.center.x
        self.position = Vector(mouse_x, self.position.y)
        if bns > 0:
            self.actor2.x = self.position.x
        else:
            self.actor1.x = self.position.x


class Background:

    def __init__(self):
        self.actor = Actor('bg.jpg', center=(300, 400))

    def draw(self):
        self.actor.draw()


class Ball:

    def __init__(self):
        self.position = Vector(265, 469)
        self.velocity = Vector(0, 0)  # speed- scalar, velocity - vector
        self.goal = Vector(pad.position.x, pad.position.y)
        self.ball_x_speed = 6
        self.ball_y_speed = 6
        self.tries = 3
        self.land = 0

    def draw(self):
        screen.draw.filled_circle((self.position.x, self.position.y), 13, "indigo")

    def update(self):
        if bns == 0:
            self.land = 93
        else:
            self.land = 62
        self.position.x += self.ball_x_speed
        self.position.y += self.ball_y_speed
        if (self.position.x >= WIDTH) or (self.position.x <= 0):
            self.ball_x_speed *= -1
        if self.position.y <= 66:
            self.ball_y_speed *= -1
        if self.position.y >= pad.position.y - 5:
            if pad.position.x - self.land < self.position.x < pad.position.x + self.land:
                # ball_x_speed *= -1
                self.ball_y_speed *= -1
            else:
                if self.tries > 0:
                    self.tries -= 1
                    time.sleep(0.1)
                    self.position = Vector(265, 469)
                else:
                    time.sleep(2)
                    self.position = Vector(265, 469)


class Health:

    def __init__(self, x):
        self.actor = Actor('health.png', center=(x, 30))
        self.position = Vector(x, 30)

    def draw(self):
        self.actor.x = self.position.x + 25
        self.actor.y = self.position.y
        self.actor.draw()


class Blocks1:

    def __init__(self, x, y):
        self.position = Vector(x, y)

    def draw(self):
        screen.draw.filled_circle((self.position.x, self.position.y), 18, "midnightblue")

    def update(self):
        pass


class Blocks2:

    def __init__(self, x, y):
        self.position = Vector(x, y)

    def draw(self):
        screen.draw.filled_circle((self.position.x, self.position.y), 18, "crimson")

    def update(self):
        pass


class Blocks3:

    def __init__(self, x, y):
        self.position = Vector(x, y)

    def draw(self):
        screen.draw.filled_rect(pygame.Rect((self.position.x, self.position.y, 84, 28)), "midnightblue")  # x = 25 y = 261

    def update(self):
        pass


class AddHealth:

    def __init__(self, pos):
        self.actor = Actor('he1.png')
        self.position = pos
        self.velocity = Vector(0, 100)

    def move(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def draw(self):
        self.actor.x = self.position.x
        self.actor.y = self.position.y
        self.actor.draw()


class AddBonus:

    def __init__(self, pos):
        self.actor = Actor('bonus.png')
        self.position = pos
        self.velocity = Vector(0, 100)
        self.bonus_catch = 0
        self.current_time = 0

    def move(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def draw(self):
        self.actor.x = self.position.x
        self.actor.y = self.position.y
        self.actor.draw()


class Finish:

    def __init__(self):
        self.actor = Actor('finish.png', center=(300, 400))

    def draw(self):
        self.actor.draw()


class Winmessage:
    def __init__(self):
        self.actor = Actor('win.png', center= (300, 400))

    def draw(self):
        self.actor.draw()


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
points = 0

pad = Paddle()
bg = Background()
bb = Ball()
b1 = [Blocks1(x*45+45, y*45) for x in range(12) for y in range(3, 6, 2)]
b2 = [Blocks2(x*45+45, y*45) for x in range(12) for y in range(4, 5)]
b3 = [Blocks3((x+1)*27+85*x, y*45) for x in range(5) for y in range(6, 9)]
fin = Finish()
win = Winmessage()
new_health = []
d = {}
for obj in b2:
    d[obj] = 0
bonuses = []
bns = 0
start = 0


def draw():
    screen.clear()
    bg.draw()
    pad.draw()
    hh = [Health(x*45) for x in range(0, bb.tries)]
    screen.draw.text(f"points: {points}", (459, 20), color=(0, 0, 200))
    [x.draw() for x in hh]
    bb.draw()
    [x.draw() for x in b1]
    [x.draw() for x in b2]
    [x.draw() for x in b3]
    [h.draw() for h in new_health]
    [bn.draw() for bn in bonuses]
    if bb.tries == 0:
        screen.clear()
        bg.draw()
        fin.draw()
    if len(b1) == 0 and len(b2) == 0:
        screen.clear()
        bg.draw()
        win.draw()


def update(dt):
    global bns, start, points
    bb.update()
    for obs in b1:
        if (obs.position.x - 18 < bb.position.x < obs.position.x + 18) \
                and (obs.position.y - 18 < bb.position.y < obs.position.y + 18):
            b1.remove(obs)
            points += 1
            bb.ball_y_speed *= -1
            rand = random.randint(0, 1)
            if rand:
                bb.ball_x_speed *= -1

    for i in b2:
        if (i.position.x - 18 < bb.position.x < i.position.x + 18) \
                and (i.position.y - 18 < bb.position.y < i.position.y + 18):
            d[i] += 1
            if d[i] == 2:
                b2.remove(i)
                points += 1
            bb.ball_y_speed *= -1
            rand = random.randint(0, 1)
            if rand:
                bb.ball_x_speed *= -1

    for p in b3:
        if (p.position.x < bb.position.x < p.position.x + 83) \
                and (p.position.y < bb.position.y < p.position.y + 15):
            # print("="*50)
            b3.remove(p)
            points += 1
            bb.ball_y_speed *= -1
        if (bb.position.x == p.position.x or bb.position.x == p.position.x + 83) \
                and (bb.position.y < p.position.y + 15):
            b3.remove(p)
            points += 1
            bb.ball_x_speed *= -1
            # rand = random.randint(0, 1)
            # if rand:
            #     bb.ball_x_speed *= -1

    if random.random() < 0.001:
        ah = AddHealth(Vector(random.randint(0, WIDTH), 55))
        new_health.append(ah)
    for h in new_health:
        h.move(dt)
        if 800 >= h.position.y >= 763:
            if pad.position.x - bb.land < h.position.x < pad.position.x + bb.land:
                if bb.tries < 3:
                    bb.tries += 1
                    new_health.remove(h)
                else:
                    continue

    if random.random() < 0.001:
        bnn = AddBonus(Vector(random.randint(0, WIDTH), 55))
        bonuses.append(bnn)
    for bn in bonuses:
        bn.move(dt)
        if bns == 0:
            if 800 >= bn.position.y >= 763:
                if pad.position.x - bb.land < bn.position.x < pad.position.x + bb.land:
                    bns = 1
                    start = pygame.time.get_ticks()
                    bonuses.remove(bn)
    if (pygame.time.get_ticks() - start)/1000 > 4:
        bns = 0


def on_mouse_move(pos):
    pad.update(pos)


pgzrun.go()
