from PIL import Image, ImageEnhance, ImageFilter

def modify_image(image_path, output_path):
    # Load the image
    img = Image.open(image_path)

    # Adjust brightness
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.5)  # Increase brightness by 50%

    # Apply a filter (grayscale)
    img = img.convert('L')

    # Apply an additional filter (optional, e.g., edge enhancement)
    img = img.filter(ImageFilter.EDGE_ENHANCE)

    # Save the modified image to a new file
    img.save(output_path)

# Specify the path to your image file and output file
image_path = 'image.png'
output_path = 'modified_image.jpg'
modify_image(image_path, output_path)
