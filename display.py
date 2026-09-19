from browser import document, window

class Display:
    def __init__(self, width=800, height=600, bg="#101014"):
        self.bg =bg

        self.canvas = document.createElement("canvas")
        self.canvas.width = width
        self.canvas.height = height
        self.ctx = self.canvas.getContext("2d")

        body = document.body
        body.style.margin = "0"
        body.style.background = bg
        body.style.display = "grid"
        body.style.placeItems = "center"
        body.style.minHeight = "100vh"

        document.body.appendChild(self.canvas)