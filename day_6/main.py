def read_input_as_grid(filename):
    """
    Reads the input file line by line and converts it into a 2D list.
    """
    with open(filename, "r") as file:
        lines = file.readlines()
        grid = [list(line.strip()) for line in lines]  # Converting each line to a list of characters
    return grid

def print_test(grid):
    for row in grid:
        print(row)
    print("full grid=")
    print(pretty_grid(grid))



def pretty_grid(grid):
    """Replacing symbols to human language words, just to make it look better"""
    pretty_grid = []
    for row in grid:
        pretty_row=[]
        for element in row:
            match element:
                case ".":
                    pretty_element="empty"

                case "#":
                    pretty_element="barrier"
                case "^":
                    pretty_element="guardUp"
                case _:
                    print(f"Unexpected symbol, {element}")
                    pretty_element="?"
            pretty_row.append(pretty_element)
        pretty_grid.append(pretty_row)

    return pretty_grid

if __name__ == "__main__":
    grid = read_input_as_grid("input.txt")
    print_test(grid)
