import ipdb

from ingredient import Ingredient
from recipe_ingredient import Recipe_ingredient
from recipe import Recipe

if __name__ == '__main__':

    #Breakfast Ingredient
    break1 = Ingredient('French Toast', 'Breakfast')
    break2 = Ingredient('Bacon and Sausage Strata', 'Breakfast')
    break3 = Ingredient('Waffles', 'Breakfast')
    break4 = Ingredient('Egg Benedict', 'Breakfast')
    break5 = Ingredient('Avocado', 'Breakfast')

    #Lunch Ingredient
    lunch1 = Ingredient('Classic Breaded Chicken Tenders', 'Lunch')
    lunch2 = Ingredient('Mac-n-Cheese', 'Lunch')
    lunch3 = Ingredient('Grilled Cheese', 'Lunch')
    lunch4 = Ingredient('Tomato Soup', 'Lunch')
    lunch5 = Ingredient('Chicken and Bacon Panini', 'Lunch')

    #Dinner Ingredient
    dinner1 = Ingredient('Chicken Pot Pie', 'Dinner')
    dinner2 = Ingredient('Lasagne', 'Dinner')
    dinner3 = Ingredient('Spaghetti and Meatballs', 'Dinner')
    dinner4 = Ingredient('Pizza', 'Dinner')
    dinner5 = Ingredient('Mashed Potato', 'Dinner')

    ipdb.set_trace()