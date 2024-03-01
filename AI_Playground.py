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


def generate_matching_pastel_colors():
    """Generate three matching pastel colors."""
    base_hue = random.random()  # Random hue between 0.0 and 1.0
    # Base saturation and value ranges for pastel colors
    base_saturation = random.uniform(0.2, 0.4)
    base_value = random.uniform(0.8, 0.9)

    # Generate variations in saturation and value for matching colors
    variation = 0.05  # Variation factor
    colors = []
    for i in range(3):
        s_variation = base_saturation + (random.uniform(-variation, variation))
        v_variation = base_value + (random.uniform(-variation, variation))
        # Ensure saturation and value stay within valid ranges
        s = min(max(s_variation, 0.1), 0.5)
        v = min(max(v_variation, 0.7), 1.0)
        color_hex = hsv_to_hex(base_hue, s, v)
        colors.append(color_hex)

    return colors


# Generate and print the matching pastel colors
pastel_colors = generate_matching_pastel_colors()
print(f"Pastel Color 1: {pastel_colors[0]}")
print(f"Pastel Color 2: {pastel_colors[1]}")
print(f"Pastel Color 3: {pastel_colors[2]}")
