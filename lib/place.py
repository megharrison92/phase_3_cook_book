
class Place:

    all = []

    def __init__(self, name, recipe, ingredient ):
        self.recipe = recipe
        self.ingredient = ingredient
        self.name = name
        #name is pantry/fridge
        Place.all.append(self)

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise Exception("Must be a string greater than 0 characters")

    name = property(get_name, set_name)
    
    def get_recipe(self):
        return self._recipe
    
    def set_recipe(self, new_recipe):
        if isinstance(new_recipe, str) and len(new_recipe) > 0:
            self._recipe = new_recipe
        else:
            raise Exception("Must be a string greater than 0 characters")

    recipe = property(get_recipe, set_recipe)

    def get_ingredient(self):
        return self._ingredient
    
    def set_ingredient(self, new_ingredient):
        if isinstance(new_ingredient, str) and len(new_ingredient) > 0:
            self._ingredient = new_ingredient
        else:
            raise Exception("Must be a string greater than 0 characters")

    ingredient = property(get_ingredient, set_ingredient)

    def get_recipe(self):
        return self._recipe

    def set_recipe(self, recipe):
        from recipe import Recipe
        if isinstance(recipe, Recipe):
            self._recipe = recipe
        else:
            raise Exception("Must be a recipe object.")

    recipe = property(get_recipe, set_recipe)

    def get_ingredient(self):
        return self._ingredient

    def set_ingredient(self, ingredient):
        from ingredient import Ingredient
        if isinstance(ingredient, Ingredient):
            self._ingredient = ingredient
        else:
            raise Exception("Must be an ingredient object.")

    ingredient = property(get_ingredient, set_ingredient)