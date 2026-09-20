
from display import Display



d = Display()

d.draw_cell(5,3,"block", "#585858")
d.draw_cell(7,3, "circle", "#e0c060")
d.draw_cell(9, 3, "diamond", "#3a7bd5")
d.draw_cell(11, 3, "triangle", "#40c040")
d.draw_cell(13, 3, "dot", "#c04040")
d.render()