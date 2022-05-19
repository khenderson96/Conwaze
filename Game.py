from Graph import Graph

class Game:
    def __init__(self, dim, rounds, probability):
        self.graph = Graph(dim)
        self.graph.randomize(probability)

        i = 0
        if rounds != 0:
            while len(self.graph.liveCells) > 0 and i < rounds:
                print('round', i)
                self.graph.GOL()
                if len(self.graph.liveCells) == 0:
                    print('cells died at round', i)
                elif len(self.graph.liveCells) > 0 and i == rounds - 1:
                    print('cells lived through round', rounds)
                i += 1
        else:
            # potential infinite loop
            # fix: make steadyState list member for Graph,
            #      in updateNeighbors, if cell.state == True and cell.nextState == True, steadyState.append(cell.id)
            while len(self.graph.liveCells) > 0:
                self.graph.GOL()
                self.graph.prettyPrint()
                if len(self.graph.liveCells) == 0:
                    print('cells died at round', i)