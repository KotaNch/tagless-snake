from snake import Snake
from display import Display
from game import Game
from input import Input

d = Display(cols=40,rows=30,cell_w=28,cell_h=28)

g = Game(d)
game_input = Input(g.on_action)

g.start()
