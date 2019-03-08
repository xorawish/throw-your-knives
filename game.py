import arcade
from models import World, Knife, Target

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.knife_sprite = ModelSprite('images/knife.png', model=self.world.knife)
        self.target_sprite = ModelSprite('images/target.png', model=self.world.target)

    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()

        self.knife_sprite.draw()
        self.target_sprite.draw()

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()

def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()