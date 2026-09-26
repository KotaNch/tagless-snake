class Snake:
    def __init__(self, x, y, direction=(1,0)):
        self.body = [(x,y)]
        self.direction = direction

    def head(self):
        return self.body[0]
    
    def set_direction(self, new_dir):
        dx, dy = new_dir
        cur_dx, cur_dy = self.direction
        if(dx, dy) == (-cur_dx, -cur_dy):
            return
        self.direction = new_dir

    def step(self, grow=False):
        hx, hy = self.body[0]
        dx, dy = self.direction
        new_head = (hx + dx, hy + dy)
        self.body.insert(0, new_head)
        if not grow:
            self.body.pop()

    def hits_wall(self, width, height):
        hx, hy = self.body[0]
        return hx < 0 or hy < 0 or hx >= width or hy >=height

    def hits_self(self):
        return self.body[0] in self.body[1:]



