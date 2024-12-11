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



def parsing_operators_between_two(num1, num2):
    operators=['+','*']
    results=[]
    result=int()
    for operator in operators:
        match operator:
            case '+':
                result=num1+num2
                results.append(result)
            case '*':
                result=num1*num2
                results.append(result)
            case _:
                print("huh?")

    return results


def parsing_operators_line(numbers):
    """
    Computes all possible results by combining numbers with '+' and '*' operators
    evaluated left-to-right as per the problem's rules.

    Args:
        numbers (list): A list of integers to combine with operators.

    Returns:
        list: A list of all possible results.
    """
    if len(numbers) == 1: #   object of type 'int' has no len()
        return [numbers[0]]
    if len(numbers) == 2:
        return parsing_operators_between_two(numbers[0], numbers[1])

    # Start with initial pair results
    results = parsing_operators_between_two(numbers[0], numbers[1])

    # Iteratively combine remaining numbers with each result
    for idx in range(2, len(numbers)):
        new_results = []
        for partial_result in results:
            new_results.extend(parsing_operators_between_two(partial_result, numbers[idx]))
        results = new_results

    #print(results)
    return results


def can_be_true_line(line):
    if line[0] in parsing_operators_line(line[1]):
        return True
    return False


def sum_callibration_results(data): # names of the functions according to task)
    sum=0
    for line in data:
        if can_be_true_line(line):
            sum=sum+line[0]

    return sum

if __name__ == "__main__":
    #input_example("test.txt")
    test_cases=parse_input("input.txt")
    #for test_case in test_cases:
        #parsing_operators_line(test_case[1])
        #print(can_be_true_line(test_case))
    print(sum_callibration_results(test_cases))