userfruit = input("Item: ")
fruits = [
    {"Fruit": "apple", "Calories": "130"},
    {"Fruit": "Avocado", "Calories": "50"},
    {"Fruit": "Banana", "Calories": "110"},
    {"Fruit": "Cantaloupe", "Calories": "50"},
    {"Fruit": "Grapefruit", "Calories": "60"},
    {"Fruit": "Grapes", "Calories": "90"},
    {"Fruit": "Honeydew Melon", "Calories": "50"},
    {"Fruit": "Kiwifruit", "Calories": "90"},
    {"Fruit": "Lemon", "Calories": "15"},
    {"Fruit": "Lime", "Calories": "20"},
    {"Fruit": "Nectarine", "Calories": "60"},
    {"Fruit": "Orange", "Calories": "80"},
    {"Fruit": "Peach", "Calories": "60"},
    {"Fruit": "pear", "Calories": "100"},
    {"Fruit": "Pineapple", "Calories": "50"},
    {"Fruit": "Plums", "Calories": "70"},
    {"Fruit": "Strawberries", "Calories": "50"},
    {"Fruit": "Sweet Cherries", "Calories": "100"},
    {"Fruit": "Tangerine", "Calories": "50"},
    {"Fruit": "Watermelon", "Calories": "80"}
]

for fruit in fruits:
    if userfruit == fruit["Fruit"]:
        print(fruit["Calories"])