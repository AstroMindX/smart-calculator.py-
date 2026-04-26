import json
from pathlib import Path

APP_VERSION = "4.0.0"
MAX_HISTORY = 10
HISTORY_FILE = Path(__file__).resolve().parent.parent / "history.txt"


history = []


def get_numbers(old_numbers):
    choice = input("Do you want to enter new numbers? (yes/no): ").lower().strip()
    if choice == "yes":
        try:
            numbers = list(map(float, input("Enter numbers separated by space: ").split()))
        except ValueError:
            print("Invalid input.")
            return None
    elif choice == "no":
        if not old_numbers:
            print("No previous numbers found. Enter new numbers.")
            return None
        numbers = old_numbers
    else:
        print("Please enter yes or no.")
        return None
    if len(numbers) < 2:
        print("Enter at least 2 numbers")
        return None
    return numbers


def add(numbers):
    return sum(numbers)


def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result


def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return None
        result /= num
    return result


def percentage(numbers):
    if numbers[1] == 0:
        return None
    return (numbers[0] * numbers[1]) / 100


def is_duplicate(operation, numbers):
    for item in history:
        if (
            isinstance(item, dict)
            and item.get("operation") == operation
            and item.get("numbers_used") == numbers
        ):
            return True
    return False


def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    history.append(json.loads(line))
                except json.JSONDecodeError:
                    history.append({"display": line})
    except FileNotFoundError:
        pass


def save_history(operation_name, numbers_used, result, equation_str):
    entry = {
        "operation": operation_name,
        "numbers_used": numbers_used,
        "result": result,
        "equation": equation_str,
    }
    if len(history) >= MAX_HISTORY:
        history.pop(0)
    history.append(entry)

    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(entry) + "\n")


def show_history():
    print("History of calculations:")
    if not history:
        print("No calculations in history yet.")
    else:
        for item in history[-MAX_HISTORY:]:
            if isinstance(item, dict) and "display" in item:
                print(item["display"])
            else:
                print(f"[{item['operation']}] {item['equation']} = {item['result']}")


def clear_history():
    history.clear()
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        file.write("")
    print("History cleared")


def print_menu():
    print(f"--- Smart Calculator v{APP_VERSION} ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")
    print("6. Show History")
    print("7. Clear History")
    print("8. Exit")


def main():
    numbers = []
    while True:
        print_menu()
        try:
            choice = int(input("Enter your choice:"))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue
        if choice == 1:
            numbers = get_numbers(numbers)
            if numbers is None:
                continue
            if is_duplicate("Add", numbers):
                print("You already calculated this before!")
                continue
            result = add(numbers)
            equation_str = " + ".join(map(str, numbers))
            print("Result:", result)
            save_history("Add", numbers, result, equation_str)
        elif choice == 2:
            numbers = get_numbers(numbers)
            if numbers is None:
                continue
            if is_duplicate("Subtract", numbers):
                print("You already calculated this before!")
                continue
            result = subtract(numbers)
            equation_str = " - ".join(map(str, numbers))
            print("Result:", result)
            save_history("Subtract", numbers, result, equation_str)
        elif choice == 3:
            numbers = get_numbers(numbers)
            if numbers is None:
                continue
            if is_duplicate("Multiply", numbers):
                print("You already calculated this before!")
                continue
            result = multiply(numbers)
            equation_str = " * ".join(map(str, numbers))
            print("Result:", result)
            save_history("Multiply", numbers, result, equation_str)
        elif choice == 4:
            numbers = get_numbers(numbers)
            if numbers is None:
                continue
            if is_duplicate("Divide", numbers):
                print("You already calculated this before!")
                continue
            result = divide(numbers)
            if result is None:
                print("Error: Division by zero")
                continue
            equation_str = " / ".join(map(str, numbers))
            print("Result:", result)
            save_history("Divide", numbers, result, equation_str)
        elif choice == 5:
            numbers = get_numbers(numbers)
            if numbers is None:
                continue
            if is_duplicate("Percentage", numbers):
                print("You already calculated this before!")
                continue
            result = percentage(numbers)
            if result is None:
                print("Error: Cannot calculate percentage with 0")
                continue
            equation_str = f"{numbers[1]}% of {numbers[0]}"
            print("Result:", result)
            save_history("Percentage", numbers, result, equation_str)
        elif choice == 6:
            show_history()
        elif choice == 7:
            clear_history()
        elif choice == 8:
            print("Exiting the calculator")
            break
        else:
            print("Invalid choice. Try again")


load_history()

if __name__ == "__main__":
    main()
