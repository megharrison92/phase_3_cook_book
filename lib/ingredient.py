
class Ingredient:
    all = []    

    def __init__(self, name, ingredient_type):
        self.name = name
        self.ingredient_type = ingredient_type
        Ingredient.all.append(self)

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise Exception("Must be a string greater than 0 characters")

    name = property(get_name, set_name)

    def get_ingredient_type(self):
        return self._ingredient_type 
    
    def set_ingredient_type(self, new_ingredient_type):
        if isinstance(new_ingredient_type, str) and len(new_ingredient_type) > 0:
            self._ingredient_type = new_ingredient_type
        else:
            raise Exception("Must be a string greater than 0 characters")

    ingredient_type = property(get_ingredient_type, set_ingredient_type)

    @property
    def places(self):
        from place import Place
        ingredient_list = []
        for place in Place.all:
            if place.ingredient == self:
                ingredient_list.append(place)
        return ingredient_list
    
    @property
    def recipes(self):
        recipe_list = []
        for place in self.places:
            if place.recipe not in recipe_list:
                recipe_list.append(place.recipe)
        return recipe_list