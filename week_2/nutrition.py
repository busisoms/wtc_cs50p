"""
Program that prompts consumers users to input a fruit 
and then outputs the number of calories in one portion of that fruit
"""

def main():
    fruits = {"Apple": 130, "Avocado": 50, "Banana": 110, 
              "Cantaloupe": 50, "Grapefruit": 60, "Grapes": 90,
              "Honeydew Melon": 50, "Kiwifruit": 90, "Lemon": 15,
              "Lime": 20, "Nectrine": 60, "Orange": 80, 
              "Peach": 60, "Pear": 100, "Pineapple": 50, 
              "Plums": 70, "Strawberries": 50, "Sweet Cherries": 100, 
              "Tangerine": 50, "Watermelon": 80}
    
    prompt = input("Item: ").title()

    if prompt in fruits:
        print(f"Calories: {fruits[prompt]}")
    else:
        print("")

main()