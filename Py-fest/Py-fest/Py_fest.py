# The initial lineup
lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)
]

# 1. Add the headliner
headliner = ("The Byte Beats", "Synthwave", 90)
lineup.append(headliner)

#2
rb = lineup.pop(0)
print(lineup)
lineup.append(rb)
#3
lb = lineup.pop(0)
lineup.append(lb)
# 4. Calculate Total Time
total_minutes = 0
for name, genre, duration in lineup:
    total_minutes += duration

print("Final Lineup:")
for name, genre, duration in lineup:
    print(f"{name} ({genre}) - {duration} min")

print(f"\nTotal Festival Duration: