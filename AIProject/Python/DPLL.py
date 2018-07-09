class DPLL:
    literal = []
    clause = []
    phi = []

    def select_rotation(self, tile): #change rotation of a tile to the next option.
        if tile.rotation == 3:
            return False
        else:
            tile.rotation += 1

    def edge(self): #produce propositions that check tiles dont get out of edges of page
        pass

    def overlap(self): #produces propositions that check tiles dont overlap
        pass

    def neighbor_color(self): #produces prpositions that check the neighbors dont be same color
        pass

class Tile:
    rotation = 0 #0, 1, 2, 3
    pass