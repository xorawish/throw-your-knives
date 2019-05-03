import arcade.key

from models import World, Knife, Target

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, title="Throw your knives!")

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.knife_sprite = None
        self.knife_sprite2 = None
        self.knife_sprite3 = None
        self.knife_sprite4 = None
        self.target_sprite = ModelSprite('images/target.png',
                                         model=self.world.target)

        self.total_time = 0.0

    def setup(self):

        arcade.set_background_color(arcade.color.BLACK)

        self.total_time = 0.0
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.knife_sprite = ModelSprite('images/knife.png',
                                        model=self.world.knife)
        self.knife_sprite2 = ModelSprite('images/knife.png',
                                         model=self.world.knife2)
        self.knife_sprite3 = ModelSprite('images/knife.png',
                                         model=self.world.knife3)
        self.knife_sprite4 = ModelSprite('images/knife.png',
                                         model=self.world.knife4)
        self.target_sprite = ModelSprite('images/target.png',
                                         model=self.world.target)

    def update(self, delta):
        self.total_time += delta
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()
        self.target_sprite.draw()

        if self.world.is_frozened():
            start = "Press P to start"
            intruction = "Press Spacebar to throw a knife"
            caution = "Don't hit other knives on the target"
            arcade.draw_text(start + "\n" + intruction + "\n" + caution,
                             400, 500, arcade.color.WHITE, 18, align="center",
                             anchor_x="center", anchor_y="center")

        if self.world.is_started():
            minutes = int(self.total_time) // 60
            seconds = int(self.total_time) % 60
            timer = f"Timer: {minutes:02d}:{seconds:02d}"

            self.knife_sprite.draw()
            self.knife_sprite2.draw()
            self.knife_sprite3.draw()
            self.knife_sprite4.draw()
            arcade.draw_text("Press P to restart" + "\n" + "Score: " +
                             str(self.world.score) + "\n" + timer, 400, 500,
                             arcade.color.WHITE, 18, align="center",
                             anchor_x="center", anchor_y="center")

    def on_key_press(self, key, key_modifiers):
        if(key == arcade.key.P):

            if not self.world.is_started():
                self.setup()
                self.world.start()

            else:
                self.world.freeze()

        self.world.on_key_press(key, key_modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        self.world.on_mouse_press(x, y, button, modifiers)


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle

    def draw(self):
        self.sync_with_model()
        super().draw()


def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()


if __name__ == '__main__':
    main()
