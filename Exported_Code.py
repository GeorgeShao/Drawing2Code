import arcade

WIDTH = 800
HEIGHT = 800
elements = None

def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    elements.draw()


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_drag(x, y, dx, dy, button, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def on_mouse_release(x, y, button, modifiers):
    pass


def setup():
    global elements

    arcade.open_window(WIDTH, HEIGHT, "PyArcadePaint")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Shape shape list
    elements = arcade.ShapeElementList()
    elements.center_x = 0
    elements.center_y = 0
    elements.angle = 0

    # Drawing code here

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    window.on_mouse_release = on_mouse_release
    window.on_mouse_drag = on_mouse_drag
    arcade.run()


if __name__ == '__main__':
    setup()
