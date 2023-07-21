

class Recipe:

    def __init__(self, name, food_type):
        self.name = name
        self.food_type = food_type 
        

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise Exception("Must be a string greater than 0 characters")

    name = property(get_name, set_name)

    def get_food_type(self):
        return self._food_type 
    
    def set_food_type(self, new_food_type):
        if isinstance(new_food_type, str) and len(new_food_type) > 0:
            self._food_type = new_food_type
        else:
            raise Exception("Must be a string greater than 0 characters")
        
    food_type = property(get_food_type, set_food_type)

    @property
    def places(self):
        from place import Place
        place_list = []
        for place in Place.all:
            if place.recipe == self:
                place_list.append(place)
        return place_list
    
    @property
    def ingredients(self):
        ingredient_list = []
        for place in self.places:
            if place.ingredient not in ingredient_list:
                ingredient_list.append(place.ingredient)
        return ingredient_list