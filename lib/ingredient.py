
class Ingredient:

    def __init__(self, name, ingredient_type):
        self.name = name
        self.ingredient_type = ingredient_type

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