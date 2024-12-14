def getInputFromFile(local_file_name):
    """Read the input file and convert it into a 2D grid of integers."""
    with open(local_file_name, "r") as file:
        lines = file.readlines()

    local_grid = []
    for line in lines:
        clean_line = line.strip()  # Remove any trailing whitespace
        row = []
        for char in clean_line:
            row.append(int(char))  # Convert each character to an integer
        local_grid.append(row)

    return local_grid

class Grid:
    def __init__(self, grid):
        self.grid=grid

    def pretty_print(self):
        for row in self.grid:
            print(row)



grid_instance=Grid(getInputFromFile("input.txt"))

grid_instance.pretty_print()
