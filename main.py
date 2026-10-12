from app.repositories.cat import update_cats_data, cat_file_path, list_to_class, read_cats_data, write_new_id, cat_to_string, get_id, write_to_file_cat
from app.models.cat_class import Cat
from app.util import read_from_file, list_to_string, write_to_file

# прочитать файл найди барсика 2 заменить ему имя на пушок обновить данные 

"""cats = read_cats_data()
for cat in cats:
    if cat.name == "Барсик2":
        cat.name = "Пушок"
update_cats_data(cats)

cats = read_cats_data()
print(cats)"""

print(get_id())
write_new_id()
print(get_id())