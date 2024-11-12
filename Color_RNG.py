import numpy as np

# Counter to be used in the loop
count = int(input("How many colors would you like to generate?: "))

# List to store generated colors
color_list = []


def color_rng():
    color_rgb = np.random.randint(0, 256, 3)
    # Convert components to regular Python integer (otherwise shows np.random before the number)
    color_rgb = tuple(int(c) for c in color_rgb)
    color_hex = "#{:02x}{:02x}{:02x}".format(*color_rgb)

    color_list.append((color_rgb, color_hex))
    return color_rgb, color_hex


# Generate the specified number of colors, in order:
for i in range(count):
    rgb_color, hex_color = color_rng()
    print(f"Color {i + 1}: RGB: {rgb_color}, HEX: {hex_color}")

# Display all stored colors
print("\nAll Generated Colors:")
for idx, color in enumerate(color_list):
    print(f"{idx + 1}: RGB: {color[0]}, HEX: {color[1]}")
