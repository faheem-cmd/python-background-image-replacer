from rembg import remove
from PIL import Image

# Store path of the images
input_path = 'messi.jpeg'
background_path = 'background.jpg'  # Replace with the path to your background image
output_path = 'output.png'

# Open the images and resize if necessary
def open_and_resize_image(path, size=None):
    image = Image.open(path)
    if size:
        image = image.resize(size, Image.LANCZOS)  # Use LANCZOS for high-quality downsizing
    return image

# Process the input image
input_image = open_and_resize_image(input_path)

# Removing the background from the given Image
foreground_image = remove(input_image)

# Open the background image
background_image = open_and_resize_image(background_path)

# Ensure the background image is large enough to accommodate the foreground image
bg_width, bg_height = background_image.size
fg_width, fg_height = foreground_image.size

# if bg_width < fg_width or bg_height < fg_height:
#     raise ValueError("Background image is smaller than foreground image.")

# Placing the foreground image onto the background image
# You can adjust (x, y) to position the foreground image as needed
x = (bg_width - fg_width) // 2
y = (bg_height - fg_height) // 2

background_image.paste(foreground_image, (x, y), foreground_image)

# Saving the final image
background_image.save(output_path)
