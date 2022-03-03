import json

with open(f'./all_images.txt', 'r') as filehandle:
    all_images = json.load(filehandle)

print(all_images)