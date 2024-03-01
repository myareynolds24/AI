# Programmer: Mya Reynolds
# Date: 2.29.24
# Program: AI Playground

print("This will be a place for me to play with programming using AI technology \n")

import random


def hsv_to_hex(h, s, v):
    """Convert an HSV color to hex format."""
    import colorsys
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return '#{0:02X}{1:02X}{2:02X}'.format(int(r * 255), int(g * 255), int(b * 255))


def generate_coordinated_pastel_colors_with_black_or_white():
    """Generate two coordinated pastel colors and one color set to either black or white."""
    base_hue = random.random()  # Random hue between 0.0 and 1.0
    saturation = 0.4  # Fixed saturation for pastel effect
    value = 0.9  # Fixed value for pastel effect

    hues = [(base_hue + i * 0.1) % 1.0 for i in range(2)]  # Generate hues with slight variation

    pastel_colors = [hsv_to_hex(hue, saturation, value) for hue in hues]

    # Randomly choose one color to be either black or white
    black_or_white = random.choice(["#FFFFFF", "#000000"])

    # Randomly decide where to insert the black or white color
    insert_index = random.randint(0, 2)
    pastel_colors.insert(insert_index, black_or_white)

    return pastel_colors


# Generate and print the colors, with one being either black or white
colors = generate_coordinated_pastel_colors_with_black_or_white()
print(f"Color 1: {colors[0]}")
print(f"Color 2: {colors[1]}")
print(f"Color 3: {colors[2]}")
