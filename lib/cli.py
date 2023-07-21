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
    "Classic Breaded Chicken Tenders": ['Chicken tender', 'AP Flour', 'Eggs', 'Breadcrumbs', 'Salt', 'Black Pepper', 'Paprika', 'Cooking Oil'],
    "Mac n Cheese": ['Elbow Macaroni', 'Cheese', 'Butter', 'Milk', 'AP Flour', 'Salt', 'Black Pepper'],
    "Grilled Cheese": ['Bread', 'Cheese', 'Butter'],
    "Tomato Soup": ['Butter', 'Onion', 'Garlic', 'Tomatoes', 'Vegetable broth', 'Spices']
    }

    user_input = input("Welcome to the Recipe Finder CLI! Print R to see recipes...")

    while user_input.lower() != "x":
        if user_input.lower() == "r":
            print("Available recipes:")
            for recipe_name in recipes.keys():
                print(recipe_name)
            print("--------------------------")
            break
        if user_input.lower() == "i":
            print("Available ingredients:")
            for recipe_name in recipes.keys():
                if isinstance(recipes.keys, list):
                    print(recipe_name.keys())
            print("--------------------------")
            break
