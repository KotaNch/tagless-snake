from browser import document, window

class Display:
    def __init__(self, cols=80, rows=40, cell_w=12, cell_h=20, bg="#101014", fg="#c8c8c8"):

        self.cols = cols
        self.rows = rows
        self.cell_w = cell_w
        self.cell_h = cell_h
        self.bg =bg
        self.fg = fg

        self.canvas = document.createElement("canvas")
        self.canvas.width = cols * cell_w
        self.canvas.height = rows * cell_h
        self.ctx = self.canvas.getContext("2d")
        self.canvas.style.background = bg

        body = document.body
        body.style.margin = "0"
        body.style.background = bg
        body.style.display = "grid"
        body.style.placeItems = "center"
        body.style.minHeight = "100vh"
        document.body.appendChild(self.canvas)


        self.buffer = []

        self.ctx.font = "{}px monospace".format(int(cell_h*0.9))
        self.ctx.textBaseline = "top"
        self.ctx.textAlign = "left"
        for _ in range(cols * rows):
            self.buffer.append({"ch": " ", "fg": fg,"bg":bg})
    def index(self, x, y):
        return y * self.cols + x

    def in_bounds(self, x, y):
        return 0 <= x < self.cols and 0 <= y < self.rows

    def clear(self):
        for cell in self.buffer:
            cell["ch"] = " "
            cell["fg"] = self.fg
            cell["bg"] = self.bg

    def draw_glyph(self, x, y, ch, fg=None, bg=None):
        if not self.in_bounds(x,y):
            return
        cell = self.buffer[self.index(x,y)]
        cell["ch"] = ch
        cell["fg"] = fg or self.fg
        cell["bg"] = bg or self.bg
        
    def render(self):
        ctx = self.ctx
        for y in range(self.rows):
            for x in range(self.cols):
                cell = self.buffer[self.index(x,y)]
                px = x * self.cell_w
                py = y * self.cell_h
                ctx.fillStyle = cell["bg"]
                ctx.fillRect(px,py, self.cell_w, self.cell_h)
                if cell["ch"] != " ":
                    ctx.fillStyle = cell["fg"]
                    ctx.fillText(cell["ch"],px,py)

        