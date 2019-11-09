import arcade
import pymsgbox
import math

# Window width & height
WIDTH = 900
HEIGHT = 800

# Chosen color & shape row & column variables
chosen_color_row = 0
chosen_color_column = 0
chosen_shape_row = 0
chosen_shape_column = 0

# In-the-moment drawing variables
currently_drawing = False
start_x = 0
start_y = 0
end_x = 0
end_y = 0

elements = None
toolbar = None

def get_chosen_color():
    if chosen_color_column == 1:
        if chosen_color_row == 1:
            return arcade.color.BLACK
        if chosen_color_row == 2:
            return arcade.color.WHITE
        if chosen_color_row == 3:
            return arcade.color.VIOLET
        if chosen_color_row == 4:
            return arcade.color.PURPLE
        if chosen_color_row == 5:
            return  arcade.color.BLUE
        if chosen_color_row == 6:
            return arcade.color.GREEN
        if chosen_color_row == 7:
            return arcade.color.YELLOW
        if chosen_color_row == 8:
            return arcade.color.ORANGE
        if chosen_color_row == 9:
            return arcade.color.RED
    if chosen_color_column == 2:
        if chosen_color_row == 1:
            return arcade.color.ASH_GREY
        if chosen_color_row == 2:
            return arcade.color.WHITE_SMOKE
        if chosen_color_row == 3:
            return arcade.color.BLUE_VIOLET
        if chosen_color_row == 4:
            return arcade.color.FUCHSIA_PURPLE
        if chosen_color_row == 5:
            return arcade.color.AIR_SUPERIORITY_BLUE
        if chosen_color_row == 6:
            return arcade.color.YELLOW_GREEN
        if chosen_color_row == 7:
            return arcade.color.FLUORESCENT_YELLOW
        if chosen_color_row == 8:
            return arcade.color.FLUORESCENT_ORANGE
        if chosen_color_row == 9:
            return arcade.color.RED_ORANGE

def on_update(delta_time):
    pass


def on_draw():
    global elements, toolbar

    # Renders toolbar, all drawn shapes, and export button
    arcade.start_render()
    elements.draw()
    toolbar.draw()
    arcade.draw_text("EXPORT", 15, 765, color=arcade.color.BLACK, font_size=18)


def draw_toolbar_dividers():
    global elements, toolbar

    # Draw toolbar outline
    toolbar.append(arcade.create_rectangle_filled(50, 400, 100, 800, arcade.color.TROLLEY_GREY))  # background
    toolbar.append(arcade.create_line(100, 0, 100, 800, arcade.color.BLACK))  # right border
    toolbar.append(arcade.create_line(1, 1, 1, 800, arcade.color.BLACK))  # left border
    toolbar.append(arcade.create_line(0, 0, 100, 0, arcade.color.BLACK))  # bottom border
    toolbar.append(arcade.create_line(1, 799, 100, 799, arcade.color.BLACK))  # top border

    # Draw toolbar divider
    toolbar.append(arcade.create_line(50, 0, 50, 750, arcade.color.BLACK))  # middle divider

    # Draw toolbar mini dividers
    for i in range(0, 800, 50):
        toolbar.append(arcade.create_line(0, i, 100, i, arcade.color.BLACK))


def draw_toolbar_shapes():
    global elements, toolbar

    # Draw rectangles
    toolbar.append(arcade.create_rectangle_filled(25, 725, 35, 15, arcade.color.BLUE))
    toolbar.append(arcade.create_rectangle_outline(25, 575, 35, 15, arcade.color.BLUE))

    # Draw circles
    toolbar.append(arcade.create_ellipse_filled(25, 675, 13, 13, arcade.color.BLUE))
    toolbar.append(arcade.create_ellipse_outline(25, 525, 13, 13, arcade.color.BLUE))

    # Draw ellipses
    toolbar.append(arcade.create_ellipse_filled(25, 625, 18, 8, arcade.color.BLUE))
    toolbar.append(arcade.create_ellipse_outline(25, 475, 18, 8, arcade.color.BLUE))

    # Draw lines
    toolbar.append(arcade.create_line(60, 710, 90, 740, arcade.color.BLUE, line_width=1))
    toolbar.append(arcade.create_line(60, 660, 90, 690, arcade.color.BLUE, line_width=2))
    toolbar.append(arcade.create_line(60, 610, 90, 640, arcade.color.BLUE, line_width=4))
    toolbar.append(arcade.create_line(60, 560, 90, 590, arcade.color.BLUE, line_width=8))
    toolbar.append(arcade.create_line(60, 510, 90, 540, arcade.color.BLUE, line_width=16))
    toolbar.append(arcade.create_line(60, 460, 90, 490, arcade.color.BLUE, line_width=32))


def draw_toolbar_colors():
    global elements, toolbar

    # First column of colors
    toolbar.append(arcade.create_rectangle_filled(25, 425, 50, 50, arcade.color.RED))
    toolbar.append(arcade.create_rectangle_filled(25, 375, 50, 50, arcade.color.ORANGE))
    toolbar.append(arcade.create_rectangle_filled(25, 325, 50, 50, arcade.color.YELLOW))
    toolbar.append(arcade.create_rectangle_filled(25, 275, 50, 50, arcade.color.GREEN))
    toolbar.append(arcade.create_rectangle_filled(25, 225, 50, 50, arcade.color.BLUE))
    toolbar.append(arcade.create_rectangle_filled(25, 175, 50, 50, arcade.color.PURPLE))
    toolbar.append(arcade.create_rectangle_filled(25, 125, 50, 50, arcade.color.VIOLET))
    toolbar.append(arcade.create_rectangle_filled(25, 75, 50, 50, arcade.color.WHITE))
    toolbar.append(arcade.create_rectangle_filled(25, 25, 50, 50, arcade.color.BLACK))

    # Second column of colors
    toolbar.append(arcade.create_rectangle_filled(75, 425, 50, 50, arcade.color.RED_ORANGE))
    toolbar.append(arcade.create_rectangle_filled(75, 375, 50, 50, arcade.color.FLUORESCENT_ORANGE))
    toolbar.append(arcade.create_rectangle_filled(75, 325, 50, 50, arcade.color.FLUORESCENT_YELLOW))
    toolbar.append(arcade.create_rectangle_filled(75, 275, 50, 50, arcade.color.YELLOW_GREEN))
    toolbar.append(arcade.create_rectangle_filled(75, 225, 50, 50, arcade.color.AIR_SUPERIORITY_BLUE))
    toolbar.append(arcade.create_rectangle_filled(75, 175, 50, 50, arcade.color.FUCHSIA_PURPLE))
    toolbar.append(arcade.create_rectangle_filled(75, 125, 50, 50, arcade.color.BLUE_VIOLET))
    toolbar.append(arcade.create_rectangle_filled(75, 75, 50, 50, arcade.color.WHITE_SMOKE))
    toolbar.append(arcade.create_rectangle_filled(75, 25, 50, 50, arcade.color.ASH_GREY))


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global chosen_color_column, chosen_shape_column, chosen_color_row, chosen_shape_row
    global currently_drawing, start_x, start_y, end_x, end_y

    # choosing color & shape row * column
    if 450 <= y <= 750:
        if x <= 50:
            for i in range(500, 800, 50):
                if y <= i:
                    chosen_shape_row = i/50
                    chosen_shape_column = 1
                    break
        elif x <= 100:
            for i in range(500, 800, 50):
                if y <= i:
                    chosen_shape_row = i/50
                    chosen_shape_column = 2
                    break
    elif y <= 450:
        if x <= 50:
            for i in range(0, 500, 50):
                if y <= i:
                    chosen_color_row = i/50
                    chosen_color_column = 1
                    break
        elif x <= 100:
            for i in range(0, 500, 50):
                if y <= i:
                    chosen_color_row = i/50
                    chosen_color_column = 2
                    break

    if x > 100:
        currently_drawing = True
        if chosen_color_column == 1:
            start_x = x
            start_y = y
        elif chosen_color_column == 2:
            start_x = x
            start_y = y
            end_x = x
            end_y = y
            # get color var
            if chosen_shape_row == 15:
                line_width = 1
            if chosen_shape_row == 14:
                line_width = 2
            if chosen_shape_row == 13:
                line_width = 4
            if chosen_shape_row == 12:
                line_width = 8
            if chosen_shape_row == 11:
                line_width = 16
            if chosen_shape_row == 10:
                line_width = 32
            # elements.append(arcade.create_line(start_x, start_y, end_x, end_y, color=get_chosen_color(), line_width=line_width))
            elements.append(arcade.create_ellipse_filled(start_x, start_y, line_width, line_width, color=get_chosen_color()))


def on_mouse_release(x, y, button, modifiers):
    global elements, toolbar
    global chosen_color_column, chosen_shape_column, chosen_color_row, chosen_shape_row
    global currently_drawing, start_x, start_y, end_x, end_y

    if x > 100:
        currently_drawing = False
        end_x = x
        end_y = y
        color = None

        # Determines & adds shape to object list
        if chosen_shape_column == 1:
            if chosen_shape_row == 15:
                elements.append(arcade.create_rectangle_filled((start_x+end_x)//2, (start_y+end_y)//2, abs(end_x-start_x), abs(end_y-start_y), get_chosen_color()))
            if chosen_shape_row == 14:
                radius = round(math.sqrt(abs(end_x-start_x)**2 + abs(end_y-start_y)**2))
                elements.append(arcade.create_ellipse_filled(start_x, start_y, radius, radius, get_chosen_color()))
            if chosen_shape_row == 13:
                elements.append(arcade.create_ellipse_filled(start_x, start_y, abs(end_x-start_x), abs(end_y-start_y), get_chosen_color()))
            if chosen_shape_row == 12:
                elements.append(arcade.create_rectangle_outline((start_x+end_x)//2, (start_y+end_y)//2, abs(end_x-start_x), abs(end_y-start_y), get_chosen_color()))
            if chosen_shape_row == 11:
                radius = round(math.sqrt(abs(end_x-start_x)**2 + abs(end_y-start_y)**2))
                elements.append(arcade.create_ellipse_outline(start_x, start_y, radius, radius, get_chosen_color()))
            if chosen_shape_row == 10:
                elements.append(arcade.create_ellipse_outline(start_x, start_y, abs(end_x-start_x), abs(end_y-start_y), get_chosen_color()))

    elif x < 100 and 750 < y < 800:
        pass
        # Exports PyArcade python code into Exported_Code.py file
        # with open('Exported_Code.py', 'w') as writer:

        #     writer.write("import arcade \n \n")
        #     writer.write("WIDTH = 800 \n")
        #     writer.write("HEIGHT = 800 \n \n \n")
        #     writer.write("def on_update(delta_time): \n")
        #     writer.write("    pass \n \n \n")
        #     writer.write("def on_draw(): \n")
        #     writer.write("    arcade.start_render() \n")
        #     writer.write("    # Drawing code here \n")

        #     for i in range(len(rectangles_filled)):
        #         writer.write("    " + RectangleFilled.create_code(rectangles_filled[i]) + "\n")
        #         rectangles_filled[i].x += 100
        #         rectangles_filled[i].x1 += 100
        #     for i in range(len(rectangles_outline)):
        #         writer.write("    " + RectangleOutline.create_code(rectangles_outline[i]) + "\n")
        #         rectangles_outline[i].x += 100
        #         rectangles_outline[i].x1 += 100
        #     for i in range(len(circle_filled)):
        #         writer.write("    " + CircleFilled.create_code(circle_filled[i]) + "\n")
        #         circle_filled[i].x += 100
        #         circle_filled[i].x1 += 100
        #     for i in range(len(circle_outline)):
        #         writer.write("    " + CircleOutline.create_code(circle_outline[i]) + "\n")
        #         circle_outline[i].x += 100
        #         circle_outline[i].x1 += 100
        #     for i in range(len(ellipse_filled)):
        #         writer.write("    " + EllipseFilled.create_code(ellipse_filled[i]) + "\n")
        #         ellipse_filled[i].x += 100
        #         ellipse_filled[i].x1 += 100
        #     for i in range(len(ellipse_outline)):
        #         writer.write("    " + EllipseOutline.create_code(ellipse_outline[i]) + "\n")
        #         ellipse_outline[i].x += 100
        #         ellipse_outline[i].x1 += 100
        #     for i in range(len(triangle_filled)):
        #         writer.write("    " + TriangleFilled.create_code(triangle_filled[i]) + "\n")
        #         triangle_filled[i].x += 100
        #         triangle_filled[i].x1 += 100
        #     for i in range(len(triangle_outline)):
        #         writer.write("    " + TriangleOutline.create_code(triangle_outline[i]) + "\n")
        #         triangle_outline[i].x += 100
        #         triangle_outline[i].x1 += 100
        #     for i in range(len(arc_top_filled)):
        #         writer.write("    " + ArcTopFilled.create_code(arc_top_filled[i]) + "\n")
        #         arc_top_filled[i].x += 100
        #         arc_top_filled[i].x1 += 100
        #     for i in range(len(arc_top_outline)):
        #         writer.write("    " + ArcTopOutline.create_code(arc_top_outline[i]) + "\n")
        #         arc_top_outline[i].x += 100
        #         arc_top_outline[i].x1 += 100
        #     for i in range(len(arc_bottom_filled)):
        #         writer.write("    " + ArcBottomFilled.create_code(arc_bottom_filled[i]) + "\n")
        #         arc_bottom_filled[i].x += 100
        #         arc_bottom_filled[i].x1 += 100
        #     for i in range(len(arc_bottom_outline)):
        #         writer.write("    " + ArcBottomOutline.create_code(arc_bottom_outline[i]) + "\n")
        #         arc_bottom_outline[i].x += 100
        #         arc_bottom_outline[i].x1 += 100
        #     for i in range(len(line_thick)):
        #         writer.write("    " + LineThick.create_code(line_thick[i]) + "\n")
        #         line_thick[i].x += 100
        #         line_thick[i].x1 += 100
        #     for i in range(len(line_thin)):
        #         writer.write("    " + LineThin.create_code(line_thin[i]) + "\n")
        #         line_thin[i].x += 100
        #         line_thin[i].x1 += 100

        #     writer.write("\n \n")
        #     writer.write("def on_key_press(key, modifiers): \n")
        #     writer.write("    pass \n \n \n")
        #     writer.write("def on_key_release(key, modifiers): \n")
        #     writer.write("    pass \n \n \n")
        #     writer.write("def on_mouse_press(x, y, button, modifiers): \n")
        #     writer.write("    pass \n \n \n")
        #     writer.write("def setup(): \n")
        #     writer.write("    arcade.open_window(WIDTH, HEIGHT, \"My Arcade Game\") \n")
        #     writer.write("    arcade.set_background_color(arcade.color.WHITE) \n")
        #     writer.write("    arcade.schedule(on_update, 1/60) \n")
        #     writer.write("    # Override arcade window methods \n")
        #     writer.write("    window = arcade.get_window() \n")
        #     writer.write("    window.on_draw = on_draw \n")
        #     writer.write("    window.on_key_press = on_key_press \n")
        #     writer.write("    window.on_key_release = on_key_release \n")
        #     writer.write("    window.on_mouse_press = on_mouse_press \n")
        #     writer.write("    arcade.run() \n \n \n")
        #     writer.write("if __name__ == '__main__': \n")
        #     writer.write("    setup() \n")

        # chosen_color_column = 0
        # chosen_color_row = 0
        # chosen_shape_column = 0
        # chosen_shape_row = 0

        # pymsgbox.alert(text='You exported the drawing as Python Arcade code in Exported_Code.py in this project\'s folder. Run it and your drawing should appear. See the README.md on my GitHub repo for more details.', title='Successfully Exported!')


def setup():
    global elements, toolbar

    arcade.open_window(WIDTH, HEIGHT, "PyArcadePaint")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Shape shape lists
    elements = arcade.ShapeElementList()
    elements.center_x = 0
    elements.center_y = 0
    elements.angle = 0

    # Toolbar shape lists
    toolbar = arcade.ShapeElementList()
    toolbar.center_x = 0
    toolbar.center_y = 0
    toolbar.angle = 0

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    window.on_mouse_release = on_mouse_release

    # Draw toolbar
    draw_toolbar_dividers()
    draw_toolbar_shapes()
    draw_toolbar_colors()

    arcade.run()


if __name__ == '__main__':
    setup()
