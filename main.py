from PIL import Image
import os
import sys


def resize_images(input_folder, output_folder, scale=0.1):

    # Check folders exist
    os.makedirs(output_folder, exist_ok=True)
    supported_formats = ('.jpg', '.jpeg', '.png')

    # Loop through files in input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(input_folder, filename)
            
            with Image.open(input_path) as img:
                new_size = (int(img.width * scale), int(img.height * scale))
                resized_img = img.resize(new_size, Image.LANCZOS)
                output_path = os.path.join(output_folder, filename)
                resized_img.save(output_path)
                print(f"Image {filename} resized and saved to {output_path}")


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Incorrect argument placed.\n\npython main.py [scale|float]")
        sys.exit()

    scale = float(sys.argv[1])
    input_folder = "./input"
    output_folder = "./output"
    
    resize_images(input_folder, output_folder, scale)