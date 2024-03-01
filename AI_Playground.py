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


def generate_mixed_color_scheme():
    """Generate a color scheme with one pastel color, one dark non-pastel color, and one color being either black or white."""
    # Generate one pastel color
    pastel_hue = random.random()
    pastel_saturation = 0.4  # Fixed saturation for pastel effect
    pastel_value = 0.9  # Fixed value for pastel effect
    pastel_color = hsv_to_hex(pastel_hue, pastel_saturation, pastel_value)

    # Generate one dark non-pastel color
    dark_hue = random.random()
    dark_saturation = random.uniform(0.5, 1.0)  # Higher saturation for more vivid color
    dark_value = random.uniform(0.2, 0.5)  # Lower value for darkness
    dark_color = hsv_to_hex(dark_hue, dark_saturation, dark_value)

    # Randomly choose either black or white
    black_or_white = random.choice(["#FFFFFF", "#000000"])

    # Combine the colors into a list and shuffle it to randomize the order
    colors = [pastel_color, dark_color, black_or_white]
    random.shuffle(colors)

    return colors


# Generate and print the mixed color scheme
colors = generate_mixed_color_scheme()
print(f"Color 1: {colors[0]}")
print(f"Color 2: {colors[1]}")
print(f"Color 3: {colors[2]}")

