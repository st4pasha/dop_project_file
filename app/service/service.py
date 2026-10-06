

def write_to_file_cat(cat):
    from app.models.cat_class import cat_to_string
    with open('app/repositories/file.txt', 'a') as file:
        file.write(cat_to_string(cat).rstrip('\n') + '\n')

def read_from_file():
    with open('app/repositories/file.txt', 'r') as file:
        file_read = file.readlines()[:-1]
        return file_read

def write_to_file_dog(dog):
    from app.models.dog_class import dog_to_string
    with open('app/repositories/file.txt', 'a') as file:
        file.write(dog_to_string(dog).rstrip('\n') + '\n')