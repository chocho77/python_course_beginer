def calculate_triangle_area(base, height):
    return 0.5 * base * height


def calculate_rectangle_area(length, width):
    return length * width


def calculate_parallelogram_area(base, height):
    return base * height


def main():
    print("Area Calculator")
    print("1. Triangle")
    print("2. Rectangle")
    print("3. Parallelogram")

    choice = input("Choose a shape (1-3): ")

    if choice == '1':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(base, height)
        print(f"Area of the triangle: {area}")
    elif choice == '2':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print(f"Area of the rectangle: {area}")
    elif choice == '3':
        base = float(input("Enter the base of the parallelogram: "))
        height = float(input("Enter the height of the parallelogram: "))
        area = calculate_parallelogram_area(base, height)
        print(f"Area of the parallelogram: {area}")
    else:
        print("Invalid choice. Please run the program again and choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
