from copy import deepcopy
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def read_input_as_grid(file_path):
    """
    Reads the input file and converts it into a 2D list of characters.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
        return [list(line.strip()) for line in lines]


class Guard:
    def __init__(self, grid):
        self.grid = grid
        self.start_position = self.find_start_position()
        self.direction = -1  # Initially moving up
        self.right_turn = -1j  # Right turn in complex numbers
        self.visited_positions = set()

    def find_start_position(self):
        """
        Locate the starting position of the guard marked with '^'.
        """
        for y, row in enumerate(self.grid):
            for x, element in enumerate(row):
                if element == "^":
                    return complex(y, x)
        raise ValueError("Starting position not found in the grid.")

    def traverse_grid(self):
        """
        Simulate the guard's movement through the grid.
        """
        position = self.start_position
        direction = self.direction
        visited_states = set()

        while True:
            if not (0 <= position.real < len(self.grid) and 0 <= position.imag < len(self.grid[0])):
                break  # Out of bounds

            state = (position, direction)
            if state in visited_states:
                return False, visited_states  # Loop detected

            visited_states.add(state)
            self.visited_positions.add(position)

            next_position = position + direction
            try:
                if self.grid[int(next_position.real)][int(next_position.imag)] == "#":
                    direction *= self.right_turn  # Turn right if a wall is encountered
                else:
                    position = next_position
            except IndexError:
                break  # Out of bounds

        return True, visited_states  # Completed traversal

    def find_loop_spots(self):
        """
        Find all positions where adding an obstruction gets the guard stuck in a loop.
        """
        loop_spots = set()
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if self.grid[y][x] == ".":
                    test_grid = deepcopy(self.grid)
                    test_grid[y][x] = "#"

                    patrol = Guard(test_grid)
                    completed, visited_states = patrol.traverse_grid()

                    if not completed:  # If the guard gets stuck in a loop
                        loop_spots.add(complex(y, x))

        return loop_spots


def main():
    grid = read_input_as_grid("input.txt")
    patrol = Guard(grid)

    loop_spots = patrol.find_loop_spots()
    print("Number of loop spots:", len(loop_spots))


if __name__ == "__main__":
    main()
