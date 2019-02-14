import arcade


WIDTH = 640
HEIGHT = 480
x= int (input ("enter x "))
y= int (input("enter y"))
r = int (input ("enter radius"))
arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(x, y, r, arcade.color.CHINA_ROSE)

# End drawing
arcade.finish_render()
arcade.run()

