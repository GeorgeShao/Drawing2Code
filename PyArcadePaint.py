import arcade

# Window width & height
WIDTH = 900
HEIGHT = 800

# Chosen color & shape row & column variables
chosen_color_row = ""
chosen_color_column = ""
chosen_shape_row = ""
chosen_shape_column = ""

# In-the-moment drawing variables
currently_drawing = False
start_x = 0
start_y = 0
end_x = 0
end_y = 0

# Shape object arrays
rectangles = []


class Rectangle:
    def __init__(self, x, y, x1, y1):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1

    def draw_shape(self):
        if self.x <= self.x1:
            if self.y <= self.y1:
                arcade.draw_lrtb_rectangle_outline(self.x, self.x1, self.y1, self.y, arcade.color.BLUE)
            elif self.y1 < self.y:
                arcade.draw_lrtb_rectangle_outline(self.x, self.x1, self.y, self.y1, arcade.color.BLUE)
        elif self.x1 < self.x:
            if self.y <= self.y1:
                arcade.draw_lrtb_rectangle_outline(self.x1, self.x, self.y1, self.y, arcade.color.BLUE)
            elif self.y1 < self.y:
                arcade.draw_lrtb_rectangle_outline(self.x1, self.x, self.y, self.y1, arcade.color.BLUE)


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()

    draw_toolbar_dividers()
    draw_toolbar_shapes()
    draw_toolbar_colors()

    for i in range(len(rectangles)):
        Rectangle.draw_shape(rectangles[i])


def draw_toolbar_dividers():
    # Draw toolbar outline
    arcade.draw_xywh_rectangle_filled(0, 0, 100, 800, arcade.color.TROLLEY_GREY) # background
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
    # Draw squares
    arcade.draw_rectangle_filled(25, 775, 25, 25, arcade.color.BLUE)
    arcade.draw_rectangle_outline(75, 775, 25, 25, arcade.color.BLUE)

    # Draw rectangles
    arcade.draw_rectangle_filled(25, 725, 35, 15, arcade.color.BLUE)
    arcade.draw_rectangle_outline(75, 725, 35, 15, arcade.color.BLUE)

    # Draw circles
    arcade.draw_circle_filled(25, 675, 13, arcade.color.BLUE)
    arcade.draw_circle_outline(75, 675, 13, arcade.color.BLUE)

    # Draw ellipses
    arcade.draw_ellipse_filled(25, 625, 18, 8, arcade.color.BLUE)
    arcade.draw_ellipse_outline(75, 625, 18, 8, arcade.color.BLUE)

    # Draw triangles
    arcade.draw_triangle_filled(25, 590, 10, 560, 40, 560, arcade.color.BLUE)
    arcade.draw_triangle_outline(75, 590, 60, 560, 90, 560, arcade.color.BLUE)

    # Draw arc tops
    arcade.draw_arc_filled(25, 520, 15, 15, arcade.color.BLUE, 0, 180)
    arcade.draw_arc_outline(75, 520, 15, 15, arcade.color.BLUE, 0, 180)

    # Draw arc bottoms
    arcade.draw_arc_filled(25, 480, 15, 15, arcade.color.BLUE, 180, 360)
    arcade.draw_arc_outline(75, 480, 15, 15, arcade.color.BLUE, 180, 360)


def draw_toolbar_colors():
    # First column of colors
    arcade.draw_rectangle_filled(25, 425, 50, 50, arcade.color.RED)
    arcade.draw_rectangle_filled(25, 375, 50, 50, arcade.color.ORANGE)
    arcade.draw_rectangle_filled(25, 325, 50, 50, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(25, 275, 50, 50, arcade.color.GREEN)
    arcade.draw_rectangle_filled(25, 225, 50, 50, arcade.color.BLUE)
    arcade.draw_rectangle_filled(25, 175, 50, 50, arcade.color.PURPLE)
    arcade.draw_rectangle_filled(25, 125, 50, 50, arcade.color.VIOLET)
    arcade.draw_rectangle_filled(25, 75, 50, 50, arcade.color.WHITE)
    arcade.draw_rectangle_filled(25, 25, 50, 50, arcade.color.BLACK)

    # Second column of colors
    arcade.draw_rectangle_filled(75, 425, 50, 50, arcade.color.RED_ORANGE)
    arcade.draw_rectangle_filled(75, 375, 50, 50, arcade.color.FLUORESCENT_ORANGE)
    arcade.draw_rectangle_filled(75, 325, 50, 50, arcade.color.FLUORESCENT_YELLOW)
    arcade.draw_rectangle_filled(75, 275, 50, 50, arcade.color.YELLOW_GREEN)
    arcade.draw_rectangle_filled(75, 225, 50, 50, arcade.color.AIR_SUPERIORITY_BLUE)
    arcade.draw_rectangle_filled(75, 175, 50, 50, arcade.color.FUCHSIA_PURPLE)
    arcade.draw_rectangle_filled(75, 125, 50, 50, arcade.color.BLUE_VIOLET)
    arcade.draw_rectangle_filled(75, 75, 50, 50, arcade.color.WHITE_SMOKE)
    arcade.draw_rectangle_filled(75, 25, 50, 50, arcade.color.ASH_GREY)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global chosen_color_column, chosen_shape_column, chosen_color_row, chosen_shape_row
    global currently_drawing, start_x, start_y, end_x, end_y
    global rectangles

    # choosing color & shape row * column
    if y >= 350:
        if x <= 50:
            for i in range(450, 850, 50):
                if y <= i:
                    chosen_shape_row = i
                    chosen_shape_column = 1
                    break
        elif x <= 100:
            for i in range(450, 850, 50):
                if y <= i:
                    chosen_shape_row = i
                    chosen_shape_column = 2
                    break
    elif y <= 350:
        if x <= 50:
            for i in range(0, 450, 50):
                if y <= i:
                    chosen_color_row = i
                    chosen_color_column = 1
                    break
        elif x <= 100:
            for i in range(0, 450, 50):
                if y <= i:
                    chosen_color_row = i
                    chosen_color_column = 2
                    break

    if x <= 100:
        print("Color: " + str(chosen_color_column) + "/" + str(chosen_color_row))
        print("Shape: " + str(chosen_shape_column) + "/" + str(chosen_shape_row))

    if x > 100:
        currently_drawing = True
        start_x = x
        start_y = y
        print("Mouse Clicked")


def on_mouse_release(x, y, button, modifiers):
    global currently_drawing, start_x, start_y, end_x, end_y, rectangles
    if x > 100:
        currently_drawing = False
        end_x = x
        end_y = y
        rectangles.append(Rectangle(start_x, start_y, end_x, end_y))
        print("Mouse Released")

def setup():
    arcade.open_window(WIDTH, HEIGHT, "PyArcadePaint")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    window.on_mouse_release = on_mouse_release

    arcade.run()


if __name__ == '__main__':
    setup()
