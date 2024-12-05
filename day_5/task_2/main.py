import string

import numpy as np

def getInputFromFile():
    """Read lines from the input file."""
    with open("input.txt", "r") as file:
        lines = file.readlines()
    return lines

def deleteEndSymbols(lines):
    """Function for deleting \n symbol"""
    new_lines=[]
    for line in lines:
        new_lines.append(line.strip())
    return new_lines

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


def getRulesFromInput(lines):
    x=[]
    y=[]
    for line in lines:
        if line=="" or line==" ":
            break
        current_x=""
        current_y=""
        left=True # Which part of the line is working with, for exmp: 47|53 - 47 left, 53 right
        for char in line:
            if char=="|":
                left=False
            else:
                if left:
                    #print(f"left {current_x} {char}")
                    current_x=current_x+char # Should add first two symbols
                else:
                    #print(f"right {current_x} {char}")
                    current_y=current_y+char
        try:
            current_x=int(current_x)
            current_y=int(current_y)
        except Exception as e:
            print("Error when trying to convert to int strings in getRulesFromInput function"+e)

        x.append(current_x)
        y.append(current_y)

    if len(x)==len(y):
        return x,y
    else:
        return "unexpected, input not correct"


def printRules(x,y):
    if len(x)!=len(y):
        print("error, len not the same")
        return "unexpected, input not correct"
    else:
        for i in range(len(y)):
            print(f"{i} index, X={x[i]}, Y={y[i]}")
    return "success"


def checkOneRowOneRule(local_x, local_y, line):
    """
    This function checks the rule for one part x, y: index(local_x) < index(local_y) for one line.
    """
    # Ensure local_x and local_y are strings for consistent comparison
    local_x = str(local_x)
    local_y = str(local_y)
    # Convert all elements in the line to strings
    line = [str(num) for num in line]

    indexes_x = []
    indexes_y = []
    print(local_x, local_y, line)

    # Get the indexes of x and y in the line
    for index, num in enumerate(line):
        if num == local_x:
            indexes_x.append(index)
        elif num == local_y:
            indexes_y.append(index)

    print("Indexes of x:", indexes_x, "Indexes of y:", indexes_y)

    # Check the rule: index(local_x) < index(local_y)
    for index_x in indexes_x:
        for index_y in indexes_y:
            if index_x > index_y:
                return False

    return True



def getRowsFromInput(lines):
    new_lines=[]
    for line in lines:

        if not ("|" in line or line==""):
            new_lines.append(line)
    return new_lines


def convertingRows2DList(lines):
    """Converting lines with numbers to 2D arr"""
    arr = []
    for line in lines:
        row = []
        temp_num = ""
        for char in line:
            if char not in (",", " "):  # If the character is not a delimiter
                temp_num += char
            else:
                if temp_num:  # Only append if temp_num is not empty
                    row.append(temp_num)
                    temp_num = ""  # Reset temp_num for the next number
        if temp_num:  # Append the last number in the line if any
            row.append(int(temp_num))
        arr.append(row)  # Append the row to the 2D list
    return arr



def fullCheckLine(x,y,line):
    if len(x)!=len(y):
        print("error, len not the same")
        return "unexpected, input not correct"
    else:
        for i in range(len(y)):
            if not checkOneRowOneRule(x[i],y[i],line):
                return False
    return True


def getMiddleNumber(line):
    line_length = len(line)
    if line_length%2 != 0:
        return line[(line_length//2)]
    else:
        return "UNEXPECTED, line length even"


def sumMiddlePageForCorrect(x, y, lines):
    sum=0
    for i, line in enumerate(lines):
        if fullCheckLine(x,y,line):
            sum=sum+int(getMiddleNumber(line))
    return sum


def main():
    """Main function to execute the program."""
    lines = getInputFromFile()
    lines=deleteEndSymbols(lines)
    #print(lines)
    x,y=getRulesFromInput(lines)
    #printRules(x,y)
    nums_arr=convertingRows2DList(getRowsFromInput(lines))
    #print(checkOneRowOneRule(x[0],y[0],nums_arr[0]))

    #print(fullCheckLine(x,y,nums_arr[4]))
    #print(getMiddleNumber(nums_arr[2]))
    print(sumMiddlePageForCorrect(x, y, nums_arr))


# START PROGRAM
main()

