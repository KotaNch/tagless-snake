from snake import Snake
from display import Display
from game import Game
from input import Input

d = Display(cols=32,rows=24,cell_w=20,cell_h=20)
s = Snake(10,10)

g = Game(d,s)
game_input = Input(g.on_action)

g.start()
