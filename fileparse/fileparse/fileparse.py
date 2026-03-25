filename = input("Enter the name of the file to parse: ")

file = open(filename, "r")

word = input("Enter the word to search for: ")

count = 0

line = file.readline()

while line:
    if word.upper() in line.upper():
        count += line.upper().count(word.upper())
    line = file.readline()

print(f"Searching for '{word}' in '{filename}'...")

print(f"{word} appears in the file {count} times.")
