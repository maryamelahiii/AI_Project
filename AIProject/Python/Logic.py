import main

class Logic:
    phi = []
    m = 0
    n = 0
    p = 0


    def out_of_bounds(self, i, j , k, r):
        pass

    def overlaps(self, i1, j1, k1, r1, i2, j2, k2, r2):
        pass

    def same_color_and_neighbors(self, i1, j1, k1, r1, i2, j2, k2, r2):
        pass

    def overlaps_propositions(self):
        literal1 = []
        literal2 = []
        clause = []
        for i1 in range(self.m):
            for i2 in range(self.m):
                for j1 in range(self.n):
                    for j2 in range(self.n):
                        for k1 in range(self.p):
                            for k2 in range(self.p):
                                if k2 != k1:
                                    for r1 in range(4):
                                        for r2 in range(4):
                                            if (not self.out_of_bounds(i1, j1, k1, r1) and not self.out_of_bounds(i2, j2, k2, r2)):
                                                if self.overlaps(i1, j1, k1, r1, i2, j2, k2, r2):
                                                    literal1 = [0, i1, j1, k1, r1]
                                                    literal2 = [0, i2, j2, k2, r2]
                                                    clause = [literal1, literal2]
                                                    self.phi.append(clause)

    def out_of_bound_propositions(self):
        clause = []
        for i in range(self.m):
            for j in range(self.n):
                for k in range(self.p):
                    for r in range(4):
                        if self.out_of_bounds(i, j , k, r):
                            clause = [[0, i, j, k, r]]
                            self.phi.append(clause)

    def same_color_and_neighbors_propositions(self):
        literal1 = []
        literal2 = []
        clause = []
        for i1 in range(self.m):
            for i2 in range(self.m):
                for j1 in range(self.n):
                    for j2 in range(self.n):
                        for k1 in range(self.p):
                            for k2 in range(self.p):
                                if k1 != k2:
                                    for r1 in range(4):
                                        for r2 in range(4):
                                            if (not self.out_of_bounds(i1, j1, k1, r1) and not self.out_of_bounds(i2, j2, k2, r2)):
                                                    if self.same_color_and_neighbors(i1, j1, k1, r1, i2, j2, k2, r2):
                                                        literal1 = [0, i1, j1, k1, r1]
                                                        literal2 = [0, i2, j2, k2, r2]
                                                        clause = [literal1, literal2]
                                                        self.phi.append(clause)

    def all_tiles_propositions(self):
        for k in range(self.p):
            clause = []
            for i in range(self.m):
                for j in range(self.n):
                    for r in range(4):
                        literal = [1, i, j, k, r]
                        clause.append(literal)
            self.phi.append(clause)

    def one_tile_proposision(self):
        for k in range(self.p):
            clause = []
            for i1 in range(self.m):
                for j1 in range(self.n):
                    for r1 in range(4):
                        for i2 in range(self.m):
                            for j2 in range(self.n):
                                for r2 in range(4):
                                    if (i1 == i2 and j1 == j2):
                                        if (r1 != r2):
                                            literal1 = [0, i1, j1, k, r1]
                                            literal2 = [0, i2, j2, k, r2]
                                            clause = [literal1, literal2]
                                            self.phi.append(clause)
                                    else:
                                        literal1 = [0, i1, j1, k, r1]
                                        literal2 = [0, i2, j2, k, r2]
                                        clause = [literal1, literal2]
                                        self.phi.append(clause)

