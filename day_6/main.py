def read_input_as_grid(filename):
    """
    Reads the input file line by line and converts it into a 2D list.
    """
    with open(filename, "r") as file:
        lines = file.readlines()
        grid = [list(line.strip()) for line in lines]  # Converting each line to a list of characters
    return grid



if __name__ == "__main__":
    grid = read_input_as_grid("input.txt")
    for row in grid:
        print(row)
    print("full grid=")
    print(grid)
    print(grid[0])
    print(grid[0][4])