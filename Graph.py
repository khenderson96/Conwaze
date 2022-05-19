import random

class Graph:
    def __init__(self, dim):
        self.cells = []
        self.liveCells = set()
        id = 0
        for x in range(dim):
            for y in range(dim):
                self.cells.append(Cell(id, x, y, dim, False))
                id += 1

    def randomize(self, probability):
        for c in self.cells:
            if random.uniform(0, 1) <= probability:
                c.state = True
                self.liveCells.add(c.id)
        self.updateAllNeighbors()

    def updateAllNeighbors(self):
        for c in self.cells:
            c.liveNeighbors.clear()
            for n in c.neighbors:
                if self.cells[n].state == True:
                    c.liveNeighbors.append(n)

    def GOL(self):
        for c in self.cells:
            if c.state == True and len(c.liveNeighbors) < 2:
                c.nextState = False
                self.liveCells.remove(c.id)
            elif c.state == True and 2 <= len(c.liveNeighbors) <= 3:
                c.nextState = True
                self.liveCells.add(c.id)
            elif c.state == True and len(c.liveNeighbors) > 3:
                c.nextState = False
                self.liveCells.remove(c.id)
            elif c.state == False and len(c.liveNeighbors) == 3:
                c.nextState = True
                self.liveCells.add(c.id)
        self.prettyPrint()
        for c in self.cells:
            c.state = c.nextState
        self.updateAllNeighbors()

    def prettyPrint(self):
        print('{:<3} {:<32} {:<12} {:<5}'.format('id', 'neighbors', 'this/next',
                                                'live neighbors'))
        for c in self.cells:
            line_new = '{:<3} {:<35} {:<1}/{:<7} {:<5}'.format(
                c.id, str(c.neighbors), c.state, c.nextState, str(c.liveNeighbors))
            print(line_new)
        print('live cells:', self.liveCells, '\n')


class Cell:
    def __init__(self, id, x, y, dim, state):
        self.id = id
        self.x, self.y = x, y
        self.state = state
        self.nextState = state
        self.neighbors = []
        self.liveNeighbors = []
        self.getNeighbors(dim)

    def getNeighbors(self, dim):
        if self.id == 0:  # bottom left
            self.neighbors.append(self.id + 1)
            self.neighbors.append(self.id + dim)
            self.neighbors.append(self.id + dim + 1)
        elif self.id % dim == 0:  # left
            self.neighbors.append(self.id - dim)
            self.neighbors.append(self.id - dim + 1)
            self.neighbors.append(self.id + 1)
            self.neighbors.append(self.id + dim)
            self.neighbors.append(self.id + dim + 1)
        elif self.id == dim * (dim - 1):  # top left
            self.neighbors.append(self.id - dim)
            self.neighbors.append(self.id - dim + 1)
            self.neighbors.append(self.id + 1)
        elif self.id == dim - 1:  # bottom right
            self.neighbors.append(self.id - 1)
            self.neighbors.append(self.id + dim - 1)
            self.neighbors.append(self.id + dim)
        elif self.id == dim * dim - 1:  # top right
            self.neighbors.append(self.id - dim - 1)
            self.neighbors.append(self.id - dim)
            self.neighbors.append(self.id - 1)
        elif self.id % dim == dim - 1:  # right
            self.neighbors.append(self.id - dim - 1)
            self.neighbors.append(self.id - dim)
            self.neighbors.append(self.id - 1)
            self.neighbors.append(self.id + dim - 1)
            self.neighbors.append(self.id + dim)
        elif self.id > dim * (dim - 1) and self.id < dim * dim - 1:  # bottom
            self.neighbors.append(self.id - dim - 1)
            self.neighbors.append(self.id - dim)
            self.neighbors.append(self.id - dim + 1)
            self.neighbors.append(self.id - 1)
            self.neighbors.append(self.id + 1)
        elif self.id > 0 and self.id < dim - 1:  # top
            self.neighbors.append(self.id - 1)
            self.neighbors.append(self.id + 1)
            self.neighbors.append(self.id + dim - 1)
            self.neighbors.append(self.id + dim)
            self.neighbors.append(self.id + dim + 1)
        else:  # central (No border)
            self.neighbors.append(self.id - dim - 1)
            self.neighbors.append(self.id - dim)
            self.neighbors.append(self.id - dim + 1)
            self.neighbors.append(self.id - 1)
            self.neighbors.append(self.id + 1)
            self.neighbors.append(self.id + dim - 1)
            self.neighbors.append(self.id + dim)
            self.neighbors.append(self.id + dim + 1)

        #temporary bug fix for MAX(id): has neighbor > MAX(id)
        self.neighbors = [
            c for c in self.neighbors if c >= 0 and c < dim * dim - 1
        ]
