class Recipe_ingredient:

    def __init__(self, recipe, ingredient):
        self.recipe = recipe
        self.ingredient = ingredient

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
    