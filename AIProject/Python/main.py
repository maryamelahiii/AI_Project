class Tile:
    def __init__(self):
        self.color = 0  # color of the tile
        self.shape = []  # 2D array showing the shape of the tile. '*' means that cell is filled and '.' means it's
        # empty.
        self.width = 0  # width of underlying rectangle
        self.height = 0  # height of underlying rectangle
        self.x = -1  # x coordinate of underlying rectangle. top left corner. Align with width
        self.y = -1  # y coordinate of underlying rectangle. top left corner. Align with height
        self.orientation = 0  # orientation of tile. 0 -> no rotation. 1 -> 90 degrees. 2 -> 180 degrees. 3 -> 270
        # degrees.
        self.cells = []  # relative coordinates of cells. (x,y) where x is align with width and y is align with height.
        self.boundsX = []  # array of tuples. (x0, y1, y2) where the range in which the line x = x0 is a bound of the
        #  shape is [y1,y2)
        self.boundsY = []  # array of tuples. (y0, x1, x2) where the range in which the line y = y0 is a bound of the
        #  shape is [x1,x2)
        self.domain = []  # array of tuples. (x, y, o) where x (align with width) and y (align with height) are the
        # coordinates of the top left corner of the underlying rectangle and 'o' is the orientation of the tile.

    def generate_cells(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.shape[j][i] == '*':
                    self.cells.append((i, j))

    def generate_domain(self, n, m):
        for i in range(m):
            for j in range(n):
                for k in range(4):
                    self.domain.append((i, j, 0))

    def generate_bounds_x(self):
        for i in range(self.width + 1):
            line_range = [0 for j in range(self.height)]
            for j in range(self.height):
                if i < self.width and i - 1 >= 0:  # has columns on both sides
                    if self.shape[j][i - 1] != self.shape[j][i]:
                        line_range[j] = 1
                elif i < self.width and i - 1 < 0:  # is at the left extremity of the rectangle
                    if self.shape[j][i] == '*':
                        line_range[j] = 1
                elif i >= self.width and i - 1 >= 0:  # is at the right extremity of the rectangle
                    if self.shape[j][i - 1] == '*':
                        line_range[j] = 1
            j = 0
            while j < len(line_range):
                while j < len(line_range) and line_range[j] == 0:
                    j += 1
                start = j
                while j < len(line_range) and line_range[j] == 1:
                    j += 1
                end = j
                if start != end:
                    self.boundsX.append((i, start, end))

    def generate_bounds_y(self):

        for i in range(self.height + 1):
            line_range = [0 for j in range(self.width)]
            for j in range(self.width):
                if i < self.height and i - 1 >= 0:  # has rows on both sides
                    if self.shape[i - 1][j] != self.shape[i][j]:
                        line_range[j] = 1
                elif i < self.height and i - 1 < 0:  # is at the top extremity of the rectangle
                    if self.shape[i][j] == '*':
                        line_range[j] = 1
                elif i >= self.height and i - 1 >= 0:  # is at the bottom extremity of the rectangle
                    if self.shape[i - 1][j] == '*':
                        line_range[j] = 1
            j = 0
            while j < len(line_range):
                while j < len(line_range) and line_range[j] == 0:
                    j += 1
                start = j
                while j < len(line_range) and line_range[j] == 1:
                    j += 1
                end = j
                if start != end:
                    self.boundsY.append((i, start, end))

    def overlaps(self, tile):

        if self.is_inside_rectangle(tile.x, tile.y) or \
                self.is_inside_rectangle(tile.x + tile.width, tile.y) or \
                self.is_inside_rectangle(tile.x + tile.width, tile.y + tile.height) or \
                self.is_inside_rectangle(tile.x, tile.y + tile.height):
            # TODO implement
            # check if overlapping area is filled. condition in if is trash
            return True
        elif tile.is_inside_rectangle(self.x, self.y) or \
                tile.is_inside_rectangle(self.x + self.width, self.y) or \
                tile.is_inside_rectangle(self.x + self.width, self.y + self.height) or \
                tile.is_inside_rectangle(self.x, self.y + self.height):
            # TODO implement
            # check if overlapping area is filled. condition in if is trash
            return True
        else:
            return False

    def same_color_and_neighbors(self, tile):
        if tile.color == self.color:
            # TODO implement
            # check if they are neighbor
            return True
        else:
            return False
        pass

    def out_of_bound(self):
        # TODO implement
        pass

    def is_inside_rectangle(self, x, y):  # x is align with width and y is align with height
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False

    def relative_position(self, tile):
        return (self.is_inside_rectangle(tile.x, tile.y),
                self.is_inside_rectangle(tile.x + tile.width, tile.y),
                self.is_inside_rectangle(tile.x + tile.width, tile.y + tile.height),
                self.is_inside_rectangle(tile.x, tile.y + tile.height))


# n is align with height
# m is align with width
n, m, p = input().split()
n, m, p = int(n), int(m), int(p)
tiles = []

for i in range(p):
    tile = Tile()
    k, c = input().split()
    k, c = int(k), int(c)
    tile.color = c
    tile.height = k
    shape = [[1] for l in range(k)]
    for j in range(k):
        shape[j] = input().split()
    tile.width = len(shape[k - 1])
    tile.shape = shape
    # tile.generate_bounds_x()
    # tile.generate_bounds_y()
    tile.generate_cells()
    tile.generate_domain(n, m)
    tiles += [tile]

for tile in tiles:
    # print(tile.shape)
    # print(str(tile.height) + ", " + str(tile.width))
    # print("X: " + str(tile.boundsX))
    # print("Y: " + str(tile.boundsY))
    print(tile.cells)


# TODO check if the tile has been assigned a coordinate. Check to see if x and y are -1 or not.

# 5 8 2
# 4 1
# * . . *
# * * * *
# * * * *
# * * * *
# 1 2
# * * * *
