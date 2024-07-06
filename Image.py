import os
from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    with Image.open(input_image_path) as image:
        resized_image = image.resize(size)
        resized_image.save(output_image_path)
        print(f"Resized image saved as {output_image_path}")

def resize_images_in_folder(folder_path, size):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_image_path = os.path.join(folder_path, filename)
            output_image_path = os.path.join(folder_path, f"resized_{filename}")
            resize_image(input_image_path, output_image_path, size)

if __name__ == "__main__":
    folder_path = '.'  
    new_size = (800, 600)  

    resize_images_in_folder(folder_path, new_size)
