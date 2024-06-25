PI = 3.14159265
PEOPLE_PER_LARGE = 7
PEOPLE_PER_MEDIUM = 3
PEOPLE_PER_SMALL = 1
LARGE_DIAMETER = 20
MEDIUM_DIAMETER = 16
SMALL_DIAMETER = 12
COST_LARGE = 14.68
COST_MEDIUM = 11.48
COST_SMALL = 7.28
#Functions for Task 2


def square(x):
    return x * x


def area(x, y):    #Calculates area of total pizzas of a given size
    return x * square(y/2) * PI

def main():
    #Task 1
    print("Please enter how many guests to order for:")
    people = int(input())
    large = people // PEOPLE_PER_LARGE
    medium = (people % PEOPLE_PER_LARGE) // PEOPLE_PER_MEDIUM
    small = ((people % PEOPLE_PER_LARGE) % PEOPLE_PER_MEDIUM) // PEOPLE_PER_SMALL
    print(str(large) + " large pizzas, " + str(medium) + " medium pizzas, and " + str(small) +
          " small pizzas will be needed.\n")
    #Task 2
    total_area = area(large, LARGE_DIAMETER) + area(medium, MEDIUM_DIAMETER) + area(small, SMALL_DIAMETER)
    avgpizza = total_area / people        #square inches of pizza per person
    print(f"A total of {total_area:.2f} square inches of pizza will be ordered ({avgpizza:.2f} per guest).\n")
    #Task 3
    print("Please enter the tip as a percentage (ie. 10 means 10%):")
    tip = float(input())
    subtotal = (large * COST_LARGE) + (medium * COST_MEDIUM) + (small * COST_SMALL)
    total = subtotal + subtotal * (tip / 100)
    print(f"The total cost of the event will be: ${total:.2f}\n")


if __name__ == "__main__":
    main()