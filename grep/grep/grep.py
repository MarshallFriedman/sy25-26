import glob

# Get all .txt files in the directory

files = glob.glob("*.txt") 

pattern = input("Enter the pattern to search for: ")

for filename in files:
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for i,line in enumerate(lines):
        if pattern in line:
            print(filename,i,line.strip())