import arcade 
 
WIDTH = 800 
HEIGHT = 800 
 
 
def on_update(delta_time): 
    pass 
 
 
def on_draw(): 
    arcade.start_render() 
    # Drawing code here 
    arcade.draw_lrtb_rectangle_filled(126, 688, 587, 289, (255, 0, 0))
    arcade.draw_line(161, 485, 241, 414, (255, 255, 0), line_width=5)
    arcade.draw_line(151, 474, 173, 503, (255, 255, 0), line_width=5)
    arcade.draw_line(153, 426, 165, 447, (255, 255, 0), line_width=5)
    arcade.draw_line(158, 436, 164, 435, (255, 255, 0), line_width=5)
    arcade.draw_line(165, 433, 171, 433, (255, 255, 0), line_width=5)
    arcade.draw_line(170, 433, 174, 434, (255, 255, 0), line_width=5)
    arcade.draw_line(174, 433, 178, 437, (255, 255, 0), line_width=5)
    arcade.draw_line(175, 437, 181, 441, (255, 255, 0), line_width=5)
    arcade.draw_line(174, 435, 183, 443, (255, 255, 0), line_width=5)
    arcade.draw_line(182, 438, 186, 448, (255, 255, 0), line_width=5)
    arcade.draw_line(180, 440, 190, 453, (255, 255, 0), line_width=5)
    arcade.draw_line(182, 446, 189, 459, (255, 255, 0), line_width=5)
    arcade.draw_line(184, 451, 196, 469, (255, 255, 0), line_width=5)
    arcade.draw_line(191, 458, 191, 464, (255, 255, 0), line_width=5)
    arcade.draw_line(191, 469, 201, 497, (255, 255, 0), line_width=5)
    arcade.draw_line(194, 483, 198, 502, (255, 255, 0), line_width=5)
    arcade.draw_line(196, 489, 198, 509, (255, 255, 0), line_width=5)
    arcade.draw_line(198, 504, 191, 515, (255, 255, 0), line_width=5)
    arcade.draw_line(193, 510, 189, 517, (255, 255, 0), line_width=5)
    arcade.draw_line(190, 515, 186, 517, (255, 255, 0), line_width=5)
    arcade.draw_line(163, 565, 170, 583, (255, 255, 0), line_width=5)
    arcade.draw_line(170, 583, 175, 567, (255, 255, 0), line_width=5)
    arcade.draw_line(174, 565, 191, 566, (255, 255, 0), line_width=5)
    arcade.draw_line(164, 565, 146, 566, (255, 255, 0), line_width=5)
    arcade.draw_line(148, 566, 161, 557, (255, 255, 0), line_width=5)
    arcade.draw_line(189, 565, 176, 557, (255, 255, 0), line_width=5)
    arcade.draw_line(158, 558, 146, 544, (255, 255, 0), line_width=5)
    arcade.draw_line(150, 544, 165, 550, (255, 255, 0), line_width=5)
    arcade.draw_line(165, 552, 177, 545, (255, 255, 0), line_width=5)
    arcade.draw_line(172, 556, 175, 546, (255, 255, 0), line_width=5)

 
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
