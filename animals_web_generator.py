import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


def serialize_animal(animal_obj):
    output = ""
    output += '<li class="cards__item">\n'
    if "name" in animal_obj:
        output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    if "diet" in animal_obj["characteristics"]:
        output += f'<strong>Diet:</strong>{animal_obj["characteristics"]["diet"]}<br/>\n'
    if "locations" in animal_obj:
        output += f'<strong>Location:</strong>{animal_obj["locations"][0]}<br/>\n'
    if "type" in animal_obj["characteristics"]:
        output += f'<strong>Type:</strong>{animal_obj["characteristics"]["type"]}<br/>\n'
    if "group" in animal_obj["characteristics"]:
        output += f'<strong>Group:</strong>{animal_obj["characteristics"]["group"]}<br/>\n'
    output += '  </p>\n'
    output += "</li>\n"
    return output

output = ""
for animal_obj in animals_data:
    output += serialize_animal(animal_obj)


with open ("animals_template.html", "r") as fileobj:
    template = fileobj.read()


new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w") as write_object:
    write_object.write(new_html)

