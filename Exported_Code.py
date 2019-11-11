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
    elements.append(arcade.create_rectangle_filled((221+239)//2, (734+711)//2, abs(239-221), abs(711-734), (255, 0, 0)))
    elements.append(arcade.create_ellipse_filled(230, 669, 24, 24, (255, 0, 0)))
    elements.append(arcade.create_rectangle_outline((231+249)//2, (604+593)//2, abs(249-231), abs(593-604), (255, 0, 0)))
    elements.append(arcade.create_ellipse_filled(231, 634, abs(255-231), abs(625-634), (255, 0, 0)))
    elements.append(arcade.create_ellipse_outline(238, 566, 19, 19, (255, 0, 0)))
    elements.append(arcade.create_ellipse_outline(235, 512, abs(271-235), abs(507-512), (255, 0, 0)))
    elements.append(arcade.create_line(351, 741, 360, 741, color=(255, 0, 0), line_width=1))
    elements.append(arcade.create_line(359, 741, 367, 741, color=(255, 0, 0), line_width=1))
    elements.append(arcade.create_line(371, 740, 383, 739, color=(255, 0, 0), line_width=1))
    elements.append(arcade.create_line(383, 738, 395, 736, color=(255, 0, 0), line_width=1))
    elements.append(arcade.create_line(393, 735, 403, 732, color=(255, 0, 0), line_width=1))
    elements.append(arcade.create_line(406, 733, 419, 731, color=(255, 0, 0), line_width=1))
    elements.append(arcade.create_line(415, 731, 424, 729, color=(255, 0, 0), line_width=1))
    elements.append(arcade.create_line(417, 731, 419, 731, color=(255, 0, 0), line_width=1))
    elements.append(arcade.create_line(416, 731, 415, 731, color=(255, 0, 0), line_width=1))
    elements.append(arcade.create_line(346, 677, 347, 677, color=(255, 0, 0), line_width=2))
    elements.append(arcade.create_line(349, 677, 352, 677, color=(255, 0, 0), line_width=2))
    elements.append(arcade.create_line(353, 677, 357, 677, color=(255, 0, 0), line_width=2))
    elements.append(arcade.create_line(358, 677, 363, 677, color=(255, 0, 0), line_width=2))
    elements.append(arcade.create_line(365, 677, 372, 677, color=(255, 0, 0), line_width=2))
    elements.append(arcade.create_line(372, 677, 379, 677, color=(255, 0, 0), line_width=2))
    elements.append(arcade.create_line(377, 677, 382, 677, color=(255, 0, 0), line_width=2))
    elements.append(arcade.create_line(394, 677, 411, 677, color=(255, 0, 0), line_width=2))
    elements.append(arcade.create_line(397, 677, 400, 677, color=(255, 0, 0), line_width=2))
    elements.append(arcade.create_line(400, 677, 403, 677, color=(255, 0, 0), line_width=2))
    elements.append(arcade.create_line(400, 676, 400, 675, color=(255, 0, 0), line_width=2))
    elements.append(arcade.create_line(340, 617, 341, 617, color=(255, 0, 0), line_width=4))
    elements.append(arcade.create_line(343, 617, 346, 617, color=(255, 0, 0), line_width=4))
    elements.append(arcade.create_line(349, 617, 355, 617, color=(255, 0, 0), line_width=4))
    elements.append(arcade.create_line(358, 617, 367, 617, color=(255, 0, 0), line_width=4))
    elements.append(arcade.create_line(370, 616, 382, 615, color=(255, 0, 0), line_width=4))
    elements.append(arcade.create_line(386, 616, 402, 616, color=(255, 0, 0), line_width=4))
    elements.append(arcade.create_line(397, 614, 408, 612, color=(255, 0, 0), line_width=4))
    elements.append(arcade.create_line(413, 614, 429, 614, color=(255, 0, 0), line_width=4))
    elements.append(arcade.create_line(423, 613, 433, 612, color=(255, 0, 0), line_width=4))
    elements.append(arcade.create_line(439, 613, 455, 613, color=(255, 0, 0), line_width=4))
    elements.append(arcade.create_line(446, 613, 453, 613, color=(255, 0, 0), line_width=4))
    elements.append(arcade.create_line(450, 613, 454, 613, color=(255, 0, 0), line_width=4))
    elements.append(arcade.create_line(454, 613, 458, 613, color=(255, 0, 0), line_width=4))
    elements.append(arcade.create_line(331, 540, 332, 540, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(335, 540, 339, 540, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(343, 541, 351, 542, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(355, 543, 367, 545, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(371, 543, 387, 543, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(390, 543, 409, 543, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(420, 543, 450, 543, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(439, 543, 458, 543, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(459, 542, 479, 541, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(470, 540, 481, 538, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(474, 539, 478, 538, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(477, 538, 480, 537, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(477, 537, 477, 536, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(476, 536, 475, 535, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(473, 535, 470, 534, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(469, 534, 465, 533, color=(255, 0, 0), line_width=8))
    elements.append(arcade.create_line(343, 483, 344, 483, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(347, 483, 351, 483, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(351, 483, 355, 483, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(363, 483, 375, 483, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(373, 482, 383, 481, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(385, 481, 397, 480, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(398, 480, 411, 479, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(413, 479, 428, 478, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(429, 478, 445, 477, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(440, 476, 451, 474, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(459, 473, 478, 470, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(468, 472, 477, 471, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(485, 470, 502, 468, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(492, 470, 499, 470, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(499, 469, 506, 468, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(500, 469, 501, 469, color=(255, 0, 0), line_width=16))
    elements.append(arcade.create_line(377, 421, 380, 421, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(381, 421, 385, 421, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(390, 421, 399, 421, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(400, 420, 410, 419, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(414, 418, 428, 416, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(426, 417, 438, 416, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(441, 414, 456, 411, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(451, 413, 461, 412, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(470, 412, 489, 411, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(481, 411, 492, 410, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(490, 411, 499, 411, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(499, 411, 508, 411, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(505, 411, 511, 411, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(507, 411, 509, 411, color=(255, 0, 0), line_width=32))
    elements.append(arcade.create_line(508, 411, 509, 411, color=(255, 0, 0), line_width=32))

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
