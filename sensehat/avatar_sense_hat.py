from sense_hat import SenseHat

sense = SenseHat()
y = (255, 255, 0)
b = (0, 0, 255)
r = (255, 0, 0)
w = (255, 255, 255)
# sense.show_message("Hello, World!", text_colour=white, back_colour=red,
#                    scroll_speed=0.1)

pixels = [
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w,
 w, r, r, w, w, r, r, w,
 w, r, r, w, w, r, r, w,
 w, w, w, r, r, w, w, w,
 w, w, w, r, r, w, w, w,
 w, w, r, r, r, r, w, w,
 w, w, r, w, w, r, w, w
]
sense.set_pixels(pixels)

