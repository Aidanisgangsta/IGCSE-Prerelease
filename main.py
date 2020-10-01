Baguette_Size = ["15cm", "30cm"]
Baguette_Bread = ["white", "brown", "seeded"]
Baguette_Filling = ["beef", "chicken", "cheese", "egg", "tuna", "turkey"]
Baguette_Salad = ["lettuce", "tomato", "sweetcorn", "cucumber", "peppers"]

customer_choice = {
    "Size": None,
    "BreadType": None,
    "Filling": None,
    "Salad1" : None,
    "Salad2": None,
    "Salad3": None
    }

print("Hello customer, please enter one of the following options for Baguette size:")
#Finds the customers baguette size
while True:
    for i in range(0, len(Baguette_Size)):
        if i > 0:
            print(", ", end="")
        print(Baguette_Size[i], end="")
    print("")
    size = input()

    if size.lower() in Baguette_Size:
        print(f"Ok you have selected a {size} baguette\n")
        customer_choice.update({"Size": size})
        break
    else:
        print("Please select a valid option out of the following:")

print("Please now select you bread type out of the following:")
#Finds the customers bread
while True:
    for i in range(0, len(Baguette_Bread)):
        if i > 0:            
            print(", ", end="")
        print(Baguette_Bread[i], end="")
    print("")
    bread = input()

    if bread.lower() in Baguette_Bread:
        print(f"Ok you have selected a {bread} baguette\n")
        customer_choice.update({"BreadType": bread})
        break
    else:
        print("Please select a valid option out of the following:")

print(customer_choice)