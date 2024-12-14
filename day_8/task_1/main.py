import numpy as np
from collections import defaultdict


def parse_input(filename):
    """Parse the input file into a grid."""
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f.readlines()]


def find_antennas(grid):
    """Find all antenna positions and their frequencies."""
    antennas = defaultdict(list)
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell.isalnum():
                antennas[cell].append((x, y))
    return antennas


def is_collinear(p1, p2, p3):
    """Check if three points are collinear."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (y3 - y1) * (x2 - x1) == (y2 - y1) * (x3 - x1)


def find_antinodes(grid, antennas):
    """Find all unique antinode locations and mark them on a grid (for debug and visual purposes)."""
    antinodes = set()
    marked_grid = [row.copy() for row in grid]  # Create a copy of the grid for marking
    # probably could use deepcopy but let it be

    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                dx, dy = x2 - x1, y2 - y1
                # Mid-point is the average of two points (x1+x2)/2=mx....
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                if mx.is_integer() and my.is_integer():
                    antinode = (int(mx), int(my))
                    antinodes.add(antinode)
                    marked_grid[antinode[1]][antinode[0]] = '#'
                # Extend the line, purpose is to  find antinodes at 1/3 and 2/3 distances
                ax, ay = x1 - dx, y1 - dy
                bx, by = x2 + dx, y2 + dy
                if 0 <= ax < len(grid[0]) and 0 <= ay < len(grid):
                    antinodes.add((ax, ay))
                    marked_grid[int(ay)][int(ax)] = '#'
                if 0 <= bx < len(grid[0]) and 0 <= by < len(grid):
                    antinodes.add((bx, by))
                    marked_grid[int(by)][int(bx)] = '#'
    return antinodes, marked_grid


def print_grid(grid):
    """Print the 2D grid in beautiful way, row afte row."""
    for row in grid:
        print("".join(row))


def main():
    grid = parse_input("input.txt")
    antennas = find_antennas(grid)
    antinodes, marked_grid = find_antinodes(grid, antennas)

    print("Original Grid:")
    print_grid(grid)
    print("\nMarked Grid (with antinodes):")
    print_grid(marked_grid)
    print(f"\nTotal unique antinode locations: {len(antinodes)}")


if __name__ == "__main__":
    main()
