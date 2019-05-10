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
        return (abs(self.x - other.x) <= self.RADIUS + other.RADIUS) and (
            abs(self.y - other.y) <= self.RADIUS + other.RADIUS)


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
    STATE_OVER = 3
    STATE_MENU = 4
    STATE_WIN = 5

    def __init__(self, width, height):
        self.state = World.STATE_MENU
        self.score = 0
        self.width = width
        self.height = height
        self.knife = Knife(self, width // 2, height // 5)
        self.knife2 = Knife(self, width // 2, height // 5)
        self.knife3 = Knife(self, width // 2, height // 5)
        self.knife4 = Knife(self, width // 2, height // 5)
        self.knife5 = Knife(self, width // 2, height // 5)
        self.knife6 = Knife(self, width // 2, height // 5)
        self.knife7 = Knife(self, width // 2, height // 5)
        self.knife8 = Knife(self, width // 2, height // 5)
        self.knife9 = Knife(self, width // 2, height // 5)
        self.knife10 = Knife(self, width // 2, height // 5)
        self.target = Target(self, width // 2, height // 2)

    def update(self, delta):

        self.knife.update(delta)
        if self.knife.hit(self.target):
            self.knife.stab()

        self.knife2.update(delta)
        if self.knife2.hit(self.target):
            self.knife2.stab()
        elif self.knife2.hit(self.knife) and self.knife.is_stabbed():
            self.over()

        self.knife3.update(delta)
        if self.knife3.hit(self.target):
            self.knife3.stab()
        elif self.knife3.hit(self.knife) and self.knife.is_stabbed():
            self.over()
        elif self.knife3.hit(self.knife2) and self.knife2.is_stabbed():
            self.over()

        self.knife4.update(delta)
        if self.knife4.hit(self.target):
            self.knife4.stab()
        elif self.knife4.hit(self.knife) and self.knife.is_stabbed():
            self.over()
        elif self.knife4.hit(self.knife2) and self.knife2.is_stabbed():
            self.over()
        elif self.knife4.hit(self.knife3) and self.knife3.is_stabbed():
            self.over()

        self.knife5.update(delta)
        if self.knife5.hit(self.target):
            self.knife5.stab()
        elif self.knife5.hit(self.knife) and self.knife.is_stabbed():
            self.over()
        elif self.knife5.hit(self.knife2) and self.knife2.is_stabbed():
            self.over()
        elif self.knife5.hit(self.knife3) and self.knife3.is_stabbed():
            self.over()
        elif self.knife5.hit(self.knife4) and self.knife4.is_stabbed():
            self.over()

        self.knife6.update(delta)
        if self.knife6.hit(self.target):
            self.knife6.stab()
        elif self.knife6.hit(self.knife) and self.knife.is_stabbed():
            self.over()
        elif self.knife6.hit(self.knife2) and self.knife2.is_stabbed():
            self.over()
        elif self.knife6.hit(self.knife3) and self.knife3.is_stabbed():
            self.over()
        elif self.knife6.hit(self.knife4) and self.knife4.is_stabbed():
            self.over()
        elif self.knife6.hit(self.knife5) and self.knife5.is_stabbed():
            self.over()

        self.knife7.update(delta)
        if self.knife7.hit(self.target):
            self.knife7.stab()
        elif self.knife7.hit(self.knife) and self.knife.is_stabbed():
            self.over()
        elif self.knife7.hit(self.knife2) and self.knife2.is_stabbed():
            self.over()
        elif self.knife7.hit(self.knife3) and self.knife3.is_stabbed():
            self.over()
        elif self.knife7.hit(self.knife4) and self.knife4.is_stabbed():
            self.over()
        elif self.knife7.hit(self.knife5) and self.knife5.is_stabbed():
            self.over()
        elif self.knife7.hit(self.knife6) and self.knife6.is_stabbed():
            self.over()

        self.knife8.update(delta)
        if self.knife8.hit(self.target):
            self.knife8.stab()
        elif self.knife8.hit(self.knife) and self.knife.is_stabbed():
            self.over()
        elif self.knife8.hit(self.knife2) and self.knife2.is_stabbed():
            self.over()
        elif self.knife8.hit(self.knife3) and self.knife3.is_stabbed():
            self.over()
        elif self.knife8.hit(self.knife4) and self.knife4.is_stabbed():
            self.over()
        elif self.knife8.hit(self.knife5) and self.knife5.is_stabbed():
            self.over()
        elif self.knife8.hit(self.knife6) and self.knife6.is_stabbed():
            self.over()
        elif self.knife8.hit(self.knife7) and self.knife7.is_stabbed():
            self.over()

        self.knife9.update(delta)
        if self.knife9.hit(self.target):
            self.knife9.stab()
        elif self.knife9.hit(self.knife) and self.knife.is_stabbed():
            self.over()
        elif self.knife9.hit(self.knife2) and self.knife2.is_stabbed():
            self.over()
        elif self.knife9.hit(self.knife3) and self.knife3.is_stabbed():
            self.over()
        elif self.knife9.hit(self.knife4) and self.knife4.is_stabbed():
            self.over()
        elif self.knife9.hit(self.knife5) and self.knife5.is_stabbed():
            self.over()
        elif self.knife9.hit(self.knife6) and self.knife6.is_stabbed():
            self.over()
        elif self.knife9.hit(self.knife7) and self.knife7.is_stabbed():
            self.over()
        elif self.knife9.hit(self.knife8) and self.knife8.is_stabbed():
            self.over()

        self.knife10.update(delta)
        if self.knife10.hit(self.target):
            self.knife10.stab()
            self.win()
        elif self.knife10.hit(self.knife) and self.knife.is_stabbed():
            self.over()
        elif self.knife10.hit(self.knife2) and self.knife2.is_stabbed():
            self.over()
        elif self.knife10.hit(self.knife3) and self.knife3.is_stabbed():
            self.over()
        elif self.knife10.hit(self.knife4) and self.knife4.is_stabbed():
            self.over()
        elif self.knife10.hit(self.knife5) and self.knife5.is_stabbed():
            self.over()
        elif self.knife10.hit(self.knife6) and self.knife6.is_stabbed():
            self.over()
        elif self.knife10.hit(self.knife7) and self.knife7.is_stabbed():
            self.over()
        elif self.knife10.hit(self.knife8) and self.knife8.is_stabbed():
            self.over()
        elif self.knife10.hit(self.knife9) and self.knife9.is_stabbed():
            self.over()

        self.target.update(delta)

    def start(self):
        self.state = World.STATE_STARTED

    def freeze(self):
        self.state = World.STATE_FROZEN

    def over(self):
        self.state = World.STATE_OVER

    def menu(self):
        self.state = World.STATE_MENU

    def win(self):
        self.state = World.STATE_WIN

    def is_started(self):
        return self.state == World.STATE_STARTED

    def is_frozened(self):
        return self.state == World.STATE_FROZEN

    def is_overed(self):
        return self.state == World.STATE_OVER

    def is_menued(self):
        return self.state == World.STATE_MENU

    def is_win(self):
        return self.state == World.STATE_WIN

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE and self.state == World.STATE_STARTED:
            if self.knife.THROWN is False:
                self.knife.throw()
                self.score += 1

            elif self.knife2.THROWN is False:
                self.knife2.throw()
                self.score += 1

            elif self.knife3.THROWN is False:
                self.knife3.throw()
                self.score += 1

            elif self.knife4.THROWN is False:
                self.knife4.throw()
                self.score += 1

            elif self.knife5.THROWN is False:
                self.knife5.throw()
                self.score += 1

            elif self.knife6.THROWN is False:
                self.knife6.throw()
                self.score += 1

            elif self.knife7.THROWN is False:
                self.knife7.throw()
                self.score += 1

            elif self.knife8.THROWN is False:
                self.knife8.throw()
                self.score += 1

            elif self.knife9.THROWN is False:
                self.knife9.throw()
                self.score += 1

            elif self.knife10.THROWN is False:
                self.knife10.throw()
                self.score += 1

    def on_mouse_press(self, x, y, button, modifiers):
        if self.state == World.STATE_STARTED:
            if self.knife.THROWN is False:
                self.knife.throw()
                self.score += 1

            elif self.knife2.THROWN is False:
                self.knife2.throw()
                self.score += 1

            elif self.knife3.THROWN is False:
                self.knife3.throw()
                self.score += 1

            elif self.knife4.THROWN is False:
                self.knife4.throw()
                self.score += 1

            elif self.knife5.THROWN is False:
                self.knife5.throw()
                self.score += 1

            elif self.knife6.THROWN is False:
                self.knife6.throw()
                self.score += 1

            elif self.knife7.THROWN is False:
                self.knife7.throw()
                self.score += 1

            elif self.knife8.THROWN is False:
                self.knife8.throw()
                self.score += 1

            elif self.knife9.THROWN is False:
                self.knife9.throw()
                self.score += 1

            elif self.knife10.THROWN is False:
                self.knife10.throw()
                self.score += 1
