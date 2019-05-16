import arcade

WIDTH = 1200
HEIGHT = 800


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    draw_toolbar_dividers()
    draw_toolbar_shapes()

def draw_toolbar_dividers():
    # Draw toolbar outline
    arcade.draw_line(100, 0, 100, 800, arcade.color.BLACK)  # right border
    arcade.draw_line(1, 1, 1, 800, arcade.color.BLACK)  # left border
    arcade.draw_line(0, 0, 100, 0, arcade.color.BLACK)  # bottom border
    arcade.draw_line(1, 799, 100, 799, arcade.color.BLACK)  # top border

    # Draw toolbar divider
    arcade.draw_line(50, 0, 50, 799, arcade.color.BLACK)  # middle divider

    # Draw toolbar mini dividers
    for i in range(0, 800, 50):
        arcade.draw_line(0, i, 100, i, arcade.color.BLACK)

def draw_toolbar_shapes():
    pass

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "PyArcadePaint")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/200)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
