import yaml
with open("Helmet_Dataset/data.yaml", "r") as file:
    data = yaml.safe_load(file)
print("Dataset Information")
for key, value in data.items():
    print(f"{key}:{value}")