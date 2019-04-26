import arcade
import math


class Knife:
    THROWN = False
    STABBED = False
    THROW_VELOCITY = 15
    RADIUS = 5

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0
        self.vangle = 0

    def throw(self):
        self.THROWN = True

    def stab(self):
        self.STABBED = True

    def is_stabbed(self):
        return self.STABBED

    def update(self, delta):
        if self.THROWN and self.STABBED is False:
            self.y += self.THROW_VELOCITY

        if self.STABBED:
            self.x = (Target.RADIUS + self.RADIUS) * math.cos(
                self.vangle - 1.5) + self.world.width // 2
            self.y = (Target.RADIUS + self.RADIUS) * math.sin(
                self.vangle - 1.5) + self.world.height // 2

            self.vangle += 0.08725
            self.angle += Target.TARGET_ANGLE_SPEED

    def hit(self, other):
        return (abs(self.x - other.x) <= self.RADIUS + Target.RADIUS) and (
            abs(self.y - other.y) <= self.RADIUS + Target.RADIUS)


class Target:
    TARGET_ANGLE_SPEED = 5
    RADIUS = 60

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

    def update(self, delta):
        self.angle += Target.TARGET_ANGLE_SPEED


class World:
    STATE_FROZEN = 1
    STATE_STARTED = 2

    def __init__(self, width, height):
        self.state = World.STATE_FROZEN

        self.width = width
        self.height = height

        self.knife = Knife(self, width // 2, height // 5)
        self.knife2 = Knife(self, width // 2, height // 5)
        self.knife3 = Knife(self, width // 2, height // 5)
        self.knife4 = Knife(self, width // 2, height // 5)

        self.target = Target(self, width // 2, height // 2)

    def update(self, delta):

        self.knife.update(delta)

        if self.knife.hit(self.target):
            self.knife.stab()

        self.knife2.update(delta)

        if self.knife2.hit(self.target):
            self.knife2.stab()
        elif self.knife2.hit(self.knife) and self.knife.is_stabbed():
            self.freeze()

        self.knife3.update(delta)

        if self.knife3.hit(self.target):
            self.knife3.stab()
        elif self.knife3.hit(self.knife) and self.knife.is_stabbed():
            self.freeze()
        elif self.knife3.hit(self.knife2) and self.knife2.is_stabbed():
            self.freeze()

        self.knife4.update(delta)

        if self.knife4.hit(self.target):
            self.knife4.stab()
        elif self.knife4.hit(self.knife) and self.knife.is_stabbed():
            self.freeze()
        elif self.knife4.hit(self.knife2) and self.knife2.is_stabbed():
            self.freeze()
        elif self.knife4.hit(self.knife3) and self.knife3.is_stabbed():
            self.freeze()

        self.target.update(delta)

    def start(self):
        self.state = World.STATE_STARTED

    def freeze(self):
        self.state = World.STATE_FROZEN

    def is_started(self):
        return self.state == World.STATE_STARTED

    def is_frozened(self):
        return self.state == World.STATE_FROZEN

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE and self.state == World.STATE_STARTED:
            if self.knife.THROWN is False:
                self.knife.throw()

            elif self.knife2.THROWN is False:
                self.knife2.throw()

            elif self.knife3.THROWN is False:
                self.knife3.throw()

            elif self.knife4.THROWN is False:
                self.knife4.throw()

    def on_mouse_press(self, x, y, button, modifiers):
        if self.state == World.STATE_STARTED:
            if self.knife.THROWN is False:
                self.knife.throw()

            elif self.knife2.THROWN is False:
                self.knife2.throw()

            elif self.knife3.THROWN is False:
                self.knife3.throw()

            elif self.knife4.THROWN is False:
                self.knife4.throw()
