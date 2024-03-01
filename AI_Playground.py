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


def generate_coordinated_pastel_colors():
    """Generate three coordinated pastel colors by varying the hue."""
    base_hue = random.random()  # Random hue between 0.0 and 1.0
    saturation = 0.4  # Fixed saturation for pastel effect
    value = 0.9  # Fixed value for pastel effect

    hues = [(base_hue + i * 0.1) % 1.0 for i in range(3)]  # Generate hues with slight variation

    return [hsv_to_hex(hue, saturation, value) for hue in hues]


# Generate and print the coordinated pastel colors
pastel_colors = generate_coordinated_pastel_colors()
print(f"Pastel Color 1: {pastel_colors[0]}")
print(f"Pastel Color 2: {pastel_colors[1]}")
print(f"Pastel Color 3: {pastel_colors[2]}")
