from snake import Snake
from display import Display
from game import Game

d = Display(cols=32,rows=24,cell_w=20,cell_h=20)
s = Snake(10,10)
for _ in range(4):
    s.step(grow=True)

g = Game(d,s)
g.draw()
