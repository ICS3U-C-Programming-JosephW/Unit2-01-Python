#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Feb. 19, 2025
# This program uses user input to calculate the area and perimeter of any rectangle.


# A function determining the area and perimeter based on the user input.
def find_area_perimeter():
    length = int(input("Enter the length of the rectangle here (in cm): \n"))
    width = int(input("Enter the width of the rectangle here (in cm): \n"))
    print("If a rectangle has the dimensions:")
    print(f"{length}cm x {width}cm \n")
    print(f"The area is: {length * width}cm^2")
    print(f"The perimeter is: {2 * (length + width)}cm")


def main():
    find_area_perimeter()


if __name__ == "__main__":
    main()
