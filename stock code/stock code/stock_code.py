stock_count = int(input("How many items are in stock?"))
if stock_count <= 0:
    print("No items in stock.")
elif stock_count <= 5:
    print("Low stock.")
else:
    print("Stock is sufficient.")
sum = 0
for i in range(1,51,2):
    sum = sum + i
print(sum)