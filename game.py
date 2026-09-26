from browser import timer 

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

    def draw(self):
        self.display.clear()
        body = self.snake.body
        for i in range(len(body)):
            x,y = body[i]
            if i == 0:
                self.display.draw_cell(x,y,"block","#00ff00")
            else:
                self.display.draw_cell(x,y,"block","#00aa00")
        self.display.render()
    def on_action(self, action):
        if action in ACTION_DIR:
            self.snake.set_direction(ACTION_DIR[action])

    def tick(self):
        self.snake.step()
        if self.snake.hits_wall(self.width, self.height) or self.snake.hits_self():
            timer.clear_interval(self.timer_id)
            print("game over")
            return
    def start(self, interval=150):
        self.draw()
        self.timer_id = timer.set_interval(self.tick, interval)
