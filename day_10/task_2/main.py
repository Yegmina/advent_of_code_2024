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
    """For path counting, mover='person who moves' from 0 to 9 and calculates ways."""

    def __init__(self, grid):
        super().__init__(grid)
        self.start_points = []
        self.end_points = []
        self.cache = {}  # Cache for memoizing path counts in DFS

        # Find all start (0) and end (9) points
        for local_y, row in enumerate(self.grid):
            for local_x, num in enumerate(row):
                if num == 0:
                    self.start_points.append((local_x, local_y))
                elif num == 9:
                    self.end_points.append((local_x, local_y))

    def print_SnE_points(self):
        """Print start and end points coordinates."""
        print("Start points:", self.start_points)
        print("End points:", self.end_points)


    def is_out_of_grid(self, x, y):
        """Check if a position is out of the grid bounds."""
        return not (0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid))

    def count_paths_from(self, current_point):
        """
        Perform DFS to count distinct paths starting from a given point.
        Returns the number of paths ending at height 9.
        """
        if current_point in self.cache:
            return self.cache[current_point]

        current_x, current_y = current_point
        current_height = self.grid[current_y][current_x]

        # Base case: if the current point is height 9, count this as a valid path
        if current_height == 9:
            return 1

        # Explore neighbors using direction methods
        total_paths = 0

        # Check if a move is possible in each direction
        if self.can_left(current_point):
            total_paths += self.count_paths_from((current_x - 1, current_y))

        if self.can_right(current_point):
            total_paths += self.count_paths_from((current_x + 1, current_y))

        if self.can_up(current_point):
            total_paths += self.count_paths_from((current_x, current_y - 1))

        if self.can_down(current_point):
            total_paths += self.count_paths_from((current_x, current_y + 1))

        # Cache the result for the current point
        self.cache[current_point] = total_paths
        return total_paths

    def calculate_total_rating(self):
        """Calculate the total rating (sum of distinct paths from all trailheads)."""
        total_rating = 0
        for start_point in self.start_points:
            total_rating += self.count_paths_from(start_point)
        return total_rating

    def can_move_one_step(self, local_current_point, local_next_point):
        """Sub function for can_left, can_right etc."""
        local_current_x, local_current_y = local_current_point
        local_next_x, local_next_y = local_next_point

        if not self.is_out_of_grid(local_next_x, local_next_y):
            local_current_value = self.grid[local_current_y][local_current_x]
            local_next_value = self.grid[local_next_y][local_next_x]
            difference_value = local_next_value - local_current_value
            if difference_value == 1:
                return True

        return False

    def can_left(self, local_current_point):
        """Return true if mover can go one step left."""
        local_current_x, local_current_y = local_current_point
        local_next_x, local_next_y = local_current_x - 1, local_current_y
        return self.can_move_one_step((local_current_x, local_current_y), (local_next_x, local_next_y))

    def can_right(self, local_current_point):
        """Return true if mover can go one step right."""
        local_current_x, local_current_y = local_current_point
        local_next_x, local_next_y = local_current_x + 1, local_current_y
        return self.can_move_one_step((local_current_x, local_current_y), (local_next_x, local_next_y))

    def can_up(self, local_current_point):
        """Return true if mover can go one step up."""
        local_current_x, local_current_y = local_current_point
        local_next_x, local_next_y = local_current_x, local_current_y - 1
        return self.can_move_one_step((local_current_x, local_current_y), (local_next_x, local_next_y))

    def can_down(self, local_current_point):
        """Return true if mover can go one step down."""
        local_current_x, local_current_y = local_current_point
        local_next_x, local_next_y = local_current_x, local_current_y + 1
        return self.can_move_one_step((local_current_x, local_current_y), (local_next_x, local_next_y))


if __name__ == "__main__":
    # Read the grid
    grid_instance = Grid(getInputFromFile("input.txt"))

    # Print the grid
    print("Grid:")
    grid_instance.pretty_print()

    # Initialize the Mover instance
    mover_instance = Mover(grid_instance.grid)
    mover_instance.print_SnE_points()

    # Calculate and print the total rating (sum of all trailhead ratings)
    total_rating = mover_instance.calculate_total_rating()
    print(f"Total rating (sum of trailhead ratings): {total_rating}")
