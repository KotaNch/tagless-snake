from rng import rand_int
WALL = 0
FLOOR = 1

TILE_SHAPE = {
    WALL: ("block", "#000000"),
    FLOOR: ("block", "#00ff00"),
}

class Room:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w =w
        self.h = h
    def center(self):
        return (self.x + self.w // 2, self.y + self.h //2)

    def intersects(self,other):
        return(
            self.x <= other.x + other.w and self.x + self.w >= other.x and self.y <= other.y + other.h and self.y + self.h >= other.y
        )

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
                shape, color = TILE_SHAPE[tile]
                display.draw_cell(x,y,shape,color)

    def carve_room(self, room):
        for y in range(room.y + 1, room.y + room.h):
            for x in range(room.x + 1, room.x + room.w):
                self.set(x,y, FLOOR)

    def generate(self, rng, max_rooms = 12, min_size = 5,max_size = 11):
        self.rooms = []
        for _ in range(max_rooms):
            w = rand_int(rng, min_size, max_size)
            h =rand_int(rng, min_size, max_size)
            x = rand_int(rng, 1, self.width - w -2)
            y = rand_int(rng,1,self.height -h -2)
            new_room = Room(x,y,w,h)

            ok = True
            for other in self.rooms:
                if new_room.intersects(other):
                    ok = False
                    break
            if not ok:
                continue

            self.carve_room(new_room)
            self.rooms.append(new_room)
        return self.rooms