import os
from PIL import Image

def resize_image(input_path, output_path, max_size):
    with Image.open(input_path) as img:
        # Calculate the new size maintaining the aspect ratio
        ratio = min(max_size / img.width, max_size / img.height)
        new_size = (int(img.width * ratio), int(img.height * ratio))
        resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
        resized_img.save(output_path)

def process_directory(directory, max_size):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                input_path = os.path.join(root, file)
                resize_image(input_path, input_path, max_size)
                print(f'Resized {input_path}')

# Set the directories and maximum size
directories = ['./test/melanoma', './test/nevus', './test/seborrheic_keratosis',
               './train/melanoma', './train/nevus', './train/seborrheic_keratosis',
               './valid/melanoma', './valid/nevus', './valid/seborrheic_keratosis']
max_size = 1000

# Process each directory
for directory in directories:
    process_directory(directory, max_size)