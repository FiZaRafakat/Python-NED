# 1. Case Count
'''Write a Python function `case_count(text: str) -> dict` that counts the number of uppercase and
lowercase letters in a string.
Example:
Input: "Hello World"
Output: { "uppercase": 2, "lowercase": 8 }'''

def case_count(text: str) -> dict:
    counts = {"uppercase": 0, "lowercase": 0}
    for char in text:
        if char.isupper():
            counts["uppercase"] += 1
        elif char.islower():
            counts["lowercase"] += 1
    return counts

# Example usage
print(case_count("Hello World"))  # {"uppercase": 2, "lowercase": 8}
print(case_count("Python Programming"))  # {"uppercase": 2, "lowercase": 16}

# 2. Removing Vowels
'''Write a Python function `remove_vowels(text: str) -> str` that takes a string and returns a new string with
all vowels removed.'''

def remove_vowels(text: str) -> str:
    vowels = "aeiouAEIOU"
    return ''.join(char for char in text if char not in vowels)

# Example usage
print(remove_vowels("Hello World"))  # "Hll Wrld"
print(remove_vowels("Python Programming"))  # "Pythn Prgrmmng"

# 3. Palindrome Check
'''Write a Python function `is_palindrome(text: str) -&gt; bool` that checks if a string is a palindrome. A string
is a palindrome if it reads the same forward and backward (e.g., &quot;madam&quot;).'''

def is_palindrome(text: str) -> bool:
    text = text.lower().replace(" ", "")
    return text == text[::-1]

# Example usage
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False


# 4. String Rotation
'''Write a Python function `rotate_string(text: str, n: int) -&gt; str` that rotates the string by `n` positions. For
example, if the input is `&quot;abcdef&quot;` and `n = 2`, the output should be `&quot;cdefab&quot;`.'''

def rotate_string(text: str, n: int) -> str:
    n = n % len(text)  # Ensure n is within the bounds of the string length
    return text[n:] + text[:n]

# Example usage
print(rotate_string("abcdef", 2))  # "cdefab"
print(rotate_string("abcdef", 4))  # "efabcd"

# 5. String Reversal
'''Write a Python function `reverse_words(sentence: str) -> str` that reverses the order of words in a given
sentence.
Example:
Input: "hello world"
Output: "world hello"'''

def reverse_words(sentence: str) -> str:
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

# Example usage
print(reverse_words("hello world"))  # "world hello"
print(reverse_words("Python Programming is fun"))  # "fun is Programming Python"

# 6. Substring Check

'''Write a Python function `contains_substring(main: str, sub: str) -> bool` that checks if a substring exists
within a string.
Example:
Input: "hello world", "world"
Output: True'''

def contains_substring(main: str, sub: str) -> bool:
    return sub in main

# Example usage
print(contains_substring("hello world", "world"))  # True
print(contains_substring("hello world", "Python"))  # False