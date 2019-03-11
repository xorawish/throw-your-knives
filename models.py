import arcade
import math

class Knife:
    THROWN = False
    STABBED = False
    THROW_VELOCITY = 15
    RADIUS = 15

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

    def update(self, delta):
        if self.THROWN and self.STABBED is False:
            self.y += self.THROW_VELOCITY

        if self.STABBED:
            self.x = (Target.RADIUS + self.RADIUS) * math.cos(self.vangle - 1.5) + self.world.width // 2
            self.y = (Target.RADIUS + self.RADIUS) * math.sin(self.vangle - 1.5) + self.world.height // 2

            self.vangle += 0.087
            self.angle += Target.TARGET_ANGLE_SPEED

    def hit(self, other):
        return (abs(self.x - other.x) <= self.RADIUS + Target.RADIUS) and (abs(self.y - other.y) <= self.RADIUS + Target.RADIUS)

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
    def __init__(self, width, height):
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

        self.knife3.update(delta)

        if self.knife3.hit(self.target):
            self.knife3.stab()

        self.knife4.update(delta)

        if self.knife4.hit(self.target):
            self.knife4.stab()

        self.target.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            if self.knife.THROWN is False:
                self.knife.throw()

            elif self.knife2.THROWN is False:
                self.knife2.throw()

            elif self.knife3.THROWN is False:
                self.knife3.throw()

            elif self.knife4.THROWN is False:
                self.knife4.throw()

    def on_mouse_press(self, x, y, button, modifiers):
            if self.knife.THROWN is False:
                self.knife.throw()

            elif self.knife2.THROWN is False:
                self.knife2.throw()

            elif self.knife3.THROWN is False:
                self.knife3.throw()

            elif self.knife4.THROWN is False:
                self.knife4.throw()

