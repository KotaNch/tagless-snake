from browser import timer 
from rng import make_rng, hash_seed, rand_int
from snake import Snake

ACTION_DIR = {
    "move_n": (0, -1),
    "move_s": (0,1),
    "move_w":(-1,0),
    "move_e":(1,0),
}
class Game:
    def __init__(self,display):
        self.display = display
        self.width = display.cols
        self.height = display.rows
        self.rng = make_rng(hash_seed("snake"))
        self.high_score = 0
        self.reset()

    def reset(self):
        self.snake =Snake(self.width // 2, self.height//2)
        self.spawn_food()
        self.running = True
        self.score = 0

    def draw(self):
        self.display.clear()
        body = self.snake.body
        for x in range(self.width):
            self.display.draw_cell(x,0,"block", "#444450")
            self.display.draw_cell(x, self.height-1, "block", "#444450")

        for y in range(self.height):
            self.display.draw_cell(0,y,"block", "#444450")
            self.display.draw_cell(self.width-1,y, "block", "#444450")

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
        self.display.draw_text_px(10,8, "Score: {}".format(self.score), "#ffffff",44)

        if not self.running:
            cx = self.display.canvas.width /2
            cy = self.display.canvas.height /2
            self.display.draw_overlay("rgba(0,0,0,0.6)")
            self.display.draw_text_px(cx,cy - 100, "GAME OVER", "#ff4040", 55,center=True)
            self.display.draw_text_px(cx,cy - 20, "Score: {}".format(self.score),"#ffffff",44, center=True)
            self.display.draw_text_px(cx, cy +30, "Best: {}".format(self.high_score), "#e0c040", 44, center=True)
            self.display.draw_text_px(cx,cy + 100, "Press R to restart", "#aaaaaa", 38, center=True)
    def on_action(self, action):
        if action in ACTION_DIR:
            self.snake.set_direction(ACTION_DIR[action])
        if action == "restart":
            self.reset()

    def tick(self):
        if not self.running:
            return
        hx, hy = self.snake.head()
        dx,dy = self.snake.direction
        next_head = (hx + dx, hy + dy)

        if next_head == self.food:
            self.snake.step(grow=True)
            self.spawn_food()
            self.score += 1
        else:
            self.snake.step()
        if self.snake.hits_wall(self.width, self.height) or self.snake.hits_self():
            self.running = False
            if self.score > self.high_score:
                self.high_score = self.score
            self.draw()
            print("game over")
            return
        self.draw()


    def start(self, interval=150):
        self.draw()
        self.timer_id = timer.set_interval(self.tick, interval)


    def spawn_food(self):
        while True:
            x = rand_int(self.rng,1,self.width-2)
            y = rand_int(self.rng,1, self.height-2)
            if (x,y) not in self.snake.body:
                self.food = (x,y)
                return
