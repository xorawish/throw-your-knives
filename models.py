import arcade

class Knife:
    THROWN = False
    THROW_VELOCITY = 15
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def throw(self):
        self.THROWN = True

    def update(self, delta):
        if self.THROWN:
            self.y += self.THROW_VELOCITY

class Target:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def update(self, delta):
        pass

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.knife = Knife(self, width // 2, height // 5)
        self.target = Target(self, width // 2, height // 2)

    def update(self, delta):
        self.knife.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.knife.throw()

    def on_mouse_press(self, x, y, button, modifiers):
            self.knife.throw()

