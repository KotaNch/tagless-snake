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
