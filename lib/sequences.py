#!/usr/bin/env python3

def print_fibonacci(length):
    """
    Prints a list of the Fibonacci sequence up to the specified length.

    Args:
        length (int): The number of Fibonacci numbers to generate

    Returns:
        list: A list containing the Fibonacci sequence
    """
    if length <= 0:
        fibonacci_sequence = []
    elif length == 1:
        fibonacci_sequence = [0]
    elif length == 2:
        fibonacci_sequence = [0, 1]
    else:
        # Initialize the sequence with the first two numbers
        fibonacci_sequence = [0, 1]

        # Generate the remaining numbers
        for i in range(2, length):
            next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
            fibonacci_sequence.append(next_number)

    print(fibonacci_sequence)
    return fibonacci_sequence