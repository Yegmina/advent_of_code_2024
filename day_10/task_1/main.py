def getInputFromFile(local_file_name):
    """Read the input file and convert it into a 2D grid of integers."""
    with open(local_file_name, "r") as file:
        lines = file.readlines()

    local_grid = []
    for line in lines:
        clean_line = line.strip()
        row = []
        for char in clean_line:
            if char == "." or char == "," or char == "?":
                row.append(-1) # for debug and test
            else:
                row.append(int(char))

        local_grid.append(row)

    return local_grid

class Grid:
    def __init__(self, grid):
        self.grid = grid

    def pretty_print(self):
        """Print grid line by line"""
        for row in self.grid:
            print(row)

class Mover(Grid):
    """for path counting, mover='person who move' from 0 to 9 and calculate ways """

    def __init__(self, grid):
        super().__init__(grid)
        self.start_points = []
        self.end_points = []

        # Find all start (0) and end (9) points
        for local_y, row in enumerate(self.grid):
            for local_x, num in enumerate(row):
                if num == 0:
                    local_xy = (local_x, local_y)
                    self.start_points.append(local_xy)
                if num == 9:
                    local_xy = (local_x, local_y)
                    self.end_points.append(local_xy)

    def print_SnE_points(self):
        """Print start and end points coordinates."""
        print("Start points:", self.start_points)
        print("End points:", self.end_points)



if __name__ == "__main__":
    grid_instance = Grid(getInputFromFile("input.txt"))

    print("Grid:")
    grid_instance.pretty_print()

    mover_instance = Mover(grid_instance.grid)

    mover_instance.print_SnE_points()

