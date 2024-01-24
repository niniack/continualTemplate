# parse_toml.py
import toml

with open("training.toml", "r") as file:
    data = toml.load(file)
    deps = data.get("dependencies", [])

with open("requirements.txt", "w") as f:
    for dep in deps:
        f.write(dep + "\n")
