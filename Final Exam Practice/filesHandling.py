import random

# 1. Write Multiple Lines to a File
'''Write a Python program that creates a file named `records.txt` and writes 4 lines of data (name and age)
to it. Use a for loop to write the lines.'''

with open('records.txt', 'w') as file:
    data = [("John", 23), ("Jane", 29), ("Doe", 35), ("Smith", 40)]
    for name, age in data:
        file.write(f"{name}, {age}\n")
        
# 2. Count Words in a File
# 2. Count Words in a File
'''Write a Python program that opens a text file called `words.txt` and counts how many words are in the
file.'''

def count_words_in_file(filename):
    with open(filename, 'r') as file:
        contents = file.read()
        words = contents.split()
        return len(words)

word_count = count_words_in_file('records.txt')
print(f"Total number of words: {word_count}")

# 3. Reading and Appending to a File
'''Write a Python program that opens a file, reads its contents, and appends a new line of text to it. Then,
display the updated content of the file.'''

def append_and_display(filename, new_line):
    with open(filename, 'a') as file:
        file.write(new_line + '\n')
    
    with open(filename, 'r') as file:
        contents = file.read()
        print(contents)

append_and_display('records.txt', 'NewName, 45')

# 4. Extract Lines Containing a Specific Word
'''Write a Python program that reads a file called `log.txt` and prints all lines containing the word "error".'''

def extract_lines_with_word(filename, word):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if word in line:
                print(line.strip())

extract_lines_with_word('records.txt', 'Doe')

# 5. Copy Contents from One File to Another
'''Write a Python program that reads the content of a file called `source.txt` and writes it to a new file
called `destination.txt`.'''

def copy_file_contents(source, destination):
    with open(source, 'r') as src_file:
        contents = src_file.read()
    
    with open(destination, 'w') as dest_file:
        dest_file.write(contents)

copy_file_contents('source.txt', 'destination.txt')

# 6. Sort and Write Data to a File
'''Write a Python program that creates a file, writes some random numbers to it, and then reads and sorts
those numbers before writing the sorted list to a new file.'''


def write_random_numbers(filename, count):
    with open(filename, 'w') as file:
        for _ in range(count):
            number = random.randint(1, 100)
            file.write(f"{number}\n")

def sort_numbers_in_file(source, destination):
    with open(source, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]
    
    numbers.sort()
    
    with open(destination, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

write_random_numbers('random_numbers.txt', 10)
sort_numbers_in_file('random_numbers.txt', 'sorted_numbers.txt')