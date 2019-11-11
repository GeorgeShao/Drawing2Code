import arcade
WIDTH = 800
HEIGHT = 800
elements = None

def on_update(delta_time):
    pass

def on_draw():
    elements.append(arcade.create_line(230, 421, 240, 424, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(245, 426, 260, 431, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(256, 429, 267, 432, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(268, 434, 280, 439, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(282, 438, 296, 442, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(299, 443, 316, 448, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(316, 450, 333, 457, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(335, 455, 354, 460, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(352, 461, 369, 467, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(358, 461, 364, 461, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(372, 467, 386, 473, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(376, 469, 380, 471, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(377, 470, 378, 471, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(378, 471, 379, 472, color=(255, 0, 0), line_width=32))

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
    global elements, toolbar

    arcade.open_window(WIDTH, HEIGHT, "PyArcadePaint")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/1000)

    # Shape shape list
    elements = arcade.ShapeElementList()
    elements.center_x = 0
    elements.center_y = 0
    elements.angle = 0

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
