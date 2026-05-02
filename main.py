#!/usr/bin/env python3

import sys
from PIL import Image

ASCII_BRIGHTNESS_VALUES = "@@#S%?*+;:,"

IMAGE_NAME, WIDTH, HEIGHT, USE_COLOR = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4] == "True"
img = Image.open(f"images/{IMAGE_NAME}").resize((WIDTH, HEIGHT)).convert("RGBA")

def get_ascii_character(avg, alpha):
    if alpha == 0: return ' '

    index = int(avg / (255 / len(ASCII_BRIGHTNESS_VALUES)))
    if index > len(ASCII_BRIGHTNESS_VALUES) - 1: return " "
    return ASCII_BRIGHTNESS_VALUES[index]

def main():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            r, g, b, a = img.getpixel((x, y))
            avg = sum([r, g, b]) / 3
            char = get_ascii_character(avg, a)

            # courtesy of https://stackoverflow.com/questions/74589665/how-to-print-rgb-colour-to-the-terminal
            if (USE_COLOR):
                color_str = f"[38;2;{r};{g};{b}m{char}"
                char = "\033" + color_str + "\033[0m"

            if x == 0:
                print()
            print(" " + char, end="")

if __name__ == "__main__":
    main()

