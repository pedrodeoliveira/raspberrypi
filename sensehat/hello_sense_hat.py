from sense_hat import SenseHat

sense = SenseHat()
y = (255, 255, 0)
b = (0, 0, 255)
r = (255, 0, 0)
w = (255, 255, 255)
sense.show_message("Feliz Ano Novo SL!", text_colour=w, back_colour=r,
                   scroll_speed=0.1)
