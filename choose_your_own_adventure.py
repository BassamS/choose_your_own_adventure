name = input("Type your name:  ")
print(f"welcome {name} to this adventure!")

answer = print("You are on a dirt road, it has come to an end and left or right. Which way would you like to go? (left or right?)").lower()

if answer == "left":
  
  
  answer = input("You come to a river, you can swim across or walk around it? type (swim) to swim across or(walk) to walk around: ")

  if answer == "swim":
    print("You swam across the river and were eaten by an allegator. You lost the game!")
  elif answer == "walk":
    print("You walked for many hours, run out of food and water and you lost the game!")
  else:
    print("Not a valid option. You loose!")

elif answer == "right":

else:
  print("Not a valid option. You loose!")  