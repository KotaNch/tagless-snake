from browser import timer 
from rng import make_rng, hash_seed, rand_int

ACTION_DIR = {
    "move_n": (0, -1),
    "move_s": (0,1),
    "move_w":(-1,0),
    "move_e":(1,0),
}
class Game:
    def __init__(self,display,snake):
        self.display = display
        self.snake = snake
        self.width = display.cols
        self.height = display.rows
        self.rng = make_rng(hash_seed("snake"))
        self.food = None 
        self.spawn_food()

    def draw(self):
        self.display.clear()
        body = self.snake.body
        for i in range(len(body)):
            x,y = body[i]
            if i == 0:
                self.display.draw_cell(x,y,"block","#00ff00")
            else:
                self.display.draw_cell(x,y,"block","#00aa00")

        if self.food is not None:
            fx,fy = self.food
            self.display.draw_cell(fx,fy, "circle", "#ff4040")
        self.display.render()
    def on_action(self, action):
        if action in ACTION_DIR:
            self.snake.set_direction(ACTION_DIR[action])

    def tick(self):
        hx, hy = self.snake.head()
        dx,dy = self.snake.direction
        next_head = (hx + dx, hy + dy)

        if next_head == self.food:
            self.snake.step(grow=True)
            self.spawn_food()
        else:
            self.snake.step()
        if self.snake.hits_wall(self.width, self.height) or self.snake.hits_self():
            timer.clear_interval(self.timer_id)
            print("game over")
            return
        self.draw()

    def start(self, interval=150):
        self.draw()
        self.timer_id = timer.set_interval(self.tick, interval)


    def spawn_food(self):
        while True:
            x = rand_int(self.rng,0,self.width-1)
            y = rand_int(self.rng,0, self.height-1)
            if (x,y) not in self.snake.body:
                self.food = (x,y)
                return
