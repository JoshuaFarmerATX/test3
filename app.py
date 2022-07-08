def clean_dogs(list_of_dogs):
    dogs_list = []
    for i in list_of_dogs:
        if "Fi" in i:
            dogs_list.append(i)
    return dogs_list

dogs = ["Fido", "Franky", "Fitzgerald"]
dogs_two = ["Chip", "Alf", "Filp"]

dogs_dict = [{
    "name": "Spikey",
    "age": 2
},
{
    "name": "Henrietta",
    "age": 4
}]
dogs_dict_two = {}

print(dogs_dict[1]["name"])
# dogs_dict['name'] = 'fido'

dogs_dict_two["name_two"] = dogs_dict[1]["name"]
print(dogs_dict_two)

# Some other things in comment