# Programmer: Mya Reynolds
# Date: 2.29.24
# Program: AI Playground

print("This will be a place for me to play with programming using AI technology \n")

import random


def pretty_random_color():
    """Generate a 'pretty' random color in hex format by constraining the RGB values."""
    # Constrain each color component to be in the middle range (60-200 out of 0-255) to avoid too bright or too dark colors
    r = random.randint(60, 200)
    g = random.randint(60, 200)
    b = random.randint(60, 200)
    return '#{:02X}{:02X}{:02X}'.format(r, g, b)


def triadic_scheme(base_color):
    """Given a base color, calculate and return a triadic color scheme."""
    # Convert hex to RGB
    base_color_rgb = tuple(int(base_color.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))

    # Generate triadic colors by swapping R, G, B values
    triadic1_rgb = base_color_rgb[1], base_color_rgb[2], base_color_rgb[0]  # Shift Right
    triadic2_rgb = base_color_rgb[2], base_color_rgb[0], base_color_rgb[1]  # Shift Left

    # Convert RGB back to hex
    triadic1_hex = '#%02X%02X%02X' % triadic1_rgb
    triadic2_hex = '#%02X%02X%02X' % triadic2_rgb

    return base_color, triadic1_hex, triadic2_hex


# Generate a 'pretty' random color
base_color = pretty_random_color()

# Get the triadic color scheme
colors = triadic_scheme(base_color)

print(f"Base Color: {colors[0]}")
print(f"Triadic Color 1: {colors[1]}")
print(f"Triadic Color 2: {colors[2]}")

