import glob

files = glob.glob("server_dump/*.txt")

ok_count = 0
warn_count = 0
error_count = 0

for file in files:
    f = open(file, "r")
    first_line = f.readline()
    if "OK" in first_line:
        ok_count += 1
    elif "WARN" in first_line:
        warn_count += 1
    elif "ERROR" in first_line:
        error_count += 1
    f.close()

print(f"Ok: {ok_count}")
print(f"Warn: {warn_count}")
print(f"Error: {error_count}")