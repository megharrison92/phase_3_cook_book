
class Ingredient:

<<<<<<< HEAD
    def __init__(self, name, is_wet=False):
        self.name = name
        self.is_wet = is_wet

    def __str__(self):
        return self.name

ingredients = [
    Ingredient('bread'),
    Ingredient('eggs', is_wet=True),
    Ingredient('milk', is_wet=True),
    Ingredient('cinnamon'),
    Ingredient('sugar'),
    Ingredient('vanilla extract', is_wet=True),
    Ingredient('maple syrup', is_wet=True),
    Ingredient('french bread'),
    Ingredient('ground sausage'),
    Ingredient('bacon'),
    Ingredient('cheese'),
    Ingredient('salt'),
    Ingredient('ground mustard'),
    Ingredient('flour'),
    Ingredient('baking powder'),
    Ingredient('butter', is_wet=True),
    Ingredient('lemon juice', is_wet=True),
    Ingredient('white pepper'),
    Ingredient('white vinegar', is_wet=True),
    Ingredient('canadian bacon'),
    Ingredient('english muffins'),
    Ingredient('avocado'),
    Ingredient('olive oil', is_wet=True),
    Ingredient('red pepper flakes'),
    Ingredient('chicken tender'),
    Ingredient('breadcrumbs'),
    Ingredient('paprika'),
    Ingredient('cooking oil', is_wet=True),
    Ingredient('elbow macaroni'),
    Ingredient('shredded cheddar cheese'),
    Ingredient('unsalted butter', is_wet=True),
    Ingredient('onion'),
    Ingredient('garlic'),
    Ingredient('canned whole peeled tomatoes', is_wet=True),
    Ingredient('spices'),
    Ingredient('boneless & skinless chicken breast'),
    Ingredient('cooked chicken'),
    Ingredient('frozen mixed veg'),
    Ingredient('dried thyme and rosemary'),
    Ingredient('lasagna noodles'),
    Ingredient('ground beef'),
    Ingredient('crushed tomatoes and tomato sauce', is_wet=True),
    Ingredient('mozzarella cheese'),
    Ingredient('parmesan cheese'),
    Ingredient('meatballs'),
    Ingredient('parmesan cheese'),
    Ingredient('minced garlic'),
    Ingredient('dried oregano'),
    Ingredient('salt and pepper'),
    Ingredient('tomato sauce', is_wet=True),
    Ingredient('crushed tomatoes', is_wet=True),
    Ingredient('dried basil and thyme'),
    Ingredient('active dry yeast'),
    Ingredient('warm water', is_wet=True),
    Ingredient('dried oregano and basil'),
    Ingredient('shredded mozzarella cheese'),
    Ingredient('sliced pepperoni'),
    Ingredient('russet or yukon gold potatoes'),
    Ingredient('chopped fresh chives or parsley')
]
=======
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
>>>>>>> b97a70b72f9d4254eca1ac0204a9d1ef11860f81
