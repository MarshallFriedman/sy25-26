F1 = ["F1", "VW Off-Road-Bug", 105, (104, 142), 6000, 9, 1880, 4]
A1 = ["A1", "Hyundai Accent WRC", 220, (221, 300), 5500, 5.4, 1998, 4]
D1 = ["D1", "Mitsubishi Lancer", 220, (219, 300), 6200, 5.9, 1997, 4]
H4 = ["H4", "VW Polo Super 1600", 185, (158, 215), 7600, 8, 1600, 4]
D4 = ["D4", "Peugeot 206 WRC", 225, (221, 300), 5600, 5.4, 1996, 4]
E4 = ["E4", "Austin Metro 6", 240, (265, 360), 9800, 3.4, 3600, 6]
H2 = ["H2", "Mitsubishi Lancer", 198, (213, 290), 5500, 7.2, 1997, 4]
D3 = ["D3", "Seat Toledo Marathon", 220, (195, 330), 8400, 5.2, 2100, 5]
F2 = ["F2", "Mitsubishi Galant", 180, (216, 294), 5800, 6.3, 3395, 4]
G2 = ["G2", "Seat Ibliza Gti", 220, (205, 2800), 8400, 6.5, 1984, 4]

cars = [F1, A1, D1, H4, D4, E4, H2, D3, F2, G2]

def display_card(car):
    print("┌──────────────────────────────────────────┐")
    print(f"│ {car[0]} - {car[1]:<32}│")
    print("├────────────────────┬─────────────────────┤")
    print(f"│ Speed: {car[2]:<12}│ 0-60: {car[5]:<14}│")
    print(f"│ HP: {car[3][0]:<15}│ CCs: {car[6]:<13}│")
    print(f"│ RPM: {car[4]:<14}│ Cylinders: {car[7]:<6}│")
    print("└────────────────────┴─────────────────────┘")

# Display each car

i = 1

for car in cars:
    print(i,car[1])
    i = i + 1
while True:
    user_car = int(input("Select your car (1-10): "))
    display_card(cars[user_car - 1])

