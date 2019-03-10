import arcade

class Knife:
    THROWN = False
    THROW_VELOCITY = 15
    
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

    def throw(self):
        self.THROWN = True

    def stab(self):
        self.THROWN = False

    def update(self, delta):
        if self.THROWN:
            self.y += self.THROW_VELOCITY

    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

class Target:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

    def update(self, delta):
        self.angle += 10

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.knife = Knife(self, width // 2, height // 5)
        self.target = Target(self, width // 2, height // 2)

    def update(self, delta):
        self.target.update(delta)
        self.knife.update(delta)
        if self.knife.hit(self.target, 60):
            self.knife.stab()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.knife.throw()

    def on_mouse_press(self, x, y, button, modifiers):
            self.knife.throw()

