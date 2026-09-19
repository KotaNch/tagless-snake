from display import Display

d = Display()
d.draw_glyph(5,3,"@", "#ffffff")
d.draw_glyph(6,3,"g", "#40c040")

print(d.buffer[d.index(5,3)])
print(d.buffer[d.index(6,3)])
print("out of bounds ok: ", d.draw_glyph(999,999, "x"))

