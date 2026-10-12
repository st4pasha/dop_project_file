from app.models.cat_class import Cat
from app.util import write_to_file, list_to_string, read_from_file

cat_name_colons = ["name", "age", "weight", "vacinnated", "colors"]
cats = [Cat("Барсик", 3, 4.5, True, ["белый","рыжий"]), Cat("Барсик2", 3, 4.5, True, ["белый","рыжий"])]
cat_file_path = "app/data/cats.csv"
metadata_file_path = "app/data/cats_metadata.csv"

#public function
def read_cats_data() -> list[Cat]:
    lst_str = read_from_file(cat_file_path)[1::]
    cat_lst = []
    for row in lst_str:
        cat_str = row.rstrip('\n')
        cat = list_to_class(cat_str)
        cat_lst.append(cat)
    return cat_lst

def update_cats_data(cats: list[Cat]):
    lst_str = []
    lst_str.append(list_to_string(cat_name_colons))

    for c in cats:
        cat_str = cat_to_string(c)
        lst_str.append(cat_str)

    write_to_file(lst_str, cat_file_path)

#private function
def cat_to_string(cat: Cat) -> str: 
    lst = [] # ['Барсик', '3', '4.5','True','['белый', 'рыжий']']
    id = get_id()
    write_new_id()

    lst.append(str(id))
    lst.append(str(cat.name))
    lst.append(str(cat.age))
    lst.append(str(cat.weight))
    lst.append(str(cat.vaccinated))
    lst.append(str(cat.colors))

    return "|".join(lst)

# lst -> Cat
def list_to_class(str: str) -> Cat: # Барсик|3|4.5|True|['белый', 'рыжий']
    # str -> 'Барсик', '3', '4.5','True','['белый', 'рыжий']'
    # name = Барсик
    # age = 3 (число)
    # weight = 4.5 (float)
    # vaccinated = True (bool)
    # color = ['белый', 'рыжий'] list[]
    lst = str.split("|")
    name = lst[0]
    age = int(lst[1])
    weight = float(lst[2])
    vaccinated = bool(lst[3])
    colors = parse_colors(lst[4])
    cat = Cat(name, age, weight, vaccinated, colors)
    return cat

def write_to_file_cat(cat):
    with open(cat_file_path, 'a') as file:
        file.write(cat_to_string(cat).rstrip('\n') + '\n')

def parse_colors(colors: str):
    colors_lst = colors.split(",")
    if len(colors_lst) > 0 and colors_lst != ['[]']:

        if len(colors_lst) == 1:
            colors1 = colors_lst[0].lstrip("[")
            colors1 = colors1.rstrip("]")
            colors_mas = [colors1.strip("''")]
            return colors_mas
        else:

            colors_mas = []

            for color in colors_lst:

                color = color.lstrip("[")
                color = color.rstrip("]")
                color = color.strip()
                colors_mas.append(color.strip("''"))

            return colors_mas  
    else:
        return []

def get_id():
    strings = read_from_file(metadata_file_path)[::-1]
    id = strings[0].strip()
    return id

def write_new_id():
    id_now = get_id()
    if id_now != "":
        write_to_file(["id_max\n" + str(int(id_now) + 1)], metadata_file_path)
    else: 
        write_to_file("1", metadata_file_path)

# пример простой parse_colors функции
"""def parse_colors(colors_str: str):
    colors_str = colors_str.lstrip("[")
    colors_str = colors_str.rstrip("]")
    colors = colors_str.split(",")

    for i in range(colors):
        color = colors[i].strip()
        colors[i] = color

    return colors

print(parse_colors(colors_empty))"""