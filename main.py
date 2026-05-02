#!/usr/bin/env python3

import sys
from PIL import Image

ASCII_BRIGHTNESS_VALUES = "@@#S%?*+;:,"

img = Image.open(f"images/{sys.argv[1]}")
width, height = img.size

def get_ascii_character(avg, alpha):
    if alpha == 0: return ' '

    index = int(avg / (255 / len(ASCII_BRIGHTNESS_VALUES)))
    if index > len(ASCII_BRIGHTNESS_VALUES) - 1: return " "
    return ASCII_BRIGHTNESS_VALUES[index]

def main():
    for y in range(height):
        for x in range(width):
            rgb_value = img.getpixel((x, y))
            avg = (rgb_value[0] + rgb_value[1] + rgb_value[2]) / 3
            char = get_ascii_character(avg, 255)

            if x == 0:
                print()
            print(" " + char, end="")

if __name__ == "__main__":
    main()

