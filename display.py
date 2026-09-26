from browser import document, window
import math

def shape_block(ctx,px,py,w,h,color):
    ctx.fillStyle =color
    ctx.fillRect(px,py,w,h)

def shape_circle(ctx,px,py,w,h,color):
    ctx.fillStyle = color
    ctx.beginPath()
    ctx.arc(px +w/2, py +h/2, min(w,h) * 0.4,0,2 * math.pi)
    ctx.fill()

def shape_diamond(ctx,px,py,w,h,color):
    cx = px + w /2
    cy = py +h /2
    ctx.fillStyle = color
    ctx.beginPath()
    ctx.moveTo(cx,py + h * 0.1)
    ctx.lineTo(px + w * 0.9, cy)
    ctx.lineTo(cx, py + h * 0.9)
    ctx.lineTo(px + w * 0.1, cy)
    ctx.closePath()
    ctx.fill()

def shape_triangle(ctx, px, py, w, h, color):
    ctx.fillStyle = color
    ctx.beginPath()
    ctx.moveTo(px + w/2, py + h * 0.15)
    ctx.lineTo(px + w * 0.85, py + h * 0.85)
    ctx.lineTo(px + w * 0.15, py + h * 0.85)
    ctx.closePath()
    ctx.fill()

def shape_dot(ctx, px, py, w, h, color):
    ctx.fillStyle = color
    ctx.beginPath()
    ctx.arc(px + w/2,py + h/2, min(w,h) * 0.14, 0, 2 * math.pi)
    ctx.fill()


SHAPES = {
    "block": shape_block,
    "circle": shape_circle,
    "diamond": shape_diamond,
    "triangle": shape_triangle,
    "dot":shape_dot,
}


class Display:
    def __init__(self, cols=80, rows=40, cell_w=16, cell_h=16, bg="#101014", fg="#c8c8c8"):

        self.cols = cols
        self.rows = rows
        self.cell_w = cell_w
        self.cell_h = cell_h
        self.bg =bg
        self.fg = fg
        
        dpr = max(window.devicePixelRatio or 1,1)
        css_w = cols * cell_w
        css_h = rows * cell_h

        self.canvas = document.createElement("canvas")
        self.canvas.setAttribute("width", str(css_w))
        self.canvas.setAttribute("height", str(css_h))
        self.canvas.style.width = "{}px".format(css_w)
        self.canvas.style.height = "{}px".format(css_h)
        self.ctx = self.canvas.getContext("2d")
        self.canvas.style.background = bg

        body = document.body
        body.style.margin = "0"
        body.style.background = bg
        body.style.display = "grid"
        body.style.placeItems = "center"
        body.style.minHeight = "100vh"
        while document.body.firstChild:
            document.body.removeChild(document.body.firstChild)
        document.body.appendChild(self.canvas)





        self.buffer = []
        for _ in range(cols * rows):
            self.buffer.append({"shape": None, "fg": fg,"bg":bg})
    def index(self, x, y):
        return y * self.cols + x

    def in_bounds(self, x, y):
        return 0 <= x < self.cols and 0 <= y < self.rows

    def clear(self):
        for cell in self.buffer:
            cell["shape"] = None
            cell["fg"] = self.fg
            cell["bg"] = self.bg

    def draw_cell(self, x, y, shape, fg=None, bg=None):
        if not self.in_bounds(x,y):
            return
        cell = self.buffer[self.index(x,y)]
        cell["shape"] = shape
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
                shape = cell["shape"]
                if shape is not None:
                    SHAPES[shape](ctx,px,py, self.cell_w, self.cell_h, cell["fg"])

    def draw_text_px(self, px,py, text, color, size=16, center=False):
        self.ctx.fillStyle = color
        self.ctx.font = "{}px monospace".format(size)
        self.ctx.textBaseline = "top"
        self.ctx.textAlign = "center" if center else "left"
        self.ctx.fillText(text,px,py)

    def draw_overlay(self,color):
        self.ctx.fillStyle = color
        self.ctx.fillRect(0,0, self.canvas.width, self.canvas.height)
