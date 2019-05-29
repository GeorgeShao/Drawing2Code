import arcade 
 
WIDTH = 800 
HEIGHT = 800 
 
 
def on_update(delta_time): 
    pass 
 
 
def on_draw(): 
    arcade.start_render() 
    # Drawing code here 
    arcade.draw_lrtb_rectangle_filled(120, 630, 561, 271, (255, 0, 0))
    arcade.draw_line(179, 502, 258, 435, (255, 255, 0), line_width=5)
    arcade.draw_line(171, 494, 193, 521, (255, 255, 0), line_width=5)
    arcade.draw_line(175, 501, 164, 487, (255, 255, 0), line_width=5)
    arcade.draw_line(170, 457, 173, 456, (255, 255, 0), line_width=5)
    arcade.draw_line(177, 455, 185, 453, (255, 255, 0), line_width=5)
    arcade.draw_line(185, 453, 195, 456, (255, 255, 0), line_width=5)
    arcade.draw_line(193, 454, 199, 457, (255, 255, 0), line_width=5)
    arcade.draw_line(185, 454, 187, 454, (255, 255, 0), line_width=5)
    arcade.draw_line(172, 456, 175, 457, (255, 255, 0), line_width=5)
    arcade.draw_line(198, 458, 204, 461, (255, 255, 0), line_width=5)
    arcade.draw_line(204, 460, 207, 466, (255, 255, 0), line_width=5)
    arcade.draw_line(207, 466, 213, 472, (255, 255, 0), line_width=5)
    arcade.draw_line(212, 471, 214, 479, (255, 255, 0), line_width=5)
    arcade.draw_line(214, 477, 219, 489, (255, 255, 0), line_width=5)
    arcade.draw_line(217, 485, 217, 496, (255, 255, 0), line_width=5)
    arcade.draw_line(216, 489, 216, 501, (255, 255, 0), line_width=5)
    arcade.draw_line(216, 494, 215, 505, (255, 255, 0), line_width=5)
    arcade.draw_line(172, 455, 176, 455, (255, 255, 0), line_width=5)
    arcade.draw_line(173, 456, 178, 456, (255, 255, 0), line_width=5)
    arcade.draw_line(216, 502, 215, 511, (255, 255, 0), line_width=5)
    arcade.draw_line(175, 457, 157, 440, (255, 255, 0), line_width=5)
    arcade.draw_line(213, 507, 208, 520, (255, 255, 0), line_width=5)
    arcade.draw_line(211, 518, 208, 522, (255, 255, 0), line_width=5)
    arcade.draw_line(182, 547, 184, 557, (255, 255, 0), line_width=5)
    arcade.draw_line(185, 559, 190, 548, (255, 255, 0), line_width=5)
    arcade.draw_line(180, 549, 172, 549, (255, 255, 0), line_width=5)
    arcade.draw_line(187, 549, 195, 549, (255, 255, 0), line_width=5)
    arcade.draw_line(171, 550, 182, 544, (255, 255, 0), line_width=5)
    arcade.draw_line(195, 549, 189, 546, (255, 255, 0), line_width=5)
    arcade.draw_line(188, 546, 194, 537, (255, 255, 0), line_width=5)
    arcade.draw_line(179, 544, 173, 538, (255, 255, 0), line_width=5)
    arcade.draw_line(173, 538, 182, 541, (255, 255, 0), line_width=5)
    arcade.draw_line(182, 541, 187, 543, (255, 255, 0), line_width=5)

 
def on_key_press(key, modifiers): 
    pass 
 
 
def on_key_release(key, modifiers): 
    pass 
 
 
def on_mouse_press(x, y, button, modifiers): 
    pass 
 
 
def setup(): 
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game") 
    arcade.set_background_color(arcade.color.WHITE) 
    arcade.schedule(on_update, 1/60) 
    # Override arcade window methods 
    window = arcade.get_window() 
    window.on_draw = on_draw 
    window.on_key_press = on_key_press 
    window.on_key_release = on_key_release 
    window.on_mouse_press = on_mouse_press 
    arcade.run() 
 
 
if __name__ == '__main__': 
    setup() 
