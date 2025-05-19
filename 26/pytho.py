
try:    
    num1 = float(input("Birinchi sonni kiriting: "))
    operator = input("Amal kiriting (+, -, *, /): ")
    num2 = float(input("Ikkinchi sonni kiriting: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            raise ValueError("nolga bolinmayd.")
    else:
        raise ValueError("yaroqsiz amal.")

    print(f"Natija: {result}")
except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Xatolik: {e}")    
