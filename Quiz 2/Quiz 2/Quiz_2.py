total = 0

for total in range(1,51,2):
    total = total + 1
print(total)



count = 0
word = "elephant"

letter = input("Enter a letter: ")
for l in word:
    if l == letter:
        count = count + 1

print(count)


#make number value = 1-10
#ask number from user
#make a number of attemps value
#if user guess number right then print "you win"
#if user guess number wrong then print "you lose"


secret = 3
count = 5

guess = int(input("enter a number between 1 and 10: "))
while count > 0:
    guess = int(input("enter a number between 1 and 10: "))
    if guess == secret:
        print("You win")
        break
    else:
        count = count - 1
        if count == 1:
            print("You lose")
    

        































