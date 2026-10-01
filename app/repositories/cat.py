from app.models.cat_class import Cat

cat = Cat("Барсик", 3, 4.5, True, ["белый","рыжий"])

def get_cat():
    return cat