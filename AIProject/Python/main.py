class Tile:
    def __init__(self):
        self.color = 0  # color of the tile
        self.shape = []  # 2D array showing the shape of the tile. '*' means that cell is filled and '.' means it's
        # empty.
        self.width = 0  # width of underlying rectangle
        self.height = 0  # height of underlying rectangle
        self.x = -1  # x coordinate of underlying rectangle. top left corner. Align with height
        self.y = -1  # y coordinate of underlying rectangle. top left corner. Align with width
        self.rotation = 0  # rotation of tile. 0 -> no rotation. 1 -> 90 degrees. 2 -> 180 degrees. 3 -> 270
        # degrees.
        self.cells_zero = []  # relative coordinates of cells when orientation of tile is zero. (x,y) where x is
        # align with height and y is align with width.
        self.cells_one = []  # relative coordinates of cells when orientation of tile is one. (x,y) where x is
        # align with height and y is align with width.
        self.cells_two = []  # relative coordinates of cells when orientation of tile is two. (x,y) where x is
        # align with height and y is align with width.
        self.cells_three = []  # relative coordinates of cells when orientation of tile is three. (x,y) where x is
        # align with height and y is align with width.
        self.boundsX = []  # array of tuples. (x0, y1, y2) where the range in which the line x = x0 is a bound of the
        #  shape is [y1,y2)
        self.boundsY = []  # array of tuples. (y0, x1, x2) where the range in which the line y = y0 is a bound of the
        #  shape is [x1,x2)
        self.domain = []  # array of tuples. (x, y, r) where x (align with height) and y (align with width) are the
        # coordinates of the top left corner of the underlying rectangle and 'o' is the rotation of the tile.

    def generate_cells_zero(self):
        x = 0
        for i in range(self.height):
            y = 0
            for j in range(self.width):
                if self.shape[i][j] == '*':
                    self.cells_zero.append((x, y))
                y += 1
            x += 1

    def generate_cells_one(self):
        x = 0
        for j in range(self.width - 1, -1, -1):
            y = 0
            for i in range(self.height):
                if self.shape[i][j] == '*':
                    self.cells_one.append((x, y))
                y += 1
            x += 1

    def generate_cells_two(self):
        x = 0
        for i in range(self.height - 1, -1, -1):
            y = 0
            for j in range(self.width - 1, -1, -1):
                if self.shape[i][j] == '*':
                    self.cells_two.append((x, y))
                y += 1
            x += 1

    def generate_cells_three(self):
        x = 0
        for j in range(self.width):
            y = 0
            for i in range(self.height - 1, -1, -1):
                if self.shape[i][j] == '*':
                    self.cells_three.append((x, y))
                y += 1
            x += 1

    def generate_domain(self, n, m):
        for i in range(m):
            for j in range(n):
                for k in range(4):
                    self.domain.append((i, j, k))

    def overlaps(self, tile):
        if self.rotation == 0 and tile.rotation == 0:
            if Tile.zero_zero_check_overlap(self, tile):
                return True
            return False
        elif self.rotation == 0 and tile.rotation == 1:
            if Tile.zero_one_check_overlap(self, tile):
                return True
            return False
        elif self.rotation == 0 and tile.rotation == 2:
            if Tile.zero_two_check_overlap(self, tile):
                return True
            return False
        elif self.rotation == 0 and tile.rotation == 3:
            if Tile.zero_three_check_overlap(self, tile):
                return True
            return False
        elif self.rotation == 1 and tile.rotation == 0:
            if Tile.one_zero_check_overlap(self, tile):
                return True
            return False
        elif self.rotation == 1 and tile.rotation == 1:
            if Tile.one_one_check_overlap(self, tile):
                return True
            return False
        elif self.rotation == 1 and tile.rotation == 2:
            if Tile.one_two_check_overlap(self, tile):
                return True
            return False
        elif self.rotation == 1 and tile.rotation == 3:
            if Tile.one_three_check_overlap(self, tile):
                return True
            return False
        elif self.rotation == 2 and tile.rotation == 0:
            if Tile.two_zero_check_overlap(self, tile):
                return True
            return False
        elif self.rotation == 2 and tile.rotation == 1:
            if Tile.two_one_check_overlap(self, tile):
                return True
            return False
        elif self.rotation == 2 and tile.rotation == 2:
            if Tile.two_two_check_overlap(self, tile):
                return True
            return False
        elif self.rotation == 2 and tile.rotation == 3:
            if Tile.two_three_check_overlap(self, tile):
                return True
            return False
        elif self.rotation == 3 and tile.rotation == 0:
            if Tile.three_zero_check_overlap(self, tile):
                return True
            return False
        elif self.rotation == 3 and tile.rotation == 1:
            if Tile.three_one_check_overlap(self, tile):
                return True
            return False
        elif self.rotation == 3 and tile.rotation == 2:
            if Tile.three_two_check_overlap(self, tile):
                return True
            return False
        elif self.rotation == 3 and tile.rotation == 3:
            if Tile.three_three_check_overlap(self, tile):
                return True
            return False
        return False

    @staticmethod
    def zero_zero_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_zero:
            for cell2 in tile2.cells_zero:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    @staticmethod
    def zero_one_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_zero:
            for cell2 in tile2.cells_one:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    @staticmethod
    def zero_two_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_zero:
            for cell2 in tile2.cells_two:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    @staticmethod
    def zero_three_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_zero:
            for cell2 in tile2.cells_three:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    @staticmethod
    def one_zero_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_one:
            for cell2 in tile2.cells_zero:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    @staticmethod
    def one_one_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_one:
            for cell2 in tile2.cells_one:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    @staticmethod
    def one_two_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_one:
            for cell2 in tile2.cells_two:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    @staticmethod
    def one_three_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_one:
            for cell2 in tile2.cells_three:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    @staticmethod
    def two_zero_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_two:
            for cell2 in tile2.cells_zero:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    @staticmethod
    def two_one_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_two:
            for cell2 in tile2.cells_one:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    @staticmethod
    def two_two_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_two:
            for cell2 in tile2.cells_two:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    @staticmethod
    def two_three_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_two:
            for cell2 in tile2.cells_three:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    @staticmethod
    def three_zero_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_three:
            for cell2 in tile2.cells_zero:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    @staticmethod
    def three_one_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_three:
            for cell2 in tile2.cells_one:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    @staticmethod
    def three_two_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_three:
            for cell2 in tile2.cells_two:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    @staticmethod
    def three_three_check_overlap(tile1, tile2):
        for cell1 in tile1.cells_three:
            for cell2 in tile2.cells_three:
                if cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
        return False

    def same_color_and_neighbors(self, tile):
        if tile.color == self.color:
            if self.rotation == 0 and tile.rotation == 0:
                if Tile.zero_zero_check_neighbor(self, tile):
                    return True
                return False
            elif self.rotation == 0 and tile.rotation == 1:
                if Tile.zero_one_check_neighbor(self, tile):
                    return True
                return False
            elif self.rotation == 0 and tile.rotation == 2:
                if Tile.zero_two_check_neighbor(self, tile):
                    return True
                return False
            elif self.rotation == 0 and tile.rotation == 3:
                if Tile.zero_three_check_neighbor(self, tile):
                    return True
                return False
            elif self.rotation == 1 and tile.rotation == 0:
                if Tile.one_zero_check_neighbor(self, tile):
                    return True
                return False
            elif self.rotation == 1 and tile.rotation == 1:
                if Tile.one_one_check_neighbor(self, tile):
                    return True
                return False
            elif self.rotation == 1 and tile.rotation == 2:
                if Tile.one_two_check_neighbor(self, tile):
                    return True
                return False
            elif self.rotation == 1 and tile.rotation == 3:
                if Tile.one_three_check_neighbor(self, tile):
                    return True
                return False
            elif self.rotation == 2 and tile.rotation == 0:
                if Tile.two_zero_check_neighbor(self, tile):
                    return True
                return False
            elif self.rotation == 2 and tile.rotation == 1:
                if Tile.two_one_check_neighbor(self, tile):
                    return True
                return False
            elif self.rotation == 2 and tile.rotation == 2:
                if Tile.two_two_check_neighbor(self, tile):
                    return True
                return False
            elif self.rotation == 2 and tile.rotation == 3:
                if Tile.two_three_check_neighbor(self, tile):
                    return True
                return False
            elif self.rotation == 3 and tile.rotation == 0:
                if Tile.three_zero_check_neighbor(self, tile):
                    return True
                return False
            elif self.rotation == 3 and tile.rotation == 1:
                if Tile.three_one_check_neighbor(self, tile):
                    return True
                return False
            elif self.rotation == 3 and tile.rotation == 2:
                if Tile.three_two_check_neighbor(self, tile):
                    return True
                return False
            elif self.rotation == 3 and tile.rotation == 3:
                if Tile.three_three_check_neighbor(self, tile):
                    return True
                return False
            return False
        else:
            return False

    @staticmethod
    def zero_zero_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_zero:
            for cell2 in tile2.cells_zero:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    @staticmethod
    def zero_one_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_zero:
            for cell2 in tile2.cells_one:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    @staticmethod
    def zero_two_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_zero:
            for cell2 in tile2.cells_two:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    @staticmethod
    def zero_three_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_zero:
            for cell2 in tile2.cells_three:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    @staticmethod
    def one_zero_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_one:
            for cell2 in tile2.cells_zero:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    @staticmethod
    def one_one_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_one:
            for cell2 in tile2.cells_one:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    @staticmethod
    def one_two_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_one:
            for cell2 in tile2.cells_two:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    @staticmethod
    def one_three_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_one:
            for cell2 in tile2.cells_three:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    @staticmethod
    def two_zero_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_two:
            for cell2 in tile2.cells_zero:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    @staticmethod
    def two_one_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_two:
            for cell2 in tile2.cells_one:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    @staticmethod
    def two_two_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_two:
            for cell2 in tile2.cells_two:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    @staticmethod
    def two_three_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_two:
            for cell2 in tile2.cells_three:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    @staticmethod
    def three_zero_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_three:
            for cell2 in tile2.cells_zero:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    @staticmethod
    def three_one_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_three:
            for cell2 in tile2.cells_one:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    @staticmethod
    def three_two_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_three:
            for cell2 in tile2.cells_two:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    @staticmethod
    def three_three_check_neighbor(tile1, tile2):
        for cell1 in tile1.cells_three:
            for cell2 in tile2.cells_three:
                if cell1[0] + tile1.x == cell2[0] + tile2.x + 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x - 1 and cell1[1] + tile1.y == cell2[1] + tile2.y:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y + 1:
                    return True
                elif cell1[0] + tile1.x == cell2[0] + tile2.x and cell1[1] + tile1.y == cell2[1] + tile2.y - 1:
                    return True
        return False

    def out_of_bound(self, n, m):
        cells = []
        if self.rotation == 0:
            cells = self.cells_zero
        elif self.rotation == 1:
            cells = self.cells_one
        elif self.rotation == 2:
            cells = self.cells_two
        elif self.rotation == 3:
            cells = self.cells_three
        for cell in cells:
            if cell[0] + self.x >= n or cell[1] + self.y >= m:
                return True
        return False

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
    tile.generate_cells_zero()
    tile.generate_cells_one()
    tile.generate_cells_two()
    tile.generate_cells_three()
    tile.generate_domain(n, m)
    tiles += [tile]

for tile in tiles:
    print("Zero: " + str(tile.cells_zero))
    print("One: " + str(tile.cells_one))
    print("Two: " + str(tile.cells_two))
    print("Three: " + str(tile.cells_three))
# TODO check if the tile has been assigned a coordinate. Check to see if x and y are -1 or not.
# 5 8 2
# 4 1
# * . . *
# * * * *
# * * * *
# * * * *
# 1 2
# * * * *
