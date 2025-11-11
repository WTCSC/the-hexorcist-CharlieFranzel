digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_decimal(number_string, original_base):
    number_string = number_string.upper()
    total_value = 0
    power = 0

    for char in number_string[::-1]: 
        char_value = digits.index(char)
        total_value += char_value * (original_base ** power)
        power += 1

    return total_value


def from_decimal(decimal_number, target_base):
    if decimal_number == 0:
        return "0"

    result_string = ""

    while decimal_number > 0:
        remainder = decimal_number % target_base
        decimal_number = decimal_number // target_base
        result_string = digits[remainder] + result_string

    return result_string


# Main Program
print("Welcome to The Hexorcist. THE POWER OF MATH COMPELS YOU!\n")

num_str = input("Enter the number you want to convert: ").strip()
orig_base = int(input("Enter the number's CURRENT base (2-36): ").strip())
new_base = int(input("Enter the NEW base you want (2-36): ").strip())

print("\n...calculating with sticks and stones...\n")

decimal_value = to_decimal(num_str, orig_base)
converted_value = from_decimal(decimal_value, new_base)

print(f"'{num_str.upper()}' (Base-{orig_base}) is '{converted_value}' (Base-{new_base}).")
