from display import Display

d = Display()
d.ctx.fillStyle = d.bg
d.ctx.fillRect(0,0, d.canvas.width, d.canvas.height)
d.ctx.fillStyle = "#3a7bd5"
d.ctx.fillRect(50,50,200,120)