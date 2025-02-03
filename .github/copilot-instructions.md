# Instruction for splitting big functions into smaller ones

1. Identify the big function that needs to be split.
2. Analyze the functionality of the big function and break it down into smaller, logical units.
3. Create new functions for each of these smaller units.
4. Ensure that each new function has a single responsibility and a clear purpose.
5. Replace the code in the big function with calls to the new smaller functions.
6. Test the new functions individually to ensure they work correctly.
7. Test the overall functionality to ensure that splitting the big function did not introduce any bugs.

# Example:

# Before:
def big_function():
    # Part 1
    # Part 2
    # Part 3

# After:
def part1():
    # Part 1

def part2():
    # Part 2

def part3():
    # Part 3

def big_function():
    part1()
    part2()
    part3()