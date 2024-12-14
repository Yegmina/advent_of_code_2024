from collections import defaultdict, namedtuple
from itertools import combinations

Coordinate = namedtuple("Coordinate", ["x", "y"])
# I could just use tuple instead, but this way is better: readability and efficient


def getInputFromFile():
    """Reads input file and returns a list of lines."""
    with open("input.txt", "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


def createAntennaMap(lines):
    """
    Create a dictionary mapping each frequency to its antenna positions
    and determine the grid size.
    """
    antennas = defaultdict(set)
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell != ".":
                antennas[cell].add(Coordinate(x, y))
    return antennas, len(lines)


def calculateDiff(pos1, pos2):
    """Calculate the directional difference and signs between two positions."""
    diff = (abs(pos1.x - pos2.x), abs(pos1.y - pos2.y))
    signs = (sign(pos1.x, pos2.x), sign(pos1.y, pos2.y))
    return diff, signs

def sign(a, b):
    """Return the sign of the difference between two numbers."""
    if a == b:
        return 0
    return (a - b) // abs(a - b)

def extendLine(start, diff, signs, grid_size):
    """
    Extend a line from a start point, adding all positions along the line
    until it leaves the grid bounds.
    """
    antinodes = set()
    current = Coordinate(start.x + signs[0] * diff[0], start.y + signs[1] * diff[1])
    while 0 <= current.x < grid_size and 0 <= current.y < grid_size:
        antinodes.add(current)
        current = Coordinate(current.x + signs[0] * diff[0], current.y + signs[1] * diff[1])
    return antinodes

def calculateAllAntinodes(pos1, pos2, grid_size):
    """
    Calculate all antinodes along the infinite line between two antennas,
    including their own positions.
    """
    diff, pos1_signs = calculateDiff(pos1, pos2)
    _, pos2_signs = calculateDiff(pos2, pos1)

    antinodes = {pos1, pos2}  # Include the antennas themselves
    antinodes.update(extendLine(pos1, diff, pos1_signs, grid_size))
    antinodes.update(extendLine(pos2, diff, pos2_signs, grid_size))

    return antinodes

def processAntennaPairs(positions, grid_size):
    """Calculate antinodes for all pairs of antennas in a frequency group."""
    antinodes = set()
    for pos1, pos2 in combinations(positions, 2):
        antinodes.update(calculateAllAntinodes(pos1, pos2, grid_size))
    return antinodes


def countUniqueAntinodes(lines):
    """
    Main calculation function: counts all unique antinode locations
    from the input grid lines.
    """
    antennas, grid_size = createAntennaMap(lines)
    antinodes = set()

    for frequency, positions in antennas.items():
        antinodes.update(processAntennaPairs(positions, grid_size))

    return len(antinodes)

def main():
    """Main program for part2."""
    lines = getInputFromFile()
    result = countUniqueAntinodes(lines)
    print(f"Part 2: Total unique antinode locations: {result}")

# start main for p2
if __name__ == "__main__":
    main()
