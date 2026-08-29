"""
Student Grade System
====================
Asks the user to enter a mark (0-100, decimals allowed) and prints the corresponding letter grade.

Grading Scale:
  90 – 100  →  A
  80 – 89   →  B
  70 – 79   →  C
  60 – 69   →  D
  Below 60  →  E
"""


def get_grade(mark: float) -> str:
    """Return the letter grade for a given mark (0-100, decimals allowed)."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def main():
    print("=" * 40)
    print("   Student Grade System")
    print("=" * 40)

    while True:
        raw = input("\nEnter your mark (0-100): ").strip()

        # --- Validate: must be a number ---
        try:
            mark = float(raw)
        except ValueError:
            print(f"  ✗ '{raw}' is not a valid number. Please enter a numeric value.")
            continue


        # --- Validate: must be within 0-100 ---
        if mark < 0:
            print(f"  ✗ Mark cannot be below 0. You entered: {mark}")
            continue
        if mark > 100:
            print(f"  ✗ Mark cannot exceed 100. You entered: {mark}")
            continue

        # --- Valid mark: calculate and display grade ---
        grade = get_grade(mark)
        # Display without trailing .0 for whole numbers
        display_mark = int(mark) if mark == int(mark) else mark
        print(f"\n  Mark: {display_mark} -> Grade: {grade}")
        print("-" * 40)

        # --- Ask if the user wants to check another mark ---
        again = input("\nCheck another mark? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nGoodbye! 👋")
            break


if __name__ == "__main__":
    main()
