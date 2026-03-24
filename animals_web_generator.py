import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

# Step 2
output = ""
for animal in animals_data:
    if "name" in animal:
        output += f"Name: {animal['name']}\n"
    if "diet" in animal["characteristics"]:
        output += f"Diet: {animal["characteristics"]["diet"]}\n"
    if "locations" in animal:
        output += f"Location: {animal["locations"][0]}\n"
    if "type" in animal["characteristics"]:
        output += f"Type: {animal["characteristics"]["type"]}\n"
    output += "\n"

# Step 1
with open ("animals_template.html", "r") as fileobj:
    template = fileobj.read()

# Step 3
new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 4
with open("animals.html", "w") as write_object:
    write_object.write(new_html)

