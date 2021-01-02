# Hook Puzzle Generator

This is a repository with code to automatically generate "Hook" puzzles, popularized (and perhaps invented?) by the folks at [Jane Street](https://www.janestreet.com/puzzles).

Hook puzzles are logical puzzles similar to Sudoku, but they usually involve a bit more math. Generally, a hook puzzle involves filling a 9x9 grid with numbers 1-9; each number, N, from 1-9 should be placed in an L-shaped "hook" of size 2N - 1. Furthermore, each number N should appear exactly N times (so 1 appears once, 2 appears 2 times, ..., 9 appears 9 times) inside its respective hook. 

[Here's an example](https://www.janestreet.com/puzzles/wp-content/uploads/2014/01/Feb14_Niedermaier.jpg) of a hook puzzle with all "hooks" unfilled except the 1-hook. In each hook of size 2N - 1, we'd insert N copies of the number N. The numbers outside of the grid indicate properties about the numbers we should place in their respective rows and columns; in this example, the number outside a row or column indicates the sum of all the numbers inside it.

The above example is a relatively easy one, but it's an older variant of hook puzzles. In the more recent variants posted by Jane Street, the following properties also hold to add challenge:

- Not all of the rows and columns have annotation numbers; some of them are blank.
- The hooks are unlabeled; you have to decide where to place them.
- The numbers in each cell should form a single [connected component](https://en.wikipedia.org/wiki/Component_(graph_theory)) with one another.
- In every 2x2 set of cells in the resulting grid, there should be at least one empty cell.

On top of this, there are many different things that the annotation numbers outside of the rows and columns can mean. In the above example, they're the sum of each number in that row or column, but in others they might be the [greatest common factor of those numbers](https://www.janestreet.com/puzzles/hooks-6/) or the [sum of concatenated numbers looking from that direction](https://www.janestreet.com/puzzles/hooks-5).

In this puzzle-generation tool, I'm going to try to support these use cases (not necessarily in the first version, but eventually):

- Different options for the type and frequency of annotations, and control over whether or not the hooks' positions will be given from the start
- Ensure that each puzzle is **human-solvable** (I'll provide more information on what this means later) 
- Ensure that each puzzle has exactly one solution
- Different difficulty modes with certain option presets - for example, "Beginner mode" would have presets like the first example shown above (nine hooks in place with simple annotations on each row or column). On the other hand, "Expert mode" might have random hook positions with fewer, and less helpful, annotations.
- UI, probably in the form of a website. I should really clean up my personal website anyway, so this will probably be a part of that.

Here are some things that would be nice to have, but they are not important enough to prioritize right now:

- Option to have more than 9 hooks
