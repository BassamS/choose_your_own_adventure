name = input("Type your name:  ")
print(f"\nwelcome {name} to this adventure!")

answer = input(
    "\nYou are on a dirt road, it has come to an end and left or right. Which way would you like to go? (left or right?): ").lower()

if answer == "left":

    answer = input(
        "\nYou come to a river, you can swim across or walk around it? type (swim) to swim across or(walk) to walk around: ").lower()

    if answer == "swim":
        print(
            "\nYou swam across the river and were eaten by an allegator. You lost the game!")
    elif answer == "walk":
        print(
            "\nYou walked for many hours, run out of food and water and you lost the game!")
    else:
        print("\nNot a valid option. You loose!")

elif answer == "right":
    answer = input(
        "\nYou come a bridge, it looks wobbly, do you want to or head back or cross it (back/cross)? ").lower()

    if answer == "back":
        print(
            "\nYou go and you loose the game!")
    elif answer == "cross":
        answer = input(
            "\nYou cross the bridge and meet stranger, do you talk to them (yes/no)? ").lower()

        if answer == "yes":
            print("\nYou talk to the stranger, they give you gold. You Win!")
        elif answer == "no":
            print("\nYou ignore the stranger, they are offended. You Loose!")
        else:
            print("\nNot a valid option. You loose!")

    else:
        print("\nNot a valid option. You loose!")

else:
    print("\nNot a valid option. You loose!")

print(f"\nThank you for trying {name}")
