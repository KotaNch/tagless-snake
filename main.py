from display import Display
from input import Input

d = Display()
d.draw_glyph(5,3,"@", "#ffffff")
d.draw_glyph(6,3,"g", "#40c040")


for x in range(d.cols):
    d.draw_glyph(x, 0, "#", "#4a4a52")
d.render()

game_input =Input()

