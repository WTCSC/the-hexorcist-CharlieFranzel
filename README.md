[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/1Lpan6Kl)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21572429)


Hexorcist

This project is a universal base converter written in Python. It can take a number from any base between 2 and 36 and convert it into another base (also between 2 and 36). The script avoids all Python built-in base conversion functions.

How It Works

The converter uses two custom functions:

to_decimal()
Turns a number in any base into a regular decimal (base-10) number.

from_decimal()
Takes a decimal number and converts it into the new target base.

Both functions use loops, math, and a string of valid digits.

Running the Program

Run the script:

python3 hexorcist.py


You will be asked for:

The number you want to convert

The number’s original base

The new base you want

The program prints out the converted value.

Rules / Limitations

No bin(), hex(), oct(), format(), or int(x, base)

Only basic math and loops

Works with digits 0–9 and letters A–Z

Example
Enter the number you want to convert: 1A4
Enter the number's CURRENT base (2-36): 16
Enter the NEW base you want (2-36): 10


Output:

'1A4' (Base-16) is '420' (Base-10).