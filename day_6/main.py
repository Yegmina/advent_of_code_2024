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

def print_grid(local_grid):
    for row in local_grid:
        print(row)

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



def short_grid(pretty_grid):
    """Replacing human language words back to symbols."""
    local_short_grid = []
    for row in pretty_grid:
        short_row = []
        for element in row:
            match element:
                case "empty":
                    short_element = "."
                case "barrier":
                    short_element = "#"
                case "path":
                    short_element = "X"
                case "guardUp":
                    print("initial guard up")
                    short_element = "^"
                case "^" | "v" | ">" | "<":
                    print(f"guard found {element}")
                    short_element = element
                case _:
                    print(f"Unexpected symbol {element}")
                    short_element = "?"
            short_row.append(short_element)
        local_short_grid.append(short_row)

    return local_short_grid




class Guard:
    def __init__(self, local_grid):
        self.grid = local_grid
        self.x=[]  # list   of X coordinates where guard was
        self.y=[]  # list   of Y coordinates where guard was
        self.directions=[]
        self.current_x=-1
        self.current_y=-1
        self.direction="Up"
        self.out_of_map=False
        self.find_guard()
        self.max_x=len(grid)-1
        self.max_y=len(grid[0])-1
        self.looped=False


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
        #print("max_x="+str(self.max_x))
        #print("max_y="+str(self.max_y))


    def move(self):
        self.check_and_redirect()
        self.mark_path()

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
        self.check_looped()
        self.mark_guard()


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

    def check_and_redirect(self):
        if not (self.out_of_map or self.looped):
            try:
                if (self.direction=="Up") and (self.grid[self.current_y-1][self.current_x]=="barrier"):
                    self.direction="Right"
                if (self.direction=="Right") and (self.grid[self.current_y][self.current_x+1]=="barrier"):
                    self.direction="Down"
                if (self.direction=="Down") and (self.grid[self.current_y+1][self.current_x]=="barrier"):
                    self.direction="Left"
                if (self.direction=="Left") and (self.grid[self.current_y][self.current_x-1]=="barrier"):
                    self.direction="Up"
            except Exception as e:
                print(e)

    try:
        def move_up(self):
            self.current_y=self.current_y-1
        def move_down(self):
            self.current_y=self.current_y+1
        def move_left(self):
            self.current_x=self.current_x-1
        def move_right(self):
            self.current_x=self.current_x+1
    except Exception as e:
        print(e)

    def mark_path(self):
        if not (self.out_of_map or self.looped):
            try:
                self.grid[self.current_y][self.current_x]="path"
                self.x.append(self.current_x)
                self.y.append(self.current_y)
                self.directions.append(self.direction)
            except Exception as e:
                print(e)


    def mark_guard(self):
        if not (self.out_of_map or self.looped):
            try:
                match self.direction:
                    case "Up":
                        self.grid[self.current_y][self.current_x]="^"
                    case "Down":
                        self.grid[self.current_y][self.current_x]="v"
                    case "Left":
                        self.grid[self.current_y][self.current_x]="<"
                    case "Right":
                        self.grid[self.current_y][self.current_x]=">"
                    case _:
                        print(f"unexpected direction error")
            except Exception as e:
                print(e)

    def check_looped(self):
        if self.current_x in self.x:
                local_index=self.x.index(self.current_x)
                if self.current_y == self.y[local_index] and self.direction==self.directions[local_index]:
                    self.looped=True
                    return True
        return False






if __name__ == "__main__":
    grid = read_input_as_grid("test.txt")
    #print_test(grid)
    grid=pretty_grid(grid)
    guard=Guard(grid)
    print_grid(short_grid(guard.grid))
    #guard.print_info()
    for i in range(50):
        while not (guard.out_of_map or guard.looped):
            guard.move()
            print_grid(short_grid(guard.grid))



    #guard.print_info()
