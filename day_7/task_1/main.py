def parse_input(filename):
    """
    Reads and parses the input file into test cases.
    Each line is split into a target value and a list of numbers.

    Args:
        filename (str): Path to the input file.

    Returns:
        list: A list of tuples where each tuple contains a target value (int)
              and a list of numbers (list of ints).
    """
    test_cases = []
    with open(filename, "r") as file:
        for line in file:
            if not line.strip():
                continue  # Skip empty lines
            target, numbers = line.split(":")
            target = int(target.strip())  # Extract and clean the target value
            numbers = list(map(int, numbers.strip().split()))  # Convert numbers to integers
            test_cases.append((target, numbers))
    return test_cases

def input_example(filename):
    # Example usage:
    test_cases = parse_input(filename)
    print(test_cases)
    #Detailed exmp
    for test_case in test_cases:
        print(test_case)
        print("---")
        print(test_case[0]) # test var
        print("---")
        print(test_case[1]) # components
        print("---")
        for component in test_case[1]:
            print(component)


if __name__ == "__main__":
    input_example("test.txt")