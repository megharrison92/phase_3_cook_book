#import classes into this
from ingredient import Ingredient
from place import Place
from recipe import Recipe

if __name__ == '__main__':

    recipes = {
    "French Toast": ['Bread', 'Eggs', 'Milk', 'Cinnamon', 'Sugar', 'Vanilla Extract', 'Maple Syrup'],
    "Bacon and Sausage Strata": ['French Bread', 'Ground Sausage', 'Bacon', 'Cheese', 'Eggs', 'Milk', 'Salt', 'Ground Mustard'],
    "Waffles": ['AP Flour', 'Sugar', 'Baking Powder', 'Salt', 'Milk', 'Eggs', 'Butter', 'Maple Syrup'],
    "Eggs Benedict": ['Eggs', 'Lemon Juice', 'White Pepper', 'Butter', 'Salt', 'White Vinegar', 'Canadian Bacon', 'English Muffins'],
    "Avocado Toast": ['Avocado', 'Lemon Juice', 'Salt', 'Black Pepper', 'Bread', 'Olive Oil', 'Red Pepper Flakes'],
    "Chicken Tenders": ['Chicken tender', 'AP Flour', 'Eggs', 'Breadcrumbs', 'Salt', 'Black Pepper', 'Paprika', 'Cooking Oil'],
    "Mac n Cheese": ['Elbow Macaroni', 'Cheese', 'Butter', 'Milk', 'AP Flour', 'Salt', 'Black Pepper'],
    "Grilled Cheese": ['Bread', 'Cheese', 'Butter'],
    "Tomato Soup": ['Butter', 'Onion', 'Garlic', 'Tomatoes', 'Vegetable broth', 'Spices']
    }

    while True:
        user_input = input("Welcome to the Recipe Finder CLI!\nType 'R' to see recipes, 'I' to see ingredients for a specific recipe, or 'X' to exit: ")

        if user_input.lower() == "r":
            print("Available recipes:")
            for recipe_name in recipes.keys():
                print(recipe_name)
            print("--------------------------")

        elif user_input.lower() == "i":
            recipe_name_input = input("Enter the recipe name to see its ingredients: ")
            recipe_name = recipe_name_input.strip()

            if recipe_name in recipes:
                print(f"Ingredients for '{recipe_name}':")
                for ingredient in recipes[recipe_name]:
                    print(ingredient)
            else:
                print("Recipe not found!")

        elif user_input.lower() == "x":
            break

        else:
            print("Invalid option. Please try again.")