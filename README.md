
# Image Processing Toolkit

This repository contains a Python script that performs basic image manipulation tasks using the Pillow library. The script allows for adjusting the brightness of an image, converting it to grayscale, enhancing the edges, and saving the modified image.

## Installation

To run this script, you need Python and Pillow. You can install Pillow using pip:

```bash
pip install Pillow
```

## Usage

To use this script, you should have an image file in a supported format (e.g., JPG, PNG). Specify the path to your image when calling the function. Place the source image name in the 'image_path' variable and the destination image name in 'output_path' variable.

```python
image_path = 'path_to_your_image.jpg'
output_path = 'modified_image.jpg'
modify_image(image_path, output_path)
```

Run the script after setting the image path and output path. The script will adjust the brightness, apply a grayscale filter, enhance edges, and save the output in the same directory.

## Features

- **Brightness Adjustment**: Enhances the image brightness.
- **Grayscale Conversion**: Converts the image to grayscale, useful for highlighting intensity.
- **Edge Enhancement**: Applies an edge enhancement filter to highlight edges in the image.

## Contributing

Contributions to this project are welcome! You can contribute in several ways:

- Submit bugs and feature requests.
- Review source code changes.
- Improve the documentation.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Pillow library for providing the tools to manipulate images.
- Contributors who participate in the development of this toolkit.
