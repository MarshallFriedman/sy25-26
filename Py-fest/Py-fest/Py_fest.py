print("\n---Py-Fest 2026 Stage Manager---")
print("1. View Lineup & Total Time")
print("2. Add a New Band")
print("3. Move First Band to End (Late Arrival)")
print("4. Remove a Band by Name")
print("5. Move Band to Specific Position")
print("6. Exit")
choice = input("Select an option (1-6): ")

lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)
]
total_time = 0
if choice == "1":
    print("\n---Current Lineup---")
    for i, artist in enumerate(lineup):
        print(str(artist[0]) + " -- " + str(artist[1])+ " -- " + str(artist[2]) + "minutes")
    
        total_time+=artist[2]
    print(f"Total Festival Duration: {total_time} minutes")
elif choice == "2":
    name = input("Enter Band Name: ")
    genre = input("Enter Band Genre: ")
    duration = int(input("Enter Performance Duration (minutes): "))
    lineup.append((name, genre, duration))
    print(f"{name} has been added to the lineup.")
elif choice == "3":
    print("Late band has been moved to the end of the lineup")
    late_band = lineup.pop[0]
    lineup.append(late_band)
    print(str(artist[0]) + " -- " + str(artist[1])+ " -- " + str(artist[2]) + "minutes")