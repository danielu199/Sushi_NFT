from PIL import Image
from PIL.PngImagePlugin import PngImageFile
from IPython.display import display
import random
import json
import os
import json


bases = ["salmon", "algae"]
bases_weights = [10, 90]

hand = ["chopstick", "katana", "laser_sword", "nunchacko", 'none']
hand_weights = [20, 20, 10, 15, 10]

shoes = ["clogs",'none']
shoes_weights = [20, 80]

hat = ['caviar', 'wasabi', 'headband', 'none']
hat_weights = [10, 20, 30, 40]

background = ['background_1', 'background_2', 'background_3', 'background_4', 'background_5', 'background_6']
background_weights = [10, 25, 20, 20, 10, 15]

# Dictionary variable for each trait.
# Each trait corresponds to its file name

bases_files = {
    "salmon": "wrap1",
    "algae": "wrap2"
}

hand_files = {
    "chopstick": "hand1",
    "katana": "hand2",
    "laser_sword": "hand3",
    "nunchacko": "hand4",
    'none': 'none'
}

shoes_files = {
    "clogs": "shoes1",
    'none': 'none'
}

hat_files = {
    "caviar": "hat1",
    "wasabi": "hat2",
    "headband": "hat3",
    'none': 'none'
}

background_files = {
    'background_1': 'background_1',
    'background_2': 'background_2',
    'background_3': 'background_3',
    'background_4': 'background_4',
    'background_5': 'background_5',
    'background_6': 'background_6'
}

## Generate Traits

TOTAL_IMAGES = 200  # Number of random unique images we want to generate

all_images = []


# A recursive function to generate unique image combinations
def create_new_image():
    new_image = {}  #

    # For each trait category, select a random trait based on the weightings
    new_image['Background'] = random.choices(background, background_weights)[0]
    new_image["Base"] = random.choices(bases, bases_weights)[0]
    new_image["Hand"] = random.choices(hand, hand_weights)[0]
    new_image["Shoes"] = random.choices(shoes, shoes_weights)[0]
    new_image["Hat"] = random.choices(hat, hat_weights)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES):
    new_trait_image = create_new_image()

    all_images.append(new_trait_image)


    # Returns true if all images are unique
    def all_images_unique(all_images):
        seen = list()
        return not any(i in seen or seen.append(i) for i in all_images)


    print("Are all images unique?", all_images_unique(all_images))

    print(all_images)

# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

#### Generate images

os.mkdir(f'./images')

for item in all_images:
    im0 = Image.open(f'./backgrounds/{background_files[item["Background"]]}.png')
    im0 = im0.convert(mode='RGBA')
    im1 = Image.open(f'./bases/{bases_files[item["Base"]]}.png')
    im1 = im1.convert(mode='RGBA')
    im2 = Image.open(f'./hands/{hand_files[item["Hand"]]}.png')
    im2 = im2.convert(mode='RGBA')
    im3 = Image.open(f'./shoes/{shoes_files[item["Shoes"]]}.png')
    im3 = im3.convert(mode='RGBA')
    im4 = Image.open(f'./hats/{hat_files[item["Hat"]]}.png')
    im4 = im4.convert(mode='RGBA')

    # Create each composite
    com0 = Image.alpha_composite(im0, im1)
    com1 = Image.alpha_composite(com0, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)


    # Convert to RGB
    #rgb_im = com3.convert('RGB')
    rgb_im = com3
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)


with open(f'./all_images.txt', 'w') as filehandle:
    json.dump(all_images, filehandle)



