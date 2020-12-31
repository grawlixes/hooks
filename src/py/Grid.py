import Types

class Grid:
    # N (int) -> Positive integer that represents the number of hooks in the grid, and therefore the number of distinct integers that will be in the grid.
    # hooks (length-N list of Hooks) -> Serialization of the position of each hook in this grid. The Hook enum in Types.py describes the position of hook i, but to understand its exact position, you need the context provided by hooks [i+1, N] above it. The 1-hook technically doesn't deserve an entry, but for the sake of convenience, it'll be listed anyway.
    # grid (2D list of ints) -> The actual grid.
    # rowAnnotations (list of Annotations) -> List of annotations for each row. Row i has an annotation represented by rowAnnotations[i], which will be None if there is no annotation.
    # colAnnotations (list of Annotations) - same as above, but with columns instead of rows.
    def __init__(self, N = 9, hooks = None):
        self.N = N
        self.hooks = []
        self.grid = []
        self.rowAnnotations = []
        self.colAnnotations = []

        self._doInputAssertions()
        self._generate()

    def _doInputAssertions(self):
        assert(N >= 1)

    def _generate(self):
        pass 
