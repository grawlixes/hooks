import Types

class Grid:
    # N (int) -> Positive integer that represents the number of hooks in the grid, and therefore the number of distinct integers that will be in the grid.
    # hooks (length-N list of Hooks) -> Serialization of the position of each hook in this grid. The Hook enum in Types.py describes the position of hook i, but to understand its exact position, you need the context provided by hooks [i+1, N] above it. The 1-hook technically doesn't deserve an entry, but for the sake of convenience, it'll be listed anyway.
    # rowAnnotations (list of Annotations) -> List of annotations for each row. Row i has an annotation represented by rowAnnotations[i], which will be None if there is no annotation.
    # colAnnotations (list of Annotations) - same as above, but with columns instead of rows.
    
    # solution (2D list of integers [0, N]) -> this grid's solution 
    def __init__(self):
        self.N = None
        self.hooks = None
        self.rowAnnotations = None
        self.colAnnotations = None

        self.solution = None

    # private methods
    
    def _doInputAssertions(self):
        assert(type(N) is int)
        assert(N >= 1)

    def _checkRowAnnotation(self, row):
        a = self.rowAnnotations[row]
        return a.match(grid[row])

    def _checkColAnnotation(self, col):
        a = self.colAnnotations[col]
        iterator = (grid[i][col] for i in range(self.N))
        return a.match(iterator)

    # public methods
    
    # generates the grid's solution
    def generate(self):
        self._doInputAssertions()
        
        # todo

        

# builder stuff
# can you tell I'm a Java programmer? this will be useful to support the multiple different presets that I want
class GridBuilder:
    def __init__(self):
        self.grid = Grid()

    def N(self, N):
        self.grid.N = N
        return self
   
    def hooks(self, hooks):
        self.grid.hooks = hooks 
        return self

    def rowAnnotations(self, rowAnnotations):
        self.grid.rowAnnotations = rowAnnotations
        return self

    def colAnnotations(self, colAnnotations):
        self.grid.colAnnotations = colAnnotations
        return self

    def build(self):
        self._setDefaults()

        return self.grid

    def _setDefaults(self):
        g = self.grid

        if not g.N:
            g.N = 9
        if not g.hooks:
            g.hooks = [Types.Hook.BOTTOM_RIGHT] * 8
