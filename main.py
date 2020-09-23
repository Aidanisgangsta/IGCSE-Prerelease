Baguette_Size = ["30cm", "15cm"]
Baguette_Bread = ["White", "Brown", "Seeded"]
Baguette_Filling = ["Beef", "Chicken", "Cheese", "Egg", "Tuna", "Turkey"]
Baguette_Salad = ["Lettuce", "Tomato", "Sweetcorn", "Cucumber", "Peppers"]

customer_choice = {
    "Size": None,
    "BreadType": None,
    "Filling": None,
    "Salad1" : None,
    "Salad2": None,
    "Salad3": None
    }

print("Hello customer, please pick one of the following options for Baguette size:")

while True:
    for i in range(0, len(Baguette_Size)):
        print(Baguette_Size[i])
    size = input()
    if size in Baguette_Size:
        print(f"Ok you have selected a {size} baguette\n")
        customer_choice.update({"Size": size})
        break
    else:
        print("Please select a valid option")

print(customer_choice)