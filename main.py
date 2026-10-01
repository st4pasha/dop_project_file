from app.repositories.cat import get_cat
from app.service import service

cat = get_cat()
service.write_to_file(cat)
cat_str = service.read_from_file()
print(cat_str)

cat_list = service.parse_row(cat_str)
print(cat_list)

cat_2 = service.list_to_class(cat_list)
print(cat_2)
