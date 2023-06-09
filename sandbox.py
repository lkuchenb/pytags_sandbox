import json
from pprint import pprint
from sys import stdout
import yaml


# Some example data that we may see in a cell
data = "age=82; hair_color=blond; shoe_size=42"

# Load transformations from config
with open("config.yaml", mode="r", encoding="utf8") as config_file:
    transforms = yaml.load(config_file, yaml.Loader)

# Apply transformations to the data
for transform in transforms:
    data = transform(data)

# Print JSON
yaml.dump(data, stdout)
