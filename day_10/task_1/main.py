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
    """For path counting, mover='person who moves' from 0 to 9 and calculate ways."""

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
                elif num == 9:
                    local_xy = (local_x, local_y)
                    self.end_points.append(local_xy)

    def print_SnE_points(self):
        """Print start and end points coordinates."""
        print("Start points:", self.start_points)
        print("End points:", self.end_points)

    def is_out_of_grid(self, x, y):
        """Check if a position is out of the grid bounds."""
        local_within_x_bounds = 0 <= x < len(self.grid[0])
        local_within_y_bounds = 0 <= y < len(self.grid)

        if not local_within_x_bounds or not local_within_y_bounds:
            return True

        return False

    def paths_from_one(self, start_point):
        """
        Perform mover to explore all paths starting from a given point.
        Return the number of unique height 9 positions reachable.
        """
        queue = [start_point]
        visited = set()
        reachable_nines = 0

        while queue:
            current_point = queue.pop(0)

            if current_point in visited:
                continue
            visited.add(current_point)

            current_x, current_y = current_point

            # Check if the current point is height 9
            if self.grid[current_y][current_x] == 9:
                reachable_nines += 1
                continue

            # Add valid neighbors to the queue using direction functions
            if self.can_left(current_point):
                queue.append((current_x - 1, current_y))
            if self.can_right(current_point):
                queue.append((current_x + 1, current_y))
            if self.can_up(current_point):
                queue.append((current_x, current_y - 1))
            if self.can_down(current_point):
                queue.append((current_x, current_y + 1))

        return reachable_nines

    def paths_from_all(self):
        """return all sums of paths' nines reacheble"""
        """in short: sum of the scores of all trailheads"""
        local_sum=0
        for start_point in self.start_points:
            local_sum += self.paths_from_one(start_point)

        return local_sum


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
    grid_instance = Grid(getInputFromFile("input.txt"))

    print("Grid:")
    grid_instance.pretty_print()

    mover_instance = Mover(grid_instance.grid)
    mover_instance.print_SnE_points()

    print(mover_instance.paths_from_all())
