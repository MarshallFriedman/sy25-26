#Number 1
weight = int(input("Enter the weight of the potato: "))
if weight < 100:
    grade = "small"
elif weight <= 200 and weight >100:
    grade = "medium"
else:
    grade = "large"
print ("This is a " + str(grade) + " potato")
#Number 2
blemish_counts = []
for i in range(5):
    count = int(input("Enter the number of blemishes for potato: "))
    blemish_counts.append(count)
total = sum(blemish_counts)
average = total/5
print("Total blemishes: " + str(total) + ", Average blemishes: " + str(average))
#Number 3
all_potatoes = [0,2,5,1,0,8,3,0]
perfect_potatoes = []
for p in all_potatoes:
    if p == 0:
        perfect_potatoes.append(p)
num_total = len(all_potatoes)
num_perfect = len(perfect_potatoes)
percentage = (num_perfect/num_total)*100
print(f"Batch_quality:{percentage}%perfect")
