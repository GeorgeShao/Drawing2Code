import arcade 
 
WIDTH = 800 
HEIGHT = 800 
 
 
def on_update(delta_time): 
    pass 
 
 
def on_draw(): 
    arcade.start_render() 
    # Drawing code here 
    arcade.draw_circle_filled(133, 694, 336, (255, 165, 0))
    arcade.draw_circle_filled(419, 471, 86, (255, 165, 0))
    arcade.draw_line(122, 548, 322, 347, (255, 191, 0), line_width=5)
    arcade.draw_line(300, 556, 466, 400, (255, 83, 73), line_width=2)
    arcade.draw_line(434, 563, 262, 280, (255, 83, 73), line_width=2)
    arcade.draw_line(169, 242, 556, 566, (255, 83, 73), line_width=2)

 
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
