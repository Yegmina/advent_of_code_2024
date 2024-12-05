import string

import numpy as np

def getInputFromFile():
    """Read lines from the input file."""
    with open("input.txt", "r") as file:
        lines = file.readlines()
    return lines

def putInfoToMatrix(lines):
    """Convert lines from the file into a numpy matrix."""
    rows = len(lines)
    cols = len(lines[0].strip())
    matrix = np.empty((rows, cols), dtype=str)
    for i, line in enumerate(lines):
        matrix[i] = list(line.strip())
    return matrix


def reverseString(word):
    """Reverse giver word and return new one, for example qwerty become ytrewq """
    reversed_word=""
    word_length = len(word)
    for i in range(word_length):
        reversed_word += word[-i-1]
    #print(reversed_word)
    return reversed_word


def horizontalAppearanceCalculator(matrix, word):
    """Count the appearances of a word in horizontal lines of the matrix."""
    counter = 0
    word_length = len(word)
    for i, line in enumerate(matrix):
        #print(f"i={i} and line={line}")
        for j in range(len(line) - word_length + 1):  # Prevent out-of-bounds slicing
            #print(f"j={j} and char={line[j]}")
            current_word = ''.join(line[j:j + word_length])
            if current_word == word or current_word == reverseString(word):
                counter += 1
                #print(f"word {word} appears {counter} times")
    #print(f"Total horizontal appearances of '{word}': {counter}")
    return counter


def rotateMatrix90(matrix):
    """Rotate the matrix by 90 degrees clockwise."""
    return np.rot90(matrix, k=-1)  # k=-1 rotates clockwise


def verticalAppearanceCalculator(matrix, word):
    """Count the appearances of a word in vertical lines of the matrix."""
    matrix=rotateMatrix90(matrix)
    print(f"rotated matrix by 90 degrees is {matrix}")
    counter= horizontalAppearanceCalculator(matrix, word)
    return counter


def getDiagonalsMatrix(matrix):
    """Extract all main and anti-diagonals from the matrix."""
    rows, cols = matrix.shape
    diagonals = []

    # Main diagonals (top-left to bottom-right)
    for diag in range(-(rows - 1), cols):
        main_diag = [matrix[i, i - diag] for i in range(max(0, diag), min(rows, cols + diag))]
        diagonals.append(''.join(main_diag))

    # Anti-diagonals (top-right to bottom-left)
    flipped_matrix = np.fliplr(matrix)  # Flip the matrix horizontally
    for diag in range(-(rows - 1), cols):
        anti_diag = [flipped_matrix[i, i - diag] for i in range(max(0, diag), min(rows, cols + diag))]
        diagonals.append(''.join(anti_diag))

    return diagonals



def countWordAppearancesInArray(words_array, searching_word):
    """Count occurrences of the word and its reverse in an array of strings."""
    counter = 0
    word_length = len(searching_word)

    for current_string in words_array:
        for i in range(len(current_string) - word_length + 1):
            current_word = current_string[i:i + word_length]
            if current_word == searching_word or current_word == reverseString(searching_word):
                counter += 1
    return counter


def countAppearanceInMatrix(matrix, word):
    """Count all appearances of the word in horizontal, vertical, and diagonal directions."""
    diagonals = getDiagonalsMatrix(matrix)
    diagonal_count = countWordAppearancesInArray(diagonals, word)
    horizontal_count = horizontalAppearanceCalculator(matrix, word)
    vertical_count = verticalAppearanceCalculator(matrix, word)
    total_count = diagonal_count + horizontal_count + vertical_count
    return total_count


def main():
    """Main function to execute the program."""
    lines = getInputFromFile()
    matrix = putInfoToMatrix(lines)
    print("Matrix:")
    print(matrix)
    word = "XMAS"  # Define the word to search for
    #horizontalAppearanceCalculator(matrix, word)
    #verticalAppearanceCalculator(matrix, word)
    #print(getDiagonalsMatrix(matrix))
    #print(countWordAppearancesInArray(getDiagonalsMatrix(matrix), word))
    result=countAppearanceInMatrix(matrix, word)
    print(f"result {result}")
    print(lines)

# START PROGRAM
main()

