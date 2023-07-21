#import classes into this
from ingredient import Ingredient
from place import Place
from recipe import Recipe
import random

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
        user_input = input("Welcome to the Recipe Finder!\nType 'R' to see recipes, 'I' to see ingredients for a specific recipe, 'F' to find recipes by ingredient, 'S' for random suggestion, 'A' for all ingredients available, 'N' to add a new recipe, or 'X' to exit: ")

        if user_input.lower() == "r":
            print("Available recipes:")
            for recipe_name in recipes.keys():
                print(recipe_name)
            print("--------------------------")

        elif user_input.lower() == "i":
            recipe_name_input = input("Enter the recipe name to see its ingredients: ")
            recipe_name = recipe_name_input.strip()

            found_recipe = False
            for name in recipes.keys():
                if recipe_name.lower() == name.lower():
                    found_recipe = True
                    print(f"Ingredients for '{name}':")
                    for ingredient in recipes[name]:
                        print(ingredient)
                    break

            if not found_recipe:
                print("Recipe not found!")

        elif user_input.lower() == "x":
            break

        elif user_input.lower() == "f":
            ingredient_input = input("Enter the ingredient to find recipes: ")
            ingredient = ingredient_input.strip().lower()

            recipes_containing_ingredient = []
            for recipe_name, ingredients in recipes.items():
                if ingredient in map(str.lower, ingredients):
                    recipes_containing_ingredient.append(recipe_name)

            if len(recipes_containing_ingredient) > 0:
                print(f"Recipes containing '{ingredient}':")
                for recipe_name in recipes_containing_ingredient:
                    print(recipe_name)
            else:
                print(f"No recipes found containing '{ingredient}'.")

        elif user_input.lower() == "s":
            random_recipe = random.choice(list(recipes.keys()))
            print(f"Random recipe suggestion: {random_recipe}")

        elif user_input.lower() == "a":
            print("Available ingredients:")
            for ingredient in recipes.values():
                print(ingredient)
            print("--------------------------")

        elif user_input.lower() == "n":
            recipe_name_input = input("Enter the new recipe name: ")
            recipe_name = recipe_name_input.strip()

            
            if recipe_name.lower() in recipes.keys():
                print("Recipe already exists! Please enter a unique recipe name.")
            else:
                
                ingredients_list = input("Enter the ingredients (comma-separated): ")
                ingredients = [ingredient.strip() for ingredient in ingredients_list.split(",")]

                
                recipes[recipe_name] = ingredients

                print(f"Recipe '{recipe_name}' added successfully!")

        elif user_input.lower() == "x":
            break

        else:
            print("Invalid option. Please try again.")