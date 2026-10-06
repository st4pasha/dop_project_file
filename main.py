from app.repositories.cat import cat
from app.service import service
from app.repositories.dog import dog


cat_1 = cat
service.write_to_file_cat(cat_1)


dog_2 = dog
service.write_to_file_dog(dog)
service.write_to_file_dog(dog)


file_read = service.read_from_file()
print(file_read)

