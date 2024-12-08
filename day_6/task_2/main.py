import copy


def read_input_as_grid(filename):
    """
    Reads the input file line by line and converts it into a 2D list.
    """
    with open(filename, "r") as file:
        lines = file.readlines()
        local_grid = [list(line.strip()) for line in lines]  # Converting each line to a list of characters
    return local_grid

def pretty_grid(local_grid):
    """Replacing symbols to human-readable words for better visualization."""
    local_pretty_grid = []
    for row in local_grid:
        pretty_row = []
        for element in row:
            match element:
                case ".":
                    pretty_element = "empty"
                case "#":
                    pretty_element = "barrier"
                case "^":
                    pretty_element = "guardUp"
                case "<":
                    pretty_element = "guardLeft"
                case ">":
                    pretty_element = "guardRight"
                case "v":
                    pretty_element = "guardDown"
                case _:
                    pretty_element = "unknown"
            pretty_row.append(pretty_element)
        local_pretty_grid.append(pretty_row)
    return local_pretty_grid

def short_grid(pretty_grid):
    """Converts the human-readable grid back to symbols."""
    local_short_grid = []
    for row in pretty_grid:
        short_row = []
        for element in row:
            match element:
                case "empty":
                    short_element = "."
                case "barrier":
                    short_element = "#"
                case "guardUp":
                    short_element = "^"
                case "guardLeft":
                    short_element = "<"
                case "guardRight":
                    short_element = ">"
                case "guardDown":
                    short_element = "v"
                case "path":
                    short_element = "X"
                case _:
                    short_element = "?"
            short_row.append(short_element)
        local_short_grid.append(short_row)
    return local_short_grid
class Guard:
    def __init__(self, local_grid):
        self.grid = local_grid
        self.visited_positions = set()
        self.visited_states = set()
        self.current_x = -1
        self.current_y = -1
        self.direction = "Up"
        self.out_of_map = False
        self.find_guard()
        self.max_x = len(self.grid[0]) - 1
        self.max_y = len(self.grid) - 1
        self.looped = False

    def find_guard(self):
        for y, row in enumerate(self.grid):
            for x, element in enumerate(row):
                if element in "^v<>":
                    self.current_y = y
                    self.current_x = x
                    self.direction = {
                        "^": "Up",
                        "v": "Down",
                        "<": "Left",
                        ">": "Right"
                    }[element]

    def move(self):
        self.check_and_redirect()
        self.mark_path()

        # Save the current state
        state = (self.current_x, self.current_y, self.direction)
        if state in self.visited_states:
            self.looped = True
            return
        self.visited_states.add(state)

        # Move based on direction
        match self.direction:
            case "Up":
                self.current_y -= 1
            case "Down":
                self.current_y += 1
            case "Left":
                self.current_x -= 1
            case "Right":
                self.current_x += 1

        self.check_in_area()
        self.mark_guard()

    def check_and_redirect(self):
        if self.out_of_map:
            return

        obstacle_ahead = False
        match self.direction:
            case "Up":
                obstacle_ahead = self.current_y > 0 and self.grid[self.current_y - 1][self.current_x] == "#"
            case "Down":
                obstacle_ahead = self.current_y < self.max_y and self.grid[self.current_y + 1][self.current_x] == "#"
            case "Left":
                obstacle_ahead = self.current_x > 0 and self.grid[self.current_y][self.current_x - 1] == "#"
            case "Right":
                obstacle_ahead = self.current_x < self.max_x and self.grid[self.current_y][self.current_x + 1] == "#"

        if obstacle_ahead:
            self.direction = {
                "Up": "Right",
                "Right": "Down",
                "Down": "Left",
                "Left": "Up"
            }[self.direction]

    def mark_path(self):
        if not self.out_of_map:
            self.visited_positions.add((self.current_x, self.current_y))
            self.grid[self.current_y][self.current_x] = "X"

    def mark_guard(self):
        if not self.out_of_map:
            self.grid[self.current_y][self.current_x] = {
                "Up": "^",
                "Down": "v",
                "Left": "<",
                "Right": ">"
            }[self.direction]

    def check_in_area(self):
        if (self.current_y < 0 or self.current_y > self.max_y or
            self.current_x < 0 or self.current_x > self.max_x):
            self.out_of_map = True

    def count_path(self):
        return len(self.visited_positions)

    def how_many_can_be_looped_by_one_more_barrier(self):
        loop_count = 0

        # Iterate over each position in the guard's path
        for y, row in enumerate(self.grid):
            for x, element in enumerate(row):
                cloned_grid = copy.deepcopy(self.grid)

            # Add a barrier at the position
                cloned_grid[y][x] = "#"

                print(f"Testing with barrier added at ({x}, {y}):")
                for row in cloned_grid:
                    print("".join(row))

                # Create a new guard instance with the modified grid
                test_guard = Guard(cloned_grid)

                # Simulate the guard's movement
                while not test_guard.out_of_map and not test_guard.looped:
                    test_guard.move()

                # Check and log whether the guard entered a loop
                if test_guard.looped:
                    print(f"Barrier at ({x}, {y}) caused a loop!")
                    loop_count += 1
                else:
                    print(f"Barrier at ({x}, {y}) did NOT cause a loop.")

        print(f"Total positions causing a loop: {loop_count}")
        return loop_count


def main1():
    grid = read_input_as_grid("test.txt")
    guard = Guard(grid)

    while not guard.out_of_map and not guard.looped:
        guard.move()

    if guard.looped:
        print("The guard has entered a loop!")
    else:
        print("Distinct positions visited:", guard.count_path())


def main2():
    grid = read_input_as_grid("test.txt")
    guard = Guard(grid)

    while not guard.out_of_map and not guard.looped:
        guard.move()

    if guard.looped:
        print("The guard has entered a loop!")
    else:
        print("Distinct positions visited:", guard.count_path())

    # Check how many loops can be caused by adding one more barrier
    possible_loops = guard.how_many_can_be_looped_by_one_more_barrier()
    print("Number of positions where adding a barrier causes looping:", possible_loops)


if __name__ == "__main__":
    main2()
