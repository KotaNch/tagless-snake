WALL = 0
FLOOR = 1

TILE_GLYPH = {
    WALL: ("#", "#585858"),
    FLOOR: (".", "#3a3a3a"),
}

class GameMap:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.tiles = []
        for _ in range(width * height):
            self.tiles.append(WALL)
    def index(self, x,y):
        return y * self.width +x

    def in_bounds(self, x,y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get(self, x, y):
        return self.tiles[self.index(x,y)]

    def set(self,x,y,tile):
        if self.in_bounds(x,y):
            self.tiles[self.index(x,y)] = tile

    def draw(self, display):
        for y in range(self.height):
            for x in range(self.width):
                tile = self.tiles[self.index(x,y)]
                ch, fg = TILE_GLYPH[tile]
                display.draw_glyph(x,y,ch,fg)