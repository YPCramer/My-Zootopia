import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

# Step 2
output = ""
for animal in animals_data:
    output += '<li class="cards__item">\n'
    if "name" in animal:
        output += f'<div class="card__title">{animal["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    if "diet" in animal["characteristics"]:
        output += f'<strong>Diet:</strong>{animal["characteristics"]["diet"]}<br/>\n'
    if "locations" in animal:
        output += f'<strong>Location:</strong>{animal["locations"][0]}<br/>\n'
    if "type" in animal["characteristics"]:
        output += f'<strong>Type:</strong>{animal["characteristics"]["type"]}<br/>\n'
    output += '  </p>\n'
    output += "</li>\n"


# Step 1
with open ("animals_template.html", "r") as fileobj:
    template = fileobj.read()

# Step 3
new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 4
with open("animals.html", "w") as write_object:
    write_object.write(new_html)

