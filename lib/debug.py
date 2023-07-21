import ipdb

from ingredient import Ingredient
from place import Place
from recipe import Recipe

if __name__ == '__main__':

    i1 = Ingredient("milk", "wet")
    i2 = Ingredient("bread", "dry")
    i3 = Ingredient("eggs", "wet")
    i4 = Ingredient("flour", "dry")

    r1 = Recipe("French Toast", "Breakfast")
    r2 = Recipe("Chicken Tenders", "Lunch")
    r3 = Recipe("Waffles", "Breakfast")
    r4 = Recipe("Mac n cheese", "Lunch")

    p1 = Place("fridge", r1, i1)
    p2 = Place("fridege",r4, i1)
    p3 = Place("pantry", r3, i3)
    p4 = Place("fridge", r1, i3 )


    ipdb.set_trace()