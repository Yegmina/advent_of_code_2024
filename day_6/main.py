def read_input_as_grid(filename):
    """
    Reads the input file line by line and converts it into a 2D list.
    """
    with open(filename, "r") as file:
        lines = file.readlines()
        local_grid = [list(line.strip()) for line in lines]  # Converting each line to a list of characters
    return local_grid

def print_test(local_grid):
    for row in local_grid:
        print(row)
    print("full grid=")
    print(pretty_grid(local_grid))



def pretty_grid(local_grid):
    """Replacing symbols to human language words, just to make it look better"""
    local_pretty_grid = []
    for row in local_grid:
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
        local_pretty_grid.append(pretty_row)

    return local_pretty_grid


class Guard:
    def __init__(self, local_grid):
        self.grid = local_grid
        self.x=[]  # list   of X coordinates where guard was
        self.y=[]  # list   of Y coordinates where guard was
        self.current_x=-1
        self.current_y=-1
        self.direction="Up"
        self.out_of_map=False
        self.find_guard()
        self.max_x=len(grid)-1
        self.max_y=len(grid[0])-1


    def find_guard(self):
        for i_row, row in enumerate(self.grid):
            for i_element, element in enumerate(row):
                match element:
                    case "guardUp":
                        self.current_y=i_row
                        self.current_x=i_element
                        self.direction="Up"
                    case "guardDown":
                        self.current_y=i_row
                        self.current_x=i_element
                        self.direction="Down"
                    case "guardLeft":
                        self.current_y=i_row
                        self.current_x=i_element
                        self.direction="Left"
                    case "guardRight":
                        self.current_y=i_row
                        self.current_x=i_element
                        self.direction="Right"

    def print_info(self):
        print("current x="+str(self.current_x))
        print("current y="+str(self.current_y))
        print("direction="+str(self.direction))
        print("max_x="+str(self.max_x))
        print("max_y="+str(self.max_y))


    def move(self):
        match self.direction:
            case "Up":
                self.move_up()
            case "Down":
                self.move_down()
            case "Left":
                self.move_left()
            case "Right":
                self.move_right()
            case _:
                print("unexpected direction error")

        self.check_in_area()


    def check_in_area(self):
        if (
                self.current_y < 0
                        or
                self.current_y > self.max_y
                        or
                self.current_x < 0
                        or
                self.current_x > self.max_x
        ):
            self.out_of_map = True

    def move_up(self):
        self.current_y=self.current_y-1
    def move_down(self):
        self.current_y=self.current_y+1
    def move_left(self):
        self.current_x=self.current_x-1
    def move_right(self):
        self.current_x=self.current_x+1




if __name__ == "__main__":
    grid = read_input_as_grid("test.txt")
    #print_test(grid)
    grid=pretty_grid(grid)
    guard=Guard(grid)
    guard.print_info()
