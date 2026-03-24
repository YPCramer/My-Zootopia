import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_skin_type(animals_data):
    skin_types = set()
    for animal in animals_data:
        if "skin_type" in animal["characteristics"]:
            skin_types.add(animal["characteristics"]["skin_type"])
    return skin_types


def serialize_animal(animal_obj):
    output = ""
    output += '<li class="cards__item">\n'
    if "name" in animal_obj:
        output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += '   <ul>\n'
    if "diet" in animal_obj["characteristics"]:
        output += f'        <li><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}</li>\n'
    if "locations" in animal_obj:
        output += f'        <li><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n'
    if "type" in animal_obj["characteristics"]:
        output += f'        <li><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</li>\n'
    if "group" in animal_obj["characteristics"]:
        output += f'        <li><strong>Group:</strong> {animal_obj["characteristics"]["group"]}</li>\n'
    output += '    </ul>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output


def main():
    animals_data = load_data('animals_data.json')
    skin_types = get_skin_type(animals_data)
    print("Available skin types: ")
    for skin_type in skin_types:
        print(f"- {skin_type}")
    user_skin_type = input("\nEnter a skin type: ")
    output = ""
    for animal in animals_data:
        if "skin_type" in animal["characteristics"]:
            if animal["characteristics"]["skin_type"].lower() == user_skin_type.lower():
                output += serialize_animal(animal)


    with open("animals_template.html", "r") as fileobj:
        template = fileobj.read()

    new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as write_object:
        write_object.write(new_html)

    print(f"Website generated for skin_type: {user_skin_type}")

if __name__ == "__main__":
    main()







