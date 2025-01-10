# 1. Safe Addition
'''Write a Python function `safe_add(x: float, y: float) -&gt; float` that adds two numbers, and returns a
custom error message if the numbers are not valid floats.'''

def safe_add(x: float, y: float) -> float:
    try:
        return float(x) + float(y)
    except ValueError:
        return "Invalid input: both x and y must be valid floats"

# 2. Safe Subtraction
'''Write a Python function `safe_subtract(x: float, y: float) -&gt; float` that subtracts two numbers and handles
the case where the subtraction results in a negative number.'''

def safe_subtract(x: float, y: float) -> float:
    try:
        result = float(x) - float(y)
        if result < 0:
            return "Result is negative"
        return result
    except ValueError:
        return "Invalid input: both x and y must be valid floats"

# 3. Check for Division by Zero
# 3. Check for Division by Zero
'''Write a Python function `divide_numbers(x: float, y: float) -> float` that divides `x` by `y`. If `y` is zero, it
should return `Cannot divide by zero`.'''

def divide_numbers(x: float, y: float) -> float:
    try:
        if y == 0:
            return "Cannot divide by zero"
        return float(x) / float(y)
    except ValueError:
        return "Invalid input: both x and y must be valid floats"

# 4. Handling Invalid Input
'''Write a Python function `parse_input(value: str) -> int` that takes a string input and converts it to an
integer. If the conversion fails, return the message "Invalid input".'''

def parse_input(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        return "Invalid input"

# 5. Negative Numbers Handling
'''Write a Python function `add_positive_numbers(x: int, y: int) -> int` that adds two numbers but only if
both are positive. If either number is negative, raise a custom error: "Both numbers must be positive".'''

def add_positive_numbers(x: int, y: int) -> int:
    if x < 0 or y < 0:
        raise ValueError("Both numbers must be positive")
    return x + y

# 6. File Not Found Handling
'''Write a Python function `open_file(filename: str)` that attempts to open a file and prints an error
message if the file is not found.'''

def open_file(filename: str):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found"