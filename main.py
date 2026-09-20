
from display import Display
from map import GameMap, FLOOR



d = Display()
m = GameMap(d.cols, d.rows)

m.set(10,5, FLOOR)
m.set(11,5, FLOOR)
m.set(12,5, FLOOR)


m.draw(d)
d.render()