"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from dish_ingredients."""
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """Append Cocktail or Mocktail based on alcohol presence."""
    
    if set(drink_ingredients) & ALCOHOLS:
        return drink_name + " Cocktail"
    else:
        return drink_name + " Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categorize dish based on ingredients."""

    if dish_ingredients.issubset(VEGAN):
        category = "VEGAN"
    elif dish_ingredients.issubset(VEGETARIAN):
        category = "VEGETARIAN"
    elif dish_ingredients.issubset(PALEO):
        category = "PALEO"
    elif dish_ingredients.issubset(KETO):
        category = "KETO"
    else:
        category = "OMNIVORE"

    return f"{dish_name}: {category}"


def tag_special_ingredients(dish):
    """Return dish name with special ingredients."""
    
    dish_name, ingredients = dish
    special = set(ingredients) & SPECIAL_INGREDIENTS
    
    return (dish_name, special)


def compile_ingredients(dishes):
    """Create master ingredient list."""
    
    master_set = set()
    
    for dish in dishes:
        master_set |= dish
        
    return master_set


def separate_appetizers(dishes, appetizers):
    """Remove appetizer dishes from dish list."""
    
    dishes_set = set(dishes)
    appetizers_set = set(appetizers)
    
    return list(dishes_set - appetizers_set)


def singleton_ingredients(dishes, intersection):
    """Find ingredients that appear only once."""
    
    all_ingredients = set()
    
    for dish in dishes:
        all_ingredients |= dish
        
    return all_ingredients - intersection
