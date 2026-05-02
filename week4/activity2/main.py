from rectangle import Rectangle

def main():
    print("=== Rectangle Area & Perimeter Calculator ===")

    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    rect = Rectangle(length, width)

    area = rect.calculate_area()
    perimeter = rect.calculate_perimeter()

    print("\nResults:")
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")

if __name__ == "__main__":
    main()