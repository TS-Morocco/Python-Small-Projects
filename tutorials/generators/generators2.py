import string

# Generate the lower case English letters
def letters():
    for c in string.ascii_lowercase:
        yield c


for letter in letters():
    print(letter)
