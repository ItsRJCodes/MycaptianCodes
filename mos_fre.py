def most_frequent(string):
    """Print the letters of a string in decreasing order of frequency."""
    # Convert the string to lowercase for case-insensitive counting
    string = string.lower()

    # Create a dictionary to count the frequency of each letter
    frequency = {}
    for char in string:
        if char.isalpha():  # Only count alphabetic characters
            frequency[char] = frequency.get(char, 0) + 1

    # Sort the dictionary by frequency in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # Print the letters and their frequencies
    for char, count in sorted_frequency:
        print(f"{char} = {count:02}")

# Input from the user
input_string = input("Please enter a string: ")
print("\nOutput:")
most_frequent(input_string)
