
# Key for and Sample of input map textfile
"""
open = o
barrier = x
cover = c
hero_spawn_area = h
enemy_spawn_area = e


sample_input = [
    [o,e,o,e,e],
    [o,o,x,x,o],
    [c,c,o,o,o],
    [o,x,x,x,o],
    [o,h,o,h,o]
    ]
"""

# Defines the size of a space @TODO(should be Window/cols)
space_size =  50    #len(window)/col

# Defines a temp input variable
sample_input = [
    ["o","e","o","e","e"],
    ["o","o","x","x","o"],
    ["c","c","o","o","o"],
    ["o","x","x","x","o"],
    ["o","h","o","h","o"]
    ]


# Creates the grid object that holds all the space objects
class GridObj():
    # Creates dict used to store space objects
    def __init__(self):
        self.spaces = {}
        self.get_spaces_from_file(sample_input)


    def get_spaces_from_file(self, input):
            # Gets number of columns based on input file
            num_columns = len(sample_input[0])
            # Sets the "grid_num" iterator used in object attribute & grid_dict
            grid_num = 1
            current_col = 1
            current_row = 1

            # Create grid's space objects based on input file
            for current_col in range(num_columns):
                for i in sample_input[current_row]:
                    if i == "o":
                        space = SpaceObj("o", grid_num, current_col, current_row)
                    elif i == "x":
                        space = SpaceObj("x", grid_num, current_col, current_row)
                    elif i == "c":
                        space = SpaceObj("c", grid_num, current_col, current_row)
                    elif i == "h":
                        space = SpaceObj("h", grid_num, current_col, current_row)
                    elif i == "e":
                        space = SpaceObj("e", grid_num, current_col, current_row)

                    # Iterates thorugh column and row numbers for grid
                    current_col += 1
                    if current_col > num_columns:
                        current_col = 1
                        current_row += 1

                    # Adds newly created space to the grid spaces dict.
                    self.spaces[grid_num] = space

                    # adds one to GridNum iterable
                    grid_num += 1


# Creates the space objects that puplate the grid from input file
class SpaceObj():
    def __init__(self, type, grid_num, current_col, current_row):
        # Defines number used in grid Dict.
        self.grid_num = grid_num
        # Defines grid column the space is located in
        self.col = current_col
        # Defines grid row the space is located in
        self.row = current_row
        # Defines x_range (aka widgth) of a space based on screensize/mapsize
        self.x_range = (current_col * space_size, current_col * space_size + space_size)
        # Defines y_range (aka height) of a space based on screensize/mapsize
        self.y_range = (current_row * space_size - space_size, current_row * space_size)
        # Creates of list of "items" that are located in a space
        self.items = []
        # Indicates if space is in use by a sprite
        self.occupied = False
        # Indicates which type of sprite is using space ("hero", "enemy", "obj")
        self.occupied_by = None
        # sets type of grid space based on injested file
        self.type = type
        # Call method to set space's type-specific attributes
        self.get_type_attributes(type)

    # Defines space's type-specific attributes based on injected data
    def get_type_attributes(self, type):
        # Sets walls/barriers attributes
        if type == "x":
            self.passible = False
            self.cover = "Full"
            self.spawn = None
        # Sets open space attributes
        elif type == "o":
            self.passible = True
            self.cover = "None"
            self.spawn = None
        # Sets hero spawn area space attributes (similiar to open space)
        elif type == "h":
            self.passible = True
            self.cover = "None"
            self.spawn = "Hero"
        # Sets enemy spawn area space attributes (similiar to open space)
        elif type == "e":
            self.passible = True
            self.cover = "None"
            self.spawn = "Enemy"
        # Sets cover attributes
        elif type == "c":
            self.passible = False
            self.cover = "Partial"
            self.spawn = None

grid = GridObj()
for space in grid.spaces.values():
    print("---------------------------")
    print("grid num: ", space.grid_num)
    print("x_range num: ", space.x_range)
    print("y_range num: ", space.y_range)
    print("Type: ", space.type)
    print("Passible: ", space.passible)
