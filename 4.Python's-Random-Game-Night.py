#Task 1
import random
writing_utensils = ["Pencil", "Pen", "Marker"]

player = input("Choose Pencil, Pen, or Marker. ")
computer = random.choice(writing_utensils)

if player == computer:
    print("You got it right.")
else:
    print("You got it wrong. Computer choose " + computer + ".")