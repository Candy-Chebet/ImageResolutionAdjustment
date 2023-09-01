from PIL import Image

# Load the input image
input_image = Image.open("./rose.jpg")

# Down-sample and up-sample images
downsample_sizes = [512, 256, 128, 64, 32]
upsample_sizes = [1024, 512, 256, 128, 64]

for down_size, up_size in zip(downsample_sizes, upsample_sizes):
    # Down-sample the image
    downsampled_image = Image.new("RGB", (down_size, down_size))
    for y in range(down_size):
        for x in range(down_size):
            pixel = input_image.getpixel((x * 2, y * 2))
            downsampled_image.putpixel((x, y), pixel)
    
    # Save down-sampled image
    downsampled_image.save(f"downsampled_{down_size}.jpg")

    # Up-sample the image
    upsampled_image = Image.new("RGB", (up_size, up_size))
    for y in range(up_size):
        for x in range(up_size):
            pixel = downsampled_image.getpixel((x // 2, y // 2))
            upsampled_image.putpixel((x, y), pixel)
    
    # Save up-sampled image
    upsampled_image.save(f"upsampled_{up_size}.jpg")

# Change gray levels
gray_levels = [128, 64, 32, 16, 8, 4, 2]

for level in gray_levels:
    # Create a new grayscale image
    gray_image = Image.new("L", input_image.size)
    for y in range(input_image.height):
        for x in range(input_image.width):
            pixel_value = input_image.getpixel((x, y))
            new_pixel_value = int(pixel_value / 256 * level) * (256 // level)
            gray_image.putpixel((x, y), new_pixel_value)

    # Save grayscale image with reduced gray levels
    gray_image.save(f"gray_levels_{level}.jpg")
